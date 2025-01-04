from flask import current_app, url_for, redirect, request
from rauth import OAuth2Service
import json
from . import auth

class OAuthSignIn:
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    @classmethod
    def get_provider(cls, provider_name):
        if cls.providers is None:
            cls.providers = {}
            for provider_class in cls.__subclasses__():
                provider = provider_class()
                cls.providers[provider.provider_name] = provider
        return cls.providers.get(provider_name)

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        callback_url = url_for('auth.oauth_callback', provider=self.provider_name,
                      _external=True)
        print(f"Callback URL: {callback_url}")
        return callback_url

class GoogleSignIn(OAuthSignIn):
    def __init__(self):
        super(GoogleSignIn, self).__init__('google')
        self.service = OAuth2Service(
            name='google',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            access_token_url='https://accounts.google.com/o/oauth2/token',
            base_url='https://www.googleapis.com/oauth2/v1/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email profile',  # Added 'profile' to get name information
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        
        # Get OAuth2 token
        try:
            oauth_session = self.service.get_auth_session(
                data={
                    'code': request.args['code'],
                    'grant_type': 'authorization_code',
                    'redirect_uri': self.get_callback_url()
                },
                decoder=json.loads  # Changed decoder
            )
            
            # Get user info
            me = oauth_session.get('userinfo').json()
            
            return (
                me.get('email'),
                me.get('given_name'),
                me.get('family_name')
            )
        except Exception as e:
            print(f"OAuth error: {str(e)}")
            return None, None, None
#!/usr/bin/env python3
import os
from app import create_app, db
from app.models import User
from flask_migrate import upgrade

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

def main():
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(
        host=host,
        port=port,
        debug=os.environ.get('FLASK_DEBUG', 'True') == 'True'
    )

if __name__ == '__main__':
    main()
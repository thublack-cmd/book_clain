from flask import flash, redirect, url_for

from app import create_app

app = create_app()

@app.route('/')
def index():
    return redirect(url_for('cubatta.audit_view'))

if __name__ == '__main__':
    app.run()

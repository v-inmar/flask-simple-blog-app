from flask import render_template
from flask_wtf.csrf import CSRFError


def load_errors(app):

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        return render_template("errors/csrf_error.html"), e.code
    
    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/not_found.html"), e.code
    
    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/server_error.html"), e.code
# Less clutter in app package.
# Main use is for cleaner(debatable) organization
# New modules should be added here


def load_modules(app):
    '''
    Loads all the blueprints and models from each of the modules.
    @param app: Flask instance
    '''
    # -- Load the blueprints and models from each module -- #

    # ==== Auth Module ==== #
    #  - Blueprint - #
    from ..modules.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    #  - Models - #
    # auth module does not have a model





    # ==== Dashboard Module ==== #
    #  - Blueprint - #
    from ..modules.dashboard.routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    #  - Models - #
    # dashboard module does not have a model





    # ==== Post Module ==== #
    #  - Blueprint - #
    from ..modules.post.routes import post_bp
    app.register_blueprint(post_bp)

    #  - Models - #
    from ..modules.post.models.post_model import PostModel
    from ..modules.post.models.post_pid_model import PostPIDModel





    # ==== User Module ==== #
    #  - Blueprint - #
    from ..modules.user.routes import user_bp
    app.register_blueprint(user_bp)

    #  - Models - #
    from ..modules.user.models.user_model import UserModel
    from ..modules.user.models.user_pid_model import UserPIDModel
    from ..modules.user.models.user_token_model import UserTokenModel

from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from .views import views
    from .predict import predict

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(predict, url_prefix='/')

    return app
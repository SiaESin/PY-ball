from flask import Flask 

from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P0tter619@localhost:5432/ball_py'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
            
    @app.route('/')
    def test(): 
        return 'Hello world!'
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    from . import animals 
    app.register_blueprint(animals.bp)
    
    return app

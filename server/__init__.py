# project/server/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask
from flask_bcrypt import Bcrypt



################
#### config ####
################

app = Flask(
    __name__,
)


app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(app_settings)


####################
#### extensions ####
####################
bcrypt = Bcrypt(app)

###################
### blueprints ####
###################

from server.article.views import article_blueprint

app.register_blueprint(article_blueprint)

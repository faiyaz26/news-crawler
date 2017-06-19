# project/server/main/views.py


#################
#### imports ####
#################
import json

from flask import Blueprint, request, jsonify
from server.article.model import NewsItem
from bson.json_util import dumps



################
#### config ####
################

article_blueprint = Blueprint('article', __name__,)


################
#### routes ####
################


@article_blueprint.route('/')
def home():
	page = int(request.args.get('page', 1))
	limit = int(request.args.get('limit', 30))
	docs = NewsItem().get_all(page, limit)
	return jsonify(json.loads(dumps(docs)))


@article_blueprint.route("/search")
def search():
	page = int(request.args.get('page', 1))
	limit = int(request.args.get('limit', 30))
	query = request.args.get('q', '')
	NewsItem().create_indexes()
	docs = NewsItem().search(query, page, limit)
	return jsonify(json.loads(dumps(docs)))
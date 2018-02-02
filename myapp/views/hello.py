from flask import Blueprint
from pymongo import ReturnDocument

from ..app import mongo


hello = Blueprint('hello',__name__)


@hello.route('/')
def index_page():
	record = mongo.db.User.find_one()
	return 'Hello {}{}! Your role is  {}!'.format(record['firstname'],record['lastname'],record['role'])

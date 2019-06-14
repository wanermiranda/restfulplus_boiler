from flask_restplus import fields
from uploader_api.api.restplus import api


pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})


upload_intent = api.model('Upload Intents', {
    'date': fields.String(readOnly=True, description='A string date representation yyyy-mm-dd hh:mm:ss+zzzz'),
    'device': fields.String(required=True, description='Device ID'),
})

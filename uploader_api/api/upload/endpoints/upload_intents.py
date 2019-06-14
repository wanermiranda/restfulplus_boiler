import logging

from flask import request
from flask_restplus import Resource
from uploader_api.api.upload.business import create_upload_intent, delete_upload_intent
from uploader_api.api.upload.serializers import upload_intent
from uploader_api.api.restplus import api
from uploader_api.database.models import UploadIntent

log = logging.getLogger(__name__)

ns = api.namespace('upload/intents', description='Operations related to upload intents')


@ns.route('/')
class UploadIntentCollection(Resource):

    @api.marshal_list_with(upload_intent)
    def get(self):
        """
        Returns a list of upload intents.
        """
        intents = UploadIntent.query.all()
        return intents

    @api.response (201,'Upload Intent successfully created.')
    @api.expect(upload_intent)
    def post(self):
        """
        Creates a new upload intent.
        """
        data = request.json
        create_upload_intent(data)
        return None,201


    @api.response(204, 'UploadIntent successfully deleted.')
    @api.expect(upload_intent)
    def delete(self):
        """
        Deletes upload intent.
        """
        data = request.json

        delete_upload_intent(data)
        return None, 204


# @ns.route('/<int:id>')
# @api.response(404, 'UploadIntent not found.')
# class UploadIntentItem(Resource):

#     @api.marshal_with(upload_intent_with_posts)
#     def get(self, id):
#         """
#         Returns a upload_intent with a list of posts.
#         """
#         return UploadIntent.query.filter(UploadIntent.id == id).one()

#     @api.expect(upload_intent)
#     @api.response(204, 'UploadIntent successfully updated.')
#     def put(self, id):
#         """
#         Updates a upload upload_intent.

#         Use this method to change the name of a upload upload_intent.

#         * Send a JSON object with the new name in the request body.

#         ```
#         {
#           "name": "New UploadIntent Name"
#         }
#         ```

#         * Specify the ID of the upload_intent to modify in the request URL path.
#         """
#         data = request.json
#         update_upload_intent(id, data)
#         return None, 204

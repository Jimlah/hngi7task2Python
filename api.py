from app import resizer
from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
import os
app = Flask(__name__)  # Create a Flask WSGI application
CORS(app)
api = Api(app, doc='/docs')  # Create a Flask-RESTPlus API
ns_conf = api.namespace('', description='Image Resizer operations')

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('image', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument('width', type=int, required=False)
upload_parser.add_argument('height', type=int, required=False)


@ns_conf.route('/image/')  # Create a URL route to this resource
class ImageResizer(Resource):  # Create a RESTful resource
    @ns_conf.expect(upload_parser)
    def post(self):
        """

        :return: Image created
        """

        args = upload_parser.parse_args()
        height, width = None, None
        if args["height"]:
            height = args["height"]
        if args["width"]:
            width = args["width"]
        if "image" in args['image'].mimetype:
            file = request.files["image"]
            filepath = "{}".format(file.filename)
            file.save(filepath)
            result = resizer.image_upload(file=filepath, height=height, width=width)
            result.update({"success": True})
            os.remove(filepath)
            return result
        return {"success": False, "message": "Incorrect file type specified"}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

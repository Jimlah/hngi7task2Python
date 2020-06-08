from flask import Flask
from flask_restx import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from flask_cors import CORS

app = Flask(__name__)  # Create a Flask WSGI application
CORS(app)
api = Api(app, doc='/docs')  # Create a Flask-RESTPlus API
ns_conf = api.namespace('', description='Image Resizer operations')

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('image', location='files',
                           type=FileStorage, required=True)


@ns_conf.route('/image/')  # Create a URL route to this resource
class ImageResizer(Resource):  # Create a RESTful resource
    def get(self):  # Create GET endpoint
        """

        :return: The image queried
        """
        return {'hello': 'world'}

    @ns_conf.expect(upload_parser)
    def post(self):
        """

        :return: Image created
        """

        args = upload_parser.parse_args()
        if "image" in args['image'].mimetype:
            img = args["image"]
            # do_something_here()

            return {"success": True}
        return {"success": False, "message": "Incorrect file type specified"}


if __name__ == '__main__':
    app.run(debug=True)

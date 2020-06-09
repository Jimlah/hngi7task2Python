from flask import Flask, send_file, request
from flask_restx import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from flask_cors import CORS
from function import GetTime
from pathlib import Path
import os


app = Flask(__name__)  # Create a Flask WSGI application
CORS(app)
api = Api(app, doc='/docs')  # Create a Flask-RESTPlus API
ns_conf = api.namespace('', description='Image Resizer operations')
CUR_DIR = Path.cwd()

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('image', location='files',
                           type=FileStorage, required=True)

@ns_conf.route('/download/<filename>',methods=["GET"])
@ns_conf.route('/image/<filename>', methods=["GET"])
@ns_conf.route('/image/')  # Create a URL route to this resource
class ImageResizer(Resource):  # Create a RESTful resource
    def get(self,filename=None):  # Create GET endpoint
        """

        :return: The image queried or return Download link
        """
        if 'download' in request.url:
            for img in Path.iterdir(CUR_DIR/'image/'):
                if filename == img.name:
                    return send_file('image/'+img.name, as_attachment=True)

                return 'Image not found', 404

        if filename in os.listdir('image/'):
            message={
                'Image name': filename,
                'Download link': request.url_root+'download/'+filename,
                'Size': '{:,.0f}'.format(os.path.getsize('image/'+filename)/float(1<<10))+" KB",
                'TimeStamp': GetTime('image/'+filename).imgtime()
                }

            return message
        return "Invalid filename" , 404

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

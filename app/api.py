from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)  # Create a Flask WSGI application
api = Api(app, doc='/docs')  # Create a Flask-RESTPlus API
ns_conf = api.namespace('', description='Image Resizer operations')


@ns_conf.route('/image/')  # Create a URL route to this resource
class ImageResizer(Resource):  # Create a RESTful resource
    def get(self):  # Create GET endpoint
        """

        :return: The image queried
        """
        return {'hello': 'world'}

    def post(self):
        """

        :return: Image created
        """


if __name__ == '__main__':
    app.run(debug=True)

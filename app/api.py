from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        """
        Get each image using id
        :return: Resized image link, image name, size and other metadata
        """
        return {'hello': 'world'}

    def post(self):
        """
        POST request to the API
        :return: Resized image link, image name, size and other metadata
        """
        pass

    def list(self):
        """
        List all images
        :return: All images, with their name and size
        """
        pass


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

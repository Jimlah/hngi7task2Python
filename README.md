### [Team Flash] Flask Micro-service in resizing images

**A flask-powered API for resizing images**



### Setting up

#### Pythonic way

- Clone this repository
- Create a python3 virtual environment(This is not compulsory)
- Run the following command
~~~
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app/api.py
~~~

- Navigate to http://127.0.0.1:5000/docs
- Upload an image file, select width and height and execute

#### Docker

- Install docker from here https://docs.docker.com/get-docker/
- Install Docker Compose from here https://docs.docker.com/compose/install/

- Make sure you are in root folder of this repo

- run docker-compose up

Visit http:///0.0.0.0:5000/docs/



##### Response

- **url**: A link to your resized image
- **filename**: Your uploaded file name
- **height**: New image height
- **width**: New image width
- **created_at**: Timestamp
- **success**: A boolean





#### Contributing

**Help us, don't cause merge conflicts**

1. ~~~
   git checkout dev
   ~~~
   
   ~~~ 
   python3 -m venv env
   
   source /env/bin/activate
   ~~~
   
   (You only need to run this once)
   
   ~~~
   pip install -r requirements.txt
   python app/api.py
   ~~~
   
   Visit http:///0.0.0.0:5000/docs/
   




#### Notes

##### Contributing

- Fork this repo
- Checkout develop branch
- Update the codes
- Push and raise a Pull request which will be attended to by managers

You will work in the app/api.py file, the resizer.py where all the functions(Or class) will be

##### For the Script guys

Make sure resizer.py is working perfectly. If it's not, it will not be pushed.

#### Todo

- A more precise readme.md
- Set up boilerplate
- Tests

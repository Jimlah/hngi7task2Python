import cloudinary
from cloudinary import uploader
from cloudinary import CloudinaryImage

cloudinary.config(
  cloud_name = 'hngi7-python',  
  api_key = '847136641947533',  
  api_secret = '3VQy3iuna0qAct-ShP7yfAwJfzc'  
)


def image_upload(file, **options):
    cloudinary.uploader.upload(file, public_id= file[:-4])
    resize(file, width=100, height= 150)

    
# this function retrives the uploaded image and and edits it returns a url to the uploaded image
def resize(file, width, height):
    result = cloudinary.utils.cloudinary_url(file,
                                width = width,
                                height = height,
                                )
    print(result)
    
#test
#image_upload("test_3.jpg")

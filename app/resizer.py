import cloudinary
from cloudinary import uploader

cloudinary.config(
    cloud_name='hngi7-python',
    api_key='847136641947533',
    api_secret='3VQy3iuna0qAct-ShP7yfAwJfzc'
)


def image_upload(file, **options):
    res = uploader.upload(file, public_id=file.split(".")[0])
    if options['width']:
        width = options['width']
    else:
        width = 150
    if options['height']:
        height = options['height']
    else:
        height = 150
    return resize(file, width=width, height=height, res=res)


# this function retrives the uploaded image and and edits it returns a url to the uploaded image
def resize(file, width, height, res):
    result = cloudinary.utils.cloudinary_url(file.split(".")[0],
                                             width=width,
                                             height=height,
                                             )
    resp = {"url": result[0], 'filename': res['original_filename'], "height": height, "width": width,
            'created_at': res['created_at']}

    return resp

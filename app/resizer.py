
import os
import sys

import cloudinary
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

os.chdir(os.path.join(os.path.dirname(sys.argv[0]),'.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())
cloudinary.config(
    cloud_name ='dvm5tspox',
    api_key ='473677673649429',
    api_secret ='bZuAtRIBgJc1DuIVBO_bVdLSE1c'
)
DEFAULT_TAG = 'python_sample_resizer'
def dump_response(response):
    print('Upload response:')
    for key in sorted(response.keys()):
        print(' %s: %s' % (key,response[key]))

def upload_files():
    print('---Upload a local file')
    response= upload('https://res.cloudinary.com/dvm5tspox/image/upload/v1591648726/samples/landscapes/girl-urban-view.jpg', tags= DEFAULT_TAG)
    dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format = response['format'],
        width=200,
        height =150,
        crop ='fill'
    )
    print('Fill 200 x 150 url:'+ url)
    print("")

    print("---Upload a local file with custom public ID")
    response = upload("https://res.cloudinary.com/dvm5tspox/image/upload/v1591648726/samples/landscapes/girl-urban-view.jpg",
    tags =DEFAULT_TAG,public_id ='custom_name')

    dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format = response['format'],
        width=200,
        height =150,
        crop ='fit' )
    print('Fit 200 x 150 url: '+ url)
    print("")



    print('---Upload a local file with maximum radius')
    response= upload('C:\\Users\\USER\\hngi7task2Python\\app\\.vscode\\DSC_1344 copy.jpg', tags= DEFAULT_TAG,
    public_id='radius_custom_name',)
    
    dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format = response['format'],
        width=300,
        height =300,
        crop ='fill',
        radius ='max'
    )
    print('Fill 300 x 300 url:'+ url)
    print("")

    print("---Upload a local file with custom public ID")
    response = upload("C:\\Users\\USER\\hngi7task2Python\\app\\.vscode\\DSC_1344 copy.jpg",
    tags =DEFAULT_TAG,public_id ='custom_name')

def cleanup():
    response = resources_by_tag(DEFAULT_TAG)
    resources= response.get('resources', [])
    if not resources:
        print('No image found')
        return
    print('Deleting {0:d} images...'.format(len(resources)))
    delete_resources_by_tag(DEFAULT_TAG)
    print('Done!')

if len(sys.argv) >1:
    if sys.argv[1] == 'upload':
        upload_files()  
    if sys.argv[1] == 'cleanup':
        cleanup()
else:
    print('---Uploading files and then cleaning up')
    print('')
    upload_files()





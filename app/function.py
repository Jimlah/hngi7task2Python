from pathlib import Path
import exifread
import os

class GetTime:
    def __init__(self, filename):
        self.filename = filename

    def imgtime(self):
        #self.name = imname
        if self.filename.endswith(("png","jpeg","jpg")):
            with open(self.filename, 'rb') as image:
                try:
                    exif = exifread.process_file(image)
                    date_time = str(exif['EXIF DateTimeOriginal'])
                    return date_time
                except KeyError:
                    return None
        #return "Use a png or jpeg file"


import os
from typing import Sequence
from urllib import response

from google.cloud import vision
from requests import Response
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Haeju/OneDrive/Documents/bowling_project/concise-clock-416019-89f5e8c52164.json'

# Instantiate the client
client = vision.ImageAnnotatorClient()

image_file_path = 'score2.jpg'
image = prepare_image_local(image_file_path)
va = VisionAI(client, image)

import sys

texts = va.text_detection()
for index, text in enumerate(texts):
    print(text.description)
    draw_boundary(image_file_path, text.bounding_poly, text.description)
    if index > 3:
        sys.exit()


# Check for any errors in the response
if Response.error.message:
    raise Exception(f'{response.error.message}')
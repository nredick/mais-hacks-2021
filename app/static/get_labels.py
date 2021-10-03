#!/usr/bin/env python3

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

def get_labels(url):  # func to get labels and confidences from an image 

    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = url

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    if response.error.message:
        return 'Error: Image not found.'
    else:
        try:  # get best three 
            return [{label.description : label.score} for label in labels][:3]
        except:  # or return all if there are less than 3 labels
            return [{label.description : label.score} for label in labels]

## for testing ## 
#print(get_labels('https://www.vets4pets.com/siteassets/species/dog/two-dogs-running-with-balls.jpg?w=585&scale=down'))


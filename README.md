# MAIS Hacks 2021 
boop

Our project aims to generate poems based on images!

This project was built for [MAIS Hacks 2021](https://maishacks.com/), a 24 HR virtual AI hackathon. Our goal was to build a model that can generate poems based on input. 

Project made with love by [Nathalie](https://github.com/nredick), [Elinor](https://github.com/elinorpd), [Alex](https://github.com/allu5662), and [Zahur](https://github.com/croissantfriend).

## Project Description

The dataset used to train the model was the [Poems Dataset (NLP)](https://www.kaggle.com/michaelarman/poemsdataset). The app works by using the Google Vision API to label images, and those label are used to generate a poem. The webapp was built using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Bootstrap](https://getbootstrap.com/), and is hosted on an AWS EC2 t2.micro instance.

## Repository Organization

- data/
  - 20k+ text files, sourced from the [Poems Dataset (NLP)](https://www.kaggle.com/michaelarman/poemsdataset).

- src/
  - Python source code for the Google Vision API. 

- model/
  - Contains Python files for the Twitter API, preprocessing data, and the script to build the model.

- ./ 
  - A requirements.txt file and .gitignore. 

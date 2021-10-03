# MAIS Hacks 2021 - Winner of the Best Hack for Art

Our project aims to generate poems based on images!

This project was built for [MAIS Hacks 2021](https://maishacks.com/), a 24 HR virtual AI hackathon. Our goal was to build a model that can generate poems based on input. 

Project made with love by [Nathalie](https://github.com/nredick), [Elinor](https://github.com/elinorpd), [Alex](https://github.com/allu5662), and [Zahur](https://github.com/croissantfriend).

## Project Description

The dataset used to train the model was the [Poems Dataset (NLP)](https://www.kaggle.com/michaelarman/poemsdataset). The app works by using the Google Vision API to label images, and those labels are used to generate a poem. The poetry generator was built using a tensorflow LSTM. The webapp was built using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Bootstrap](https://getbootstrap.com/).

## Repository Organization

- app/
  - Contains Flask python files, HTML, and CSS files to create the web app. Also contains Python source code for the Google Vision API.

- data/
  - A subset of the 20k+ poems used to train the data, sourced from the [Poems Dataset (NLP)](https://www.kaggle.com/michaelarman/poemsdataset). Only files used to generate the final model training data are present in the repository.

- src/
  - Python notebook for the training of the model to generate poetry.  

- model/
  - Contains Python files for the Twitter API, preprocessing data, and the script to build the model. Also includes pickled model and tokenizer for the poetry generator.

- ./ 
  - A requirements.txt file and .gitignore. 

### A screenshot of our webapp generated poem with [this image](https://webstockreview.net/images/cheese-clipart-yellow-cheese-21.jpg) submitted

![Demo of our web app displaying a poem about Gruyere cheese.](https://github.com/nredick/mais-hacks-2021/blob/main/sample_images/Gruyere_poem.png)

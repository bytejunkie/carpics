#!/usr/bin/env python3
import os
import random

from flask import Flask, render_template, request

app = Flask(__name__)
cars = dict()

cars["bmw"] = [
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/bmw/bmw_01.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/bmw/bmw_02.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/bmw/bmw_03.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/bmw/bmw_04.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/bmw/bmw_05.jpg"
]

cars["audi"] = [
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/audi/audi_01.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/audi/audi_02.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/audi/audi_03.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/audi/audi_04.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/audi/audi_05.jpg"
]

cars["vw"] = [
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/vw/vw_01.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/vw/vw_02.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/vw/vw_03.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/vw/vw_04.jpg",
    "https://cars-docker-images.s3.eu-west-2.amazonaws.com/vw/vw_05.jpg"
]

all_cars = cars["bmw"] + cars["audi"] + cars["vw"]


@app.route("/")
def index():
    """runs the car pics in a container"""
    
    manu = request.args.get('manufacturer')
    if manu:
        url = random.choice(cars[manu])
    else:
        url = random.choice(all_cars)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

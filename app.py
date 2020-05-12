from flask import Flask, render_template, request
import os
import random

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

@app.route("/")
def index():
    manu = request.args.get('manufacturer')
    url = random.choice(cars[manu])
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
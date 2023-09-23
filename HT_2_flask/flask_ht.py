import csv

import requests
from faker import Faker
from flask import Flask, render_template, request

app = Flask(__name__)
fake = Faker("ru-RU")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/requirements")
def requirements():
    with open("requirements.txt", "r") as file:
        lines = file.readlines()
    req_text = "\n".join(line.rstrip() for line in lines)
    return render_template("requirements.html", req_text=req_text)


@app.route("/users/generate")
def users_generate():
    count = request.args.get('count', type=int, default=100)
    if count > 0:
        count = min(count, 500)  # защита от перегрузки сервера
        users = [(i + 1, fake.first_name(), fake.email()) for i in range(count)]
        return render_template('users_generate.html', users=users)
    else:
        return "Query параметр должен быть положительным числом"


@app.route("/mean")
def mean():
    try:
        with open("hw.csv", "r") as file:
            file_csv = csv.reader(file)
            count = 0
            height_cm = 0
            weight_kg = 0
            for index, item in enumerate(file_csv):
                if index != 0 and item:
                    count += 1
                    height_cm += float(item[1])
                    weight_kg += float(item[2])

                else:
                    continue

            average_height = round(height_cm * 2.54 / count, 2)
            average_weight = round(weight_kg / 2.205 / count, 2)
        return render_template('mean.html', average_height=average_height, average_weight=average_weight)
    except FileNotFoundError:
        return "Файл, не найден"


@app.route("/space")
def space():
    r = requests.get("http://api.open-notify.org/astros.json")
    number_of_astronauts = len(r.json()["people"])
    return render_template("space.html", number_of_astronauts=number_of_astronauts)


if __name__ == "__main__":
    app.run()

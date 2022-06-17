from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/consultations/exercise/')
def exercise():
    return render_template('consultations/exercise.html')

@app.route('/consultations/general_info/')
def general_info():
    return render_template('consultations/general_info.html')

@app.route('/consultations/self_check/')
def self_check():
    return render_template('consultations/self_check.html')

@app.route('/consultations/food/')
def food():
    return render_template('consultations/food.html')

@app.route('/consultations/fasting/')
def fasting():
    return render_template('consultations/fasting.html')

@app.route('/consultations/sleep/')
def sleep():
    return render_template('consultations/sleep.html')

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    # print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)



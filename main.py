from flask import Flask, render_template
import random
import datetime
import requests
from flask_wtf import FlaskForm
from wtforms import RadioField


class SkinCareForm(FlaskForm):
    certification = RadioField('certification', choices=[('Acne', 'Acne'), ('Redness', 'Redness'),
                                                         ('Hyper pigmented', 'Hyper pigmented'), ('Dry', 'Dry'),
                                                         ('Wrinkled','Wrinkled')])

class BackPainForm(FlaskForm):
    radio1 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio2 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio3 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio4 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio5 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])


app = Flask(__name__)
app.secret_key = "#2247tryryWWWT23ff"


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

@app.route('/consultations/skin_care/', methods=["GET", "POST"])
def skin_care():
    skin_care_form = SkinCareForm()

    name_of_consult = "Skin Care"
    prescription = skin_care_form.certification.data
    if prescription == None:
        messages_r = None
        return render_template('consultations/skin_care.html', form=skin_care_form, message=messages_r)

    else:
        messages_r = prescription + ' self-management protocol has been sent to your email.'
        tags_message = "success"

        return render_template('consultations/skin_care.html', form=skin_care_form, message=messages_r, tag=tags_message)

@app.route('/consultations/back_pain/', methods=["GET", "POST"])
def back_pain():
    back_form = BackPainForm()
    name_of_consult = "Back & Neck Pain"
    if back_form.radio1.data == "Yes" or back_form.radio2.data == "Yes" or back_form.radio3.data == "Yes" or \
            back_form.radio4.data == "Yes" or back_form.radio5.data == "Yes":
        prescription = "Urgently see your doctor"
        tags_message = "warning"
        return render_template('consultations/back_pain.html', form=back_form, message=prescription, tag=tags_message)

    elif back_form.radio1.data == "No" and back_form.radio2.data == "No" and back_form.radio3.data == "No" and \
            back_form.radio4.data == "No" and back_form.radio5.data == "No":
        prescription = "Home Lower Back Rehabilitation Programme For 6 Weeks. has been sent to your email"
        tags_message = "success"
        return render_template('consultations/back_pain.html', form=back_form, message=prescription, tag=tags_message)

    else:
        messages_r = None
        return render_template('consultations/back_pain.html', form=back_form, message=messages_r)




if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager


class SkinCareForm(FlaskForm):
    certification = RadioField('certification', choices=[('Acne', 'Acne'), ('Redness', 'Redness'),
                                                         ('Hyper pigmented', 'Hyper pigmented'), ('Dry', 'Dry'),
                                                         ('Wrinkled','Wrinkled')])


class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    phone_number = StringField('Phone')
    password = StringField('Password')
    confirm_password = StringField('Confirm Password')


class BackPainForm(FlaskForm):
    radio1 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio2 = RadioField('radio2', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio3 = RadioField('radio3', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio4 = RadioField('radio4', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio5 = RadioField('radio5', choices=[('Yes', 'Yes'), ('No', 'No')])


class FemaleUrinary(FlaskForm):
    radio6 = RadioField('radio6', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio7 = RadioField('radio7', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio8 = RadioField('radio8', choices=[('Yes', 'Yes'), ('No', 'No')])


class FemaleUrinary2(FlaskForm):
    radio1 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio2 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio3 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio4 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio5 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])


class MaleUrinaryForm(FlaskForm):
    radio1 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])
    radio2 = RadioField('radio1', choices=[('Yes', 'Yes'), ('No', 'No')])


app = Flask(__name__)
app.secret_key = "#2247tryryWWWT23ff"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# # CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/consultations/exercise/')
def exercise():
    return render_template('consultations/exercise.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/general_info/')
def general_info():
    return render_template('consultations/general_info.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/self_check/')
def self_check():
    return render_template('consultations/self_check.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/food/')
def food():
    return render_template('consultations/food.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/fasting/')
def fasting():
    return render_template('consultations/fasting.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/sleep/')
def sleep():
    return render_template('consultations/sleep.html', logged_in=current_user.is_authenticated)


@app.route('/consultations/skin_care/', methods=["GET", "POST"])
@login_required
def skin_care():
    skin_care_form = SkinCareForm()

    name_of_consult = "Skin Care"
    prescription = skin_care_form.certification.data
    if prescription == None:
        messages_r = None
        return render_template('consultations/skin_care.html', form=skin_care_form, message=messages_r, logged_in=True)

    else:
        messages_r = prescription + ' self-management protocol has been sent to your email.'
        tags_message = "success"

        return render_template('consultations/skin_care.html', form=skin_care_form, message=messages_r, tag=tags_message
                               , logged_in=True)


@app.route('/consultations/back_pain/', methods=["GET", "POST"])
@login_required
def back_pain():
    back_form = BackPainForm()
    name_of_consult = "Back & Neck Pain"
    if back_form.radio1.data == "Yes" or back_form.radio2.data == "Yes" or back_form.radio3.data == "Yes" or \
            back_form.radio4.data == "Yes" or back_form.radio5.data == "Yes":
        prescription = "Urgently see your doctor"
        tags_message = "warning"
        return render_template('consultations/back_pain.html', form=back_form, message=prescription, tag=tags_message, logged_in=True)

    elif back_form.radio1.data == "No" and back_form.radio2.data == "No" and back_form.radio3.data == "No" and \
            back_form.radio4.data == "No" and back_form.radio5.data == "No":
        prescription = "Home Lower Back Rehabilitation Programme For 6 Weeks. has been sent to your email"
        tags_message = "success"
        return render_template('consultations/back_pain.html', form=back_form, message=prescription, tag=tags_message, logged_in=True)

    else:
        messages_r = None
        return render_template('consultations/back_pain.html', form=back_form, message=messages_r, logged_in=True)


@app.route('/consultations/female_urinary/', methods=["GET", "POST"])
@login_required
def female_urinary():
    female_urinary_form = FemaleUrinary()
    name_of_consult = "Female Urinary"
    if female_urinary_form.radio6.data == "Yes" or female_urinary_form.radio7.data == "Yes" or female_urinary_form.radio8.data == "Yes":
        prescription = "Urgently see your doctor"
        tags_message = "warning"
        return render_template('consultations/female_urinary.html', form=female_urinary_form, message=prescription, tag=tags_message, logged_in=True)

    elif female_urinary_form.radio6.data == "No" and female_urinary_form.radio7.data == "No" and female_urinary_form.radio8.data == "No":
        return redirect(url_for('female_urinary2'))

    else:
        messages_r = None
        return render_template('consultations/female_urinary.html', form=female_urinary_form, message=messages_r, logged_in=True)


@app.route('/consultations/female_urinary2/', methods=["GET", "POST"])
@login_required
def female_urinary2():
    female_urinary_form2 = FemaleUrinary2()
    name_of_consult = "Female Urinary"
    if female_urinary_form2.radio3.data == "yes":
        prescription = "combine the pelvic floor muscle training program & the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
        tags_message = "success"
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=prescription,
                               tag=tags_message, logged_in=True)

    elif female_urinary_form2.radio1.data == "yes" and female_urinary_form2.radio2.data == "yes":
        prescription = "combine the pelvic floor muscle training program & the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
        tags_message = "success"
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=prescription,
                               tag=tags_message, logged_in=True)

    elif female_urinary_form2.radio1.data == "yes" and female_urinary_form2.radio2.data == "no":
        prescription = "Do the pelvic floor muscle training program for 12 weeks. If no improvement consult a urogynaecologist."
        tags_message = "success"
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=prescription,
                               tag=tags_message, logged_in=True)
    elif female_urinary_form2.radio2.data == "yes" and female_urinary_form2.radio1.data == "no":
        prescription = "Do the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
        tags_message = "success"
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=prescription,
                               tag=tags_message, logged_in=True)
    elif female_urinary_form2.radio4.data == "yes":
        prescription = "Do the pelvic floor muscle training program for 12 weeks. If no improvement consult a urogynaecologist."
        tags_message = "success"
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=prescription,
                               tag=tags_message, logged_in=True)
    else:
        messages_r = None
        return render_template('consultations/female_urinary2.html', form=female_urinary_form2, message=messages_r,
                               logged_in=True)


@app.route('/consultations/male_urinary/', methods=["GET", "POST"])
@login_required
def male_urinary():
    male_urinary_form = MaleUrinaryForm()
    name_of_consult = "Back & Neck Pain"
    if male_urinary_form.radio1.data == "Yes" or male_urinary_form.radio2.data == "Yes":
        prescription = "Urgently see your doctor"
        tags_message = "warning"
        return render_template('consultations/male_urinary.html', form=male_urinary_form, message=prescription,
                               tag=tags_message, logged_in=True)

    elif male_urinary_form.radio1.data == "No" and male_urinary_form.radio2.data == "No":
        prescription = "trial of erectile rehabilitation home pack for 6 weeks to 3 months"
        tags_message = "success"
        return render_template('consultations/male_urinary.html', form=male_urinary_form, message=prescription, tag=tags_message, logged_in=True)

    else:
        messages_r = None
        return render_template('consultations/male_urinary.html', form=male_urinary_form, message=messages_r, logged_in=True)


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.password.data == register_form.confirm_password.data:
            pass_w = register_form.password.data
            pass_hash = generate_password_hash(pass_w, method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email=register_form.email.data,
                name=register_form.first_name.data,
                last_name=register_form.last_name.data,
                password=pass_hash,
            )

            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                flash('User already exists, Please try with another email!')
                return redirect(url_for('register'))

            # Log in and authenticate user after adding details to database.
            login_user(new_user)

            return redirect(url_for("home", name=new_user.name))

        else:
            flash("Passwords don't match!")
            return redirect(url_for("login",))

    return render_template("accounts/register.html", form=register_form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # Email exists and password correct
        else:
            login_user(user)

            return redirect_dest(fallback=url_for('home', name=user.name))
        print(dest_url)
        print(fallback)
            # return redirect(url_for('home', name=user.name))

    return render_template("accounts/login.html", logged_in=current_user.is_authenticated)


@app.route('/consultations/diabetes/')
@login_required
def diabetes():
    return render_template('consultations/diabetes.html', logged_in=True)

@app.route('/consultations/hypertension/')
@login_required
def hypertension():
    return render_template('consultations/hypertension.html', logged_in=True)


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    print(current_user.name)
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.login_manager.unauthorized_handler
def unauth_handler():
    return render_template("accounts/login.html", next=request.endpoint)


def redirect_dest(fallback):
    if request.args.get('next') == 'login':
        dest = 'home'
    else:
        dest = request.args.get('next')
    try:
        dest_url = url_for(dest)
    except:
        return redirect(fallback)
    return redirect(dest_url)

if __name__ == "__main__":
    app.run(debug=True)



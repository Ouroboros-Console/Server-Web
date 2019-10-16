from flask import render_template, request, url_for, redirect, flash
from server import app, db, bcrypt
from server.models import User
from server.forms import RegistrationForm


@app.route("/", methods=["GET", "POST"])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        try:
            user = User(
                email=form.email.data, password=hashed_pw, address=form.address.data
            )

            db.session.add(user)
            db.session.commit()

            flash("Your account has been successfully registered", category="success")

        except:
            flash("Some error occured", category="danger")

        finally:
            return redirect(url_for("home"))

    return render_template("index.html", footer_bg="white", form=form)


@app.route("/course")
def course():
    return render_template("course-single.html", footer_bg="light")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         return "Congratulations...You have been registered !"

#     return render_template("index.html", footer_bg="white", form=form)


if __name__ == "__main__":
    app.run(debug=True)

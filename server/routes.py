import random
import string
import flask
from server import app, db, bcrypt, models
from server.forms import RegistrationForm


@app.route("/", methods=["GET", "POST"])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        salt_pw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64)) + \
               form.password.data
        salt_api_key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64)) + \
               form.password.data
        form.password.data += salt_pw
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user_id = models.User.query.limit(1).all()
        user_id[0] += 1
        api_key = user_id[0] + salt_pw + salt_api_key

        try:
            user = models.User(
                email=form.email.data, password=hashed_pw, address=form.address.data,
                api_key=api_key, salt_pw=salt_pw
            )

            db.session.add(user)
            db.session.commit()

            return flask.redirect(flask.url_for("test"))
        except:
            flask.flash("Some error occured", category="danger")
            return flask.redirect(flask.url_for("/"))

    return flask.render_template("index.html", footer_bg="white", form=form)


@app.route("/course")
def course():
    return flask.render_template("course-single.html", footer_bg="light")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         return "Congratulations...You have been registered !"

#     return render_template("index.html", footer_bg="white", form=form)

@app.route("/fetch/<api_key>")
def fetch_video(api_key):
    message = models.AES256.decrypt(api_key)
    flask.Response(models.User.query.filter_by(api_key=message).first())

# For any debugging purpose
@app.route("/test")
def test():
    return flask.Response("done")


if __name__ == "__main__":
    app.run(debug=True)

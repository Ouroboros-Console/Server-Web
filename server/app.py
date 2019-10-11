from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', footer_bg='white')


@app.route("/course")
def course():
    return render_template('course-single.html', footer_bg='light')


if __name__ == "__main__":
    app.run(debug=True)

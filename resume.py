from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/')
def home_page():
    return render_template('home.html')


@app.route('/courses/')
def course_page():
    courses = [
            'MISY350',
            'MISY330',
            'MISY427'
            ]
    return render_template('courses.html', courses=courses)


@app.route('/about/')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

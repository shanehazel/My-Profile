from flask import Flask, render_template, request
from areaCircle import area_circle
from areaTriangle import area_triangle

app = Flask(__name__, static_url_path = '', static_folder = 'C:\Flask_Intro\My-Profile\static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/areaOfcircle')
def circle():
    return render_template('areaOfcircle.html')

@app.route('/areaOfTriangle')
def triangle():
    return render_template('areaOfTriangle.html')

@app.route('/program')
def program():
    return render_template('program.html')

@app.route('/motto')
def motto():
    return render_template('motto.html')

@app.route('/section')
def section():
    return render_template('section.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/calculate_circle', methods=['GET', 'POST'])
def areaCircle():
    area = None
    if request.method == 'POST':
        input_radius = request.form.get('radius', '')
        try:
            input_radius = int(input_radius)
            area = area_circle(input_radius)
        except ValueError as s:
            area = str(s)
    return render_template('areaOfcircle.html', area=area)

@app.route('/calculate_triangle', methods=['GET', 'POST'])
def areaTriangle():
    try:
        input_base = float(request.form.get('base', ''))
        input_height = float(request.form.get('height', ''))
        area = area_triangle(input_base, input_height)
    except ValueError as s:
        area = str(s)
    return render_template('areaOfTriangle.html', area=area)


@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
        result = None
        if request.method == 'POST':
            input_string = request.form['inputString']
            result = input_string.upper()
            return render_template('touppercase.html', result=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)

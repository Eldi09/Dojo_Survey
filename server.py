from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="My Secret key!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    return render_template('result.html', info = session)

@app.route('/process', methods=['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')



if __name__ == "__main__":
    app.run(debug=True)
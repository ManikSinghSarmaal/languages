from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return " Welcome to Manik's flask development "

@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html', result=score)

@app.route('/fail/<int:score>')
def fail(score):
    return f'the student has passed with score of {score}'


@app.route('/marks/<int:score>')
def topa(score):
    result =''
    if score<33:
        result = 'fail'
    else :
        result = 'success'
    return redirect(url_for(result, score= score))

if __name__=='__main__':
    app.run(debug= True)
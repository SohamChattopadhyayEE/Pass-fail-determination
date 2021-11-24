from flask import Flask, redirect, url_for, render_template, request
import argparse

parser = argparse.ArgumentParser(description="Form for pass-fail determination")
parser.add_argument('-p','--passing_marks',type=int,default=50,
                    help="The marks determining pass or fail")
args = parser.parse_args()
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/show_result/<int:score>')
def show_result(score):
    res = ""
    if score>=args.passing_marks:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res,average_score=score)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    
    return redirect(url_for("show_result", score=total_score))


if __name__ ==  '__main__':
    app.run(debug=True)
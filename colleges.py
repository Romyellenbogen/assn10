from flask import Flask, render_template
from modules import convert_to_dict
app = Flask(__name__)

application = app

collegeList = convert_to_dict("public3.csv")

@app.route('/')
def index():
    ids = []
    names = []
    for college in collegeList:
        ids.append(college['Id'])
        names.append(college['Name'])
    pairs_list = zip(ids, names)
    return render_template('index.html', pairs=pairs_list, the_title="Colleges")

@app.route('/college/<num>')
def detail(num):
    for college in collegeList:
        if college['Id'] == num:
            collegeDict = college
            break
    return render_template('college.html', c=collegeDict, the_title=collegeDict['Name'])


if __name__ == '__main__':
    app.run(debug=True)

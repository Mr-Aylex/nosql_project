from flask import Flask, jsonify ,render_template
from pymongo import MongoClient
import json

from flask import jsonify
#https://pymongo.readthedocs.io/en/stable/tutorial.html
#https://matplotlib.org/

app = Flask(__name__)


@app.route('/')
# this function return data in a plot format
def main():  # put application's code here
    #create a list of data to pass to the template
    data = [
        {'name': 'Alice', 'age': '25'},
        {'name': 'Bob', 'age': '27'},
        {'name': 'Charlie', 'age': '29'},
    ]
    # render the template with the data
    return render_template('index.html', data=data)

@app.route('/test')
def test():
    f = open('./owid-covid-data.json','r')
    datas = json.load(f)
    # for data in datas:
    #     print(data)

    return render_template('test.html', data=[datas])



@app.route('/api',methods=['GET','PUT'])
def api():

    f = open('./owid-covid-data.json','r')
    datas = json.load(f)

    return_data = dict()
    i = 0;
    for data in datas:
        return_data[i] = data
        i = i+1

    return jsonify(return_data)


@app.route('/test2',methods=['GET','PUT'])
def test2():
    return render_template('test2.html')


@app.route('/jsondata',methods=['GET','PUT'])
def jsondata():
    return render_template('testdata.geojson')



# FLASK_ENV="development"
if __name__ == '__main__':
    app.run(debug=True)

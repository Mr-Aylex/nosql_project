from flask import Flask, render_template
from pymongo import MongoClient
import json

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



if __name__ == '__main__':
    app.run()
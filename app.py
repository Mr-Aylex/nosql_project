from flask import Flask, render_template
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
import json
from pymongo import MongoClient
import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
import base64
from io import BytesIO
from matplotlib.figure import Figure

# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://matplotlib.org/
app = Flask(__name__)


@app.route('/')
# this function return data in a plot format
def main():  # put application's code here
    # create a list of data to pass to the template
    generate_map()
    # render the template with the data
    return render_template('index.html')


@app.route('/map')
def get_img():
    buf = BytesIO()
    m = Basemap(projection='ortho', lon_0=4, lat_0=34, resolution='l')
    # m.drawcoastlines()
    # m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    # m.drawparallels(np.arange(-90., 120., 30.))
    # m.drawmeridians(np.arange(0., 420., 60.))
    m.drawmapboundary(fill_color='aqua')
    # m.etopo()
    m.bluemarble()
    plt.title("Full Disk Orthographic Projection")
    plt.savefig(buf, format='jpg', dpi=900)
    plt.savefig(fname='static/img/map.jpg', dpi=500)
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


def generate_map():
    print("Generating map")
    buf = BytesIO()
    map = Basemap(
        projection='ortho',
        lat_0=30, lon_0=50
    )
    map.shadedrelief()
    map.drawcoastlines()
    map.drawcountries()

    map.drawlsmask(
        land_color="#ddaa66",
        ocean_color="#7777ff",
        resolution='l'
    )
    plt.savefig(fname='static/img/map.jpg', dpi=300)


if __name__ == '__main__':
    data = pd.read_csv("annual-number-of-deaths-by-cause.csv", sep=";", index_col=['Year', 'Entity'])
    # get all lignes with Yemen in the Entity column
    # add a column with longitude and latitude
    dict = {}
    for index, row in data.iterrows():
        if not index[0] in dict:
            dict[index[0]] = {}
            dict[index[0]][index[1]] = row

        else:
            dict[index[0]][index[1]] = row


    df = pd.DataFrame.from_dict(dict)
    df.to_json('annual-number-of-deaths-by-country-and-year.json')
    # print(dict[2007][0])
    # js = json.loads()
    # print(json.dumps(dict, indent=4))
    # data = pd.DataFrame.from_dict(dict)
    # liste_of_country = data['Entity'].drop_duplicates()


    # print(liste_of_country)
    # liste_of_country.to_csv('liste_of_country.csv')
    # data_group_country = data[data['Entity'] == 'France']

    # print(data_group_country)

    # img = img.imread("monde_carte_avec_pays.jpg")
    # plt.imshow(img)

    # plt.show()
    # app.run()

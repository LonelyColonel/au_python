import logging
import geopandas
import pandas
import matplotlib.pyplot as plt
from shapely.geometry import Point
from requests import get
import geodatasets


logging.basicConfig(level=logging.INFO, filename='logs_file.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')


def request_info_func():
    request = get('https://data.nasa.gov/resource/y77d-th95.json').json()
    meteor_names = []
    coords_list_latitude = []
    coords_list_longitude = []
    coords = []
    for i in range(len(request)):
        try:
            res = request[i]['geolocation']['coordinates']
            coords_list_latitude.append(res[0])
            coords_list_longitude.append(res[1])
            meteor_names.append(request[i]['name'])
            coords.append(res)
        except KeyError:
            logging.info(f'The coordinates of the {request[i]["name"]} meteorite are not specified :-(')

    res_list = list(zip(meteor_names, coords_list_latitude, coords_list_longitude, coords))
    collownames = ['names', 'latitude', 'longitude', 'coords']
    dataframe = pandas.DataFrame(res_list, columns=collownames)
    dataframe['coords'] = dataframe['coords'].apply(Point)
    return dataframe


def main_func():
    fig, ax = plt.subplots(figsize=(20, 16))
    world = geopandas.read_file(geodatasets.get_path("naturalearth.land"))
    plt.title("Meteorite landings")
    geo_meteor = geopandas.GeoDataFrame(request_info_func(), geometry='coords')
    main_map = world.plot(ax=ax, alpha=0.4, color="green")
    geo_meteor.plot(ax=main_map, color='red', marker="o", markersize=10)
    ax.axis('off')
    plt.show()


if __name__ == '__main__':
    main_func()

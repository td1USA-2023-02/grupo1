import h3
from shapely.geometry import Polygon, Point
from shapely import wkt
import shapely.wkt
import googlemaps
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


def output_h3_id_attributes(h3_id):
    return {
        "co_ordinates" : h3.h3_to_geo(h3_id), 
        "geo_boundary" : Polygon(h3.h3_to_geo_boundary(h3_id, geo_json=True)).wkt, 
        "parent" : h3.h3_to_parent(h3_id), 
        "children" : h3.h3_to_children(h3_id)
    }

output_h3_id_attributes('8843acd819fffff')
print(output_h3_id_attributes('8843acd819fffff'))

polygon_string = "POLYGON ((55.13977696520102 25.09805053895709, 55.14002932545401 25.09743871100549, 55.1407574981263 25.0972787358399, 55.14123332293791 25.09773058763684, 55.14098097073993 25.09834242241949, 55.14025278567518 25.09850239857415, 55.13977696520102 25.09805053895709))"

shapely_polygon_fig = wkt.loads(polygon_string)
print(shapely_polygon_fig)

fig, ax = plt.subplots()
ax.plot(*shapely_polygon_fig.exterior.xy)
ax.set_aspect('equal', adjustable='datalim')
plt.show()

print(shapely_polygon_fig.wkt)

print("Base de datos")

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              55.07652282714844,
              25.11731056144692
            ],
            [
              55.15205383300781,
              25.055745117015316
            ],
            [
              55.223464965820305,
              25.112958466940725
            ],
            [
              55.15068054199219,
              25.18070920440447
            ],
            [
              55.07652282714844,
              25.11731056144692
            ]
          ]
        ]
      }
    }
  ]
}



print("Codigo ejecutado")
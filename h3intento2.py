import h3
from shapely.geometry import Polygon, Point
import shapely.wkt
def output_h3_id_attributes(h3_id):
    return {
        "co_ordinates" : h3.h3_to_geo(h3_id), 
        "geo_boundary" : Polygon(h3.h3_to_geo_boundary(h3_id, geo_json=True)).wkt, 
        "parent" : h3.h3_to_parent(h3_id), 
        "children" : h3.h3_to_children(h3_id)
    }
output_h3_id_attributes('8843acd819fffff')

'''
import h3
import googlemaps
gmaps = googlemaps.Client(key="")
h3_id = "8843a13687fffff"
h3_centroid = h3.h3_to_geo(h3_id)
response = gmaps.reverse_geocode(h3_centroid)
parse_response = {
    "address" : response[0]['formatted_address'],
    "place" : response[0]['address_components'][0]['long_name'],
    "neighbourhood" : response[0]['address_components'][1]['long_name'],
    "city" : response[0]['address_components'][2]['long_name']
}
parse_response'''
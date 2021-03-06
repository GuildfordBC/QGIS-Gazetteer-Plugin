from json import loads
from collections import namedtuple

url = "http://example.gov.uk/getdata.aspx"
params = {
    'type': 'json',
    'RequestType': 'LocationSearch',
    'gettotals': 'true',
    'axuid': '1344265603167',
    'mapsource': 'Example/MyHouse',
    '_': '1344265603168',
    'location': '##searchstring##',
    'pagesize': '100',
    'startnum': '1',
}


def parseRequestResults(data, iface=None):
    json_result = loads(data)
    columns = json_result['columns']
    for item in json_result['data']:
        mapped = dict(zip(columns, item))
        result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
        result.description = mapped['Name']
        result.x = float(mapped['X'])
        result.y = float(mapped['Y'])
        result.zoom = float(mapped['Zoom'])
        result.epsg = 27700
        yield result

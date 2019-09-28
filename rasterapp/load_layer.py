import os 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
from django.contrib.gis.utils import LayerMapping
from .models import districts

districts_mapping = {
    'ddgn': 'DDGN',
    'first_dcod': 'FIRST_DCOD',
    'first_dist': 'FIRST_DIST',
    'first_gn_c': 'FIRST_GN_C',
    'first_stat': 'FIRST_STAT',
    'shape_leng': 'SHAPE_LENG',
    'shape_area': 'SHAPE_AREA',
    'area': 'Area',
    'centroid_x': 'Centroid_X',
    'centroid_y': 'Centroid_Y',
    'geom': 'MULTIPOLYGON',
}
gapana_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/newdistrict.shp'))
def run(verbose= True):
    lm=LayerMapping(districts, gapana_shp, districts_mapping, transform= False, encoding= 'iso-8859-1')
    lm.save(strict=True,verbose=verbose)
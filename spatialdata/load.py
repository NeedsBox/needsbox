from django.contrib.gis.utils import LayerMapping

from .models import Limits

limits_mapping = {
    'id': 'id',
    'concelho': 'concelho',
    'nome': 'nome',
    'distrito': 'distrito',
    'distrito_title': 'distrito_title',
    'nuti': 'nuti',
    'nutii': 'nutii',
    'nutiii': 'nutiii',
    'ilha': 'ilha',
    'ilha_title': 'ilha_title',
    'layer': 'layer',
    'geom': 'MULTIPOLYGON',
}

concelho_shapefile = 'concelhos_4326.gpkg'


def run(verbose=True):
    layermap = LayerMapping(Limits, concelho_shapefile, limits_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)

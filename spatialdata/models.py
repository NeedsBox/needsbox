from django.contrib.gis.db import models


# Model de um concelho (deveria ter ficado numa app à parte)
class Limits(models.Model):
    concelho = models.CharField(max_length=254)
    nome = models.CharField(max_length=254)
    distrito = models.CharField(max_length=254)
    distrito_title = models.CharField(max_length=254)
    nuti = models.CharField(max_length=254)
    nutii = models.CharField(max_length=254)
    nutiii = models.CharField(max_length=254)
    ilha = models.CharField(max_length=254, null=True)
    ilha_title = models.CharField(max_length=27, null=True)
    layer = models.CharField(max_length=100, null=True)
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326)

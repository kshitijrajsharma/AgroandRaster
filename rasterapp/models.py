from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class newflood (models.Model):
    
    geometry=geomodels.PolygonField()

class agriculture (models.Model):
    geometry=geomodels.PolygonField()
    name=models.CharField(max_length=20)
    location=geomodels.PointField(max_length=30,blank=True)
    Additionalinfo=models.CharField(max_length=20,blank=True)
    Type=models.CharField(max_length=20)
    # def __unicode__(self):
    #     return self.name
    
class districts(models.Model):
    ddgn = models.BigIntegerField()
    first_dcod = models.IntegerField()
    first_dist = models.CharField(max_length=50)
    first_gn_c = models.FloatField()
    first_stat = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    area = models.FloatField()
    centroid_x = models.FloatField()
    centroid_y = models.FloatField()
    geom = geomodels.MultiPolygonField(srid=4326)
class pointofinterests(models.Model):
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()
    alt=models.FloatField()
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     birth_date = models.DateField()
#     location = models.CharField(max_length=100, blank=True)
    


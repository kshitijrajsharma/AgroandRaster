from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import newflood,agriculture,districts,pointofinterests

# Register your models here.
class newfloodadmin(LeafletGeoAdmin):
    pass
class agricultureadmin(LeafletGeoAdmin):
    list_display=('name','Type')
    settings_overrides =  {
        'DEFAULT_CENTER': (28.3949, 84.1240),
        'DEFAULT_ZOOM': 7,
        'MIN_ZOOM': 3,
        'MAX_ZOOM': 18,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
class gapanasadmin(LeafletGeoAdmin):
    list_display=('first_dist','first_stat')

@admin.register(pointofinterests)
class PersonAdmin(ImportExportModelAdmin):
    list_display=('name','lat','lon','alt')



admin.site.register(newflood,newfloodadmin)
admin.site.register(agriculture,agricultureadmin)
admin.site.register(districts,gapanasadmin)



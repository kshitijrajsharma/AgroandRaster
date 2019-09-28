from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import rasterio
from django.views.generic import TemplateView
from rasterio.features import shapes
from shapely.geometry import shape
from django.core.serializers import serialize
from .models import newflood,agriculture,districts,pointofinterests
from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from tablib import Dataset

from io import StringIO
from django.http import HttpResponse
from .resources import PersonResource

# Create your views here.
def pathrouting(request):
    template_name='route.html'
    return render(request,template_name)
def path(request):
    template_name='path.html'
    return render(request,template_name)
def district(request):
    template_name='district.html'
    return render(request,template_name)
def HomePageView(request):
    template_name= 'Home.html'
    return render(request,template_name)
def vectorize(request):  
    with rasterio.open(r'C:\Users\sharm\Desktop\naxa\flood-map.tif') as dataset:
        raster = dataset.read(1) 
        crs = dataset.crs   # copies of projection
        transform = dataset.transform # GEOCOORDinates of upper left corner of raster image
        epsg = crs['init'].lstrip('epsg:') #to put in database espg value is needed and extracted from crs value
    for polygon, value in shapes(raster, mask=raster.astype(bool), transform=transform):
        newflood.objects.create(geometry=GEOSGeometry(shape(polygon).wkt, srid=epsg))
    return HttpResponse('<h1>Vectorization done</h1>')
@login_required
def rasterdataset(request):
    raster=serialize('geojson',newflood.objects.all())
    return HttpResponse(raster,content_type='json')
@login_required
def agriculturedataset(request):
    raster=serialize('geojson',agriculture.objects.all())
    return HttpResponse(raster,content_type='json')
@login_required
def districtdataset(request):
    raster=serialize('geojson',districts.objects.all())
    return HttpResponse(raster,content_type='json')
@login_required
def shapefileimport(request):
    template_name= 'shape.html'
    return render(request,template_name)
def csv_upload(request):
    template_name='csvupload.html'
    # return render(request,template_name)
    if request.method=='POST':
        person_resource =PersonResource
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        data_set=new_persons.read()
        imported_data = dataset.load(data_set,format='csv')
        # imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request,template_name)
def csvtojson(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    return HttpResponse(response,content_type='json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    # return response


    
    
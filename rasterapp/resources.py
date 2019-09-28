from import_export import resources
from .models import pointofinterests

class PersonResource(resources.ModelResource):
    class Meta:
        model = pointofinterests
from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth import views as auth_views 
from .import views
from usersapp import views as user_views


app_name = 'maps'

urlpatterns = [
    url(r'^$', views.HomePageView, name='homepage'),
    # path('account/', include(('social_django.urls', 'social_django'), namespace='social')),
    # path('account/', include(('django.contrib.auth.urls', 'django'), namespace='auth')),
 
    # url('', include('social_django.urls', namespace='social')),
   
    path('vectorize/', views.vectorize, name='flood-vectorize'),
    path('home/', views.HomePageView, name='home'),
    path('shapefileimport/', views.shapefileimport, name='shapefileimport'),
    path('rasterdataset/', views.rasterdataset,name='Geojson-raster'),
    path('agriculturedataset/', views.agriculturedataset,name='Geojson-agri'),
    path('districtdataset/', views.districtdataset,name='Geojson-district'),
    path('routing/',views.pathrouting,name='routing'),
    path('pathfinding/', views.path,name='path-routing'),
    path('district/', views.district,name='district'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('csv/',views.csv_upload,name="csv"),
    path('csvexport/',views.csvtojson,name="csvtojson"),

]
from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
  # root
  path('', views.home, name='home'),
  #other 
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('callback', views.callback, name='callback'),
  path('notebook', views.notebook, name='notebook'),
  path('createnb', views.createnb,name="createnb"),
  path('getnb', views.getnb,name="getnb"),
]
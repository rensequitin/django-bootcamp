from django.urls import path

from . import views
app_name = "post"
urlpatterns = [
    path('',views.index, name ='index'),
    path('<post_id>/favorite/',views.favorite, name ='favorite'),
]

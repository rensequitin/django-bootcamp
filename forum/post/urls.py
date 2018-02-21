from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = "post"
urlpatterns = [
    path('',views.index, name ='index'),
    path('<post_id>/favorite/', views.favorite, name='favorite'),
    path('update/', views.update, name='update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

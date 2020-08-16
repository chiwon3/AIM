from django.urls import include, path
from . import views

urlpatterns = [
    path("parser_start/", views.save_daum_webtoon_data, name="")
]
from django.urls import path
from . import views
app_name = "pins"


urlpatterns = [
    path("create_pin/", views.create_pin,name="create_pin"),
    path("pin_detail/<int:id>/", views.pin_detail,name="pin_detail"),
]

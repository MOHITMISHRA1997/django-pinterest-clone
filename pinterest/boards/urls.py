from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('create_board',views.create_board,name="create_board"),
    path('board_detail/<str:board_title>/',views.board_detail,name="board_detail"),
    path('save_to_board/<str:title>/',views.save_to_board,name="save_to_board"),
    path('remove_from_board/<str:title>/<str:board>/',views.remove_from_board,name="remove_from_board"),
    path('edit-board/<str:board_name>/<int:id>/',views.edit_board,name="edit_board"),
]

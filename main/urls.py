from django.urls import path
from .views import create_category,delete_category, get_category, update_category
urlpatterns = [
    path("create-category/", create_category, name="create-category"),
    path("get-category/", get_category, name="get-category"),
    path("delete-category/<int:id>", delete_category, name="delete-category"),
    path("update-category/<int:id>", update_category, name="update-category"),

]
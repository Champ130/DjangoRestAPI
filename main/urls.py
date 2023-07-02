from django.urls import path
from .views import CategoryView, create_category,delete_category, get_category,  updates_category
urlpatterns = [
    path("create-category/", create_category, name="create-category"),
    path("get-category/", get_category, name="get-category"),
    path("delete-category/<int:id>", delete_category, name="delete-category"),
    path("updates-category/<int:id>", updates_category, name="updates-category"),
    path("category/",CategoryView.as_view(),name="category-views")

]
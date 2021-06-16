from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_home, name="get_data"),
    path(
        "errorreport/",
        views.get_error_details,
        #views.get_people_details,
        name="customer_search_results",
    ),

]

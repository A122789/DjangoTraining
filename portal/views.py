from django.shortcuts import render, get_object_or_404, redirect
from portal.models import (
    error,
)

# Create your views here.


def get_error_details(request):

    # Calling Get method
    # if request.method == "GET":
    error_results = error.objects.order_by("errordatetime")[:10]

    context = {
        "error_results_dict": error_results,
    }

    # log.info(context)
    return render(request, "portal/errorreport.html", context)


def get_home(request):
    return redirect("errorreport/")

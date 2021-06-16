from django.shortcuts import render, get_object_or_404, redirect
from portal.models import (
    error,
<<<<<<< HEAD
    assigner
)
import logging, sys

log = logging.getLogger(__name__)  # Defining the main logger as log

out_hdlr = logging.StreamHandler(sys.stdout)  # Defining the stream we need to log to: stdout = "print to console"

out_hdlr.setFormatter(logging.Formatter("%(message)s"))  # Formatting what the log looks like in stdout stream

out_hdlr.setLevel(logging.INFO)  # Setting the lowest levels of stuff we want to capture with the stream. Set to capture INFO + scarier ones

log.addHandler(out_hdlr)  # Attaching the stream Handler we defined to the main logger

log.setLevel(logging.INFO)  # Setting the lowest level of stuff we want to capture with the logger. Again (INFO, WARNING, ERROR,...)
=======
)

>>>>>>> origin
# Create your views here.


def get_error_details(request):

    # Calling Get method
    # if request.method == "GET":
<<<<<<< HEAD
    error_results = error.objects.order_by("-errordatetime")[:20]

    log.info(error_results[0].errordatetime)

    people_results = assigner.objects.order_by("-personid")[:20]
    log.info(people_results[0].friendlyname)

    context = {
        "error_results_dict": error_results,
        "people_results_dict": people_results,
    }

    log.info(context)
=======
    error_results = error.objects.order_by("errordatetime")[:10]

    context = {
        "error_results_dict": error_results,
    }

    # log.info(context)
>>>>>>> origin
    return render(request, "portal/errorreport.html", context)


def get_home(request):
    return redirect("errorreport/")

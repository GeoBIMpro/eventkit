from django.contrib.auth.decorators import login_required
from .service_manager import create_conf_from_wms, create_confs_from_voyager
import json
from django.http import HttpResponse, HttpResponseRedirect


@login_required
def register_service(request):
    if request.method == "POST":
        print request.POST
        service_url = request.POST.get("service_url")
        service_name = request.POST.get("service_name")
        service_type = request.POST.get("service_type")
        if 'wms' in service_type.lower():
            create_conf_from_wms(service_url, name=service_name)
        return HttpResponseRedirect("/layers/")
    else:
        return HttpResponse(
            json.dumps("This endpoint requires POST."),
            content_type='application/json',
            status=405
        )


@login_required
def import_voyager_cart(request):
    if request.method == "POST":
        service_file = request.POST.get("service_file")
        voyager_base_url = request.POST.get("voyager_base_url")
        create_confs_from_voyager(service_file, voyager_base_url)
        return HttpResponseRedirect("/layers/")
    else:
        return HttpResponse(
            json.dumps("This endpoint requires POST."),
            content_type='application/json',
            status=405
        )
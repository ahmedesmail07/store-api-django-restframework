from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response


# function based view
def api_home(request, *args, **kwargs):
    return JsonResponse({"Message": "Welcome To Your First API"})

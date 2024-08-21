from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products

@api_view(["GET"])  # It helps to create DRF view
def app_home(request, *args, **kwargs):  # Removed `self`
    model_data = Products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data=data)



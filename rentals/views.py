from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rentals.models import Rental, RentalList
from rentals.serializers import RentalSerializer, RentalListSerializer

# Create your views here.
def index(request):
    return HttpResponse("This is an API for the ember.js rentals example!")

@csrf_exempt
def rental_list(request):

    if request.method == 'GET':
        rental_list_object = RentalList(rentals=Rental.objects.all())
        serializer = RentalListSerializer(rental_list_object)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RentalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def rental_detail(request, pk):
    try:
        rental = Rental.objects.get(pk=pk)
    except Rental.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = RentalSerializer(rental)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RentalSerializer(rental, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rental.delete()
        return HttpResponse(status=204)


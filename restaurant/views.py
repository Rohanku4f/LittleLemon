from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def menu(request):
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    
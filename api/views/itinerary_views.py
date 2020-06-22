from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

from ..models.itineraries import Itinerary
from ..serializers import ItinerarySerializer

# Create your views here.
class Itineraries(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Index Request"""
        # print(request.session)
        itineraries = Itinerary.objects.filter(plan=pk)
        data = ItinerarySerializer(itineraries, many=True).data
        return Response(data)

    serializer_class = ItinerarySerializer
    def post(self, request, pk):
        """Post request"""
        # print(request.data)
        itinerary = ItinerarySerializer(data=request.data['itinerary'])
        if itinerary.is_valid():
            b = itinerary.save()
            return Response(itinerary.data, status=status.HTTP_201_CREATED)
        else:
            return Response(itinerary.errors, status=status.HTTP_400_BAD_REQUEST)

class ItineraryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        itinerary = get_object_or_404(Itinerary, pk=pk)
        data = ItinerarySerializer(itinerary).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        itinerary = get_object_or_404(Itinerary, pk=pk)
        ms = ItinerarySerializer(itinerary, data=request.data['itinerary'], partial=True)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        itinerary = get_object_or_404(Itinerary, pk=pk)
        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

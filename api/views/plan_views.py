# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.plans import Plan
from ..serializers import PlanSerializer, ItinerarySerializer, UserSerializer

# Create your views here.
class Plans(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        plans = Plan.objects.filter(owner=request.user.id)
        data = PlanSerializer(plans, many=True).data
        return Response(data)

    serializer_class = PlanSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['plan']['owner'] = request.user.id
        # Serialize/create plan
        plan = PlanSerializer(data=request.data['plan'])
        if plan.is_valid():
            p = plan.save()
            return Response(plan.data, status=status.HTTP_201_CREATED)
        else:
            return Response(plan.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        plan = get_object_or_404(Plan, pk=pk)
        data = PlanSerializer(plan).data
        if not request.user.id == data['owner']:
             raise PermissionDenied('Unauthorized, you do not own this plan')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        plan = get_object_or_404(Plan, pk=pk)
        data = PlanSerializer(plan).data
        if not request.user.id == data['owner']:
            raise PermissionDenied('Unauthorized, you do not own this plan')
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['plan'].get('owner', False):
            del request.data['plan']['owner']
        # Locate Plan
        plan = get_object_or_404(Plan, pk=pk)
        data = PlanSerializer(plan).data
        if not request.user.id == data['owner']:
            raise PermissionDenied('Unauthorized, you do not own this plan')

        # Add owner to data object now that we know this user owns the resource
        request.data['plan']['owner'] = request.user.id
        # Validate updates with serializer
        p = PlanSerializer(plan, data=request.data['plan'], partial=True)
        if p.is_valid():
            p.save()
            return Response(p.data)
        return Response(p.errors, status=status.HTTP_400_BAD_REQUEST)

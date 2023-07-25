from django.shortcuts import render
from .models import Item
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ItemSerializer
# Create your views here.

# class ThingListView(ListAPIView):
class ItemListView(ListCreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
from rest_framework import generics
from goods.models import Product
from api.serializers import ProductSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class SubjectDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

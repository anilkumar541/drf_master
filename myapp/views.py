from django.shortcuts import render

# # Create your views here.

# ****************************************function based views start here********************************

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from myapp.models import Product
# from myapp.serializers import ProductsSerializer



# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductsSerializer(products, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def products_detail(request, pk):

#     try:
#         products = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProductsSerializer(products)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductsSerializer(products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         products.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        


# ****************************************function based views end here********************************



# ****************************************class based views start here********************************
# from rest_framework.views import APIView
# from myapp.models import Category
# from myapp.serializers import CategorySerializer
# from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated



# class CategoryListView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def get(self, request):
#         category = Category.objects.all()
#         serializer= CategorySerializer(category, many=True)
#         return Response(serializer.data)

# class CategioryDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def get(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         serializer= CategorySerializer(category, many=False)
#         return Response(serializer.data)    

# class CategoryCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def post(self, request):
#         serializer= CategorySerializer(data=request.data)    
#         if serializer.is_valid():
#             serializer.save()    
#             return Response(serializer.data)    
#         else:
#             return Response(serializer.errors)

# class CategoryUpdateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def get(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         serializer= CategorySerializer(category, many=False)
#         return Response(serializer.data) 
        
#     def put(self, request, pk):
#         category= Category.objects.get(pk=pk)            
#         serializer= CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)    

#     def patch(self, request, pk):
#         category= Category.objects.get(pk=pk)            
#         serializer= CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 


# class CategoryDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     def get(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         serializer= CategorySerializer(category, many=False)
#         return Response(serializer.data) 

#     def delete(self, request, pk):
#         category= Category.objects.get(pk=pk) 
#         category.delete()
#         return Response("deleted")

        
# ****************************************class based views end here*******************************


#  ****************************************generic views starts here*******************************

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
# from myapp.models import Product
# from myapp.serializers import ProductSerializer


# class ProductListView(ListModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
     

# class ProductCreateView(CreateModelMixin,ListModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ProductRetrieveView(RetrieveModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)           

# class ProductUpdateView(UpdateModelMixin,RetrieveModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)      


# class ProductDeleteView(DestroyModelMixin,RetrieveModelMixin, GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)  

# ***************************************************generic view end here ******************************        



# ***********************************************nested serializer views starts here ******************************        

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from myapp.models import Category, Product
from myapp.serializers import CategorySerializer, ProductSerializer
from myapp.pagination import MyPageNumberPagination, TestLimitOffsetPagination, TestCursorPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



@method_decorator(cache_page(60*5), name='dispatch')
class CategoryListCreateView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination

    # pagination_class =TestLimitOffsetPagination
    # pagination_class = TestCursorPagination

    # sort based on created_at(asc and desc)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category_name'] # filter by category_name=mobile
    ordering_fields=["created_at"] #order by created_at

# class CategoryCreateView(CreateAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer

    def check_permissions(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.has_perm("myapp.add_category"):
            raise PermissionDenied

class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    #  pagination_class = MyPageNumberPagination

@method_decorator(cache_page(60), name='dispatch')
class ProductListCreateView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # throttle_classes = [CustomUserRateThrottle]
    pagination_class = MyPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['product_name', "category__category_name"]
    ordering_fields=["created_at"]
    search_fields = ["product_name"] #search_fields = ["product_name", "category__category_name"]

    def check_permissions(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.has_perm("myapp.add_product"):
            raise PermissionDenied

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #  pagination_class = MyPageNumberPagination

# ***********************************************nested serializer views ends here *****************************

from myapp.models import Faq
from myapp.serializers import FaqSerializer

@method_decorator(cache_page(60), name='dispatch')
class FaqListCreateView(ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FaqRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
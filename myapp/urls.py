from django.urls import path
from myapp import views

urlpatterns = [
    
    #function based views endpoints =>
    # path("api/products/", views.products, name='products'),
    # path("api/products/<int:pk>/", views.products_detail, name='products_detail'),

    #class based views endpoints =>
    # path("api/categories/", views.CategoryListView.as_view(), name="category"),
    # path("api/categories/post/", views.CategoryCreateView.as_view(), name="create_category"),
    # path("api/categories/category/<int:pk>/", views.CategioryDetailView.as_view(), name="get_category_id"),
    # path("api/categories/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="update_category"),
    # path("api/categories/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete_category")

    #generic views endpoints
    # path("api/products/", views.ProductListView.as_view(), name="list_product"),
    # path("api/products/post/", views.ProductCreateView.as_view(), name="create_product"),
    # path("api/products/get/<int:pk>/", views.ProductRetrieveView.as_view(), name="get_product"),
    # path("api/products/update/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    # path("api/products/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),

    #nested serializer endpoints
    path("api/categories/", views.CategoryListCreateView.as_view(), name="category_api"),
    path("api/categories/<int:pk>/", views.CategoryRUDView.as_view(), name="category_rud_api"),
    path("api/products/", views.ProductListCreateView.as_view(), name="product_api"),
    path("api/products/<int:pk>/", views.ProductRUDView.as_view(), name="product_rud_api"),
    path("api/faq/", views.FaqListCreateView.as_view()),
    path("api/faq/<int:pk>/", views.FaqRUDView.as_view())
    
]



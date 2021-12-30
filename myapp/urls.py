from django.urls import path
from myapp import views

urlpatterns = [
    
    #function based views endpoints =>
    # path("", views.products, name='products'),
    # path("<int:pk>/", views.products_detail, name='products_detail'),

    #class based views endpoints =>
    # path("", views.CategoryListView.as_view(), name="category"),
    # path("create/", views.CategoryCreateView.as_view(), name="create_category"),
    # path("category/<int:pk>/", views.CategioryDetailView.as_view(), name="get_category_id"),
    # path("update/<int:pk>/", views.CategoryUpdateView.as_view(), name="update_category"),
    # path("delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete_category")

    #generic views endpoints
    # path("", views.ProductListView.as_view(), name="list_product"),
    # path("create_product/", views.ProductCreateView.as_view(), name="create_product"),
    # path("get_product/<int:pk>/", views.ProductRetrieveView.as_view(), name="get_product"),
    # path("update_product/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product"),
    # path("delete_product/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),

    #nested serializer endpoints
    path("category_api/", views.CategoryListCreateView.as_view(), name="category_api"),
    path("category_api/<int:pk>/", views.CategoryRUDView.as_view(), name="category_rud_api"),
    path("product_api/", views.ProductListCreateView.as_view(), name="product_api"),
    path("product_api/<int:pk>/", views.ProductRUDView.as_view(), name="product_rud_api"),
    path("faq_api/", views.FaqListCreateView.as_view()),
    path("faq_api/<int:pk>/", views.FaqRUDView.as_view())
    
]



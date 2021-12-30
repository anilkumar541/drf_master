from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=88)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'categories'    

    def __str__(self):
        return self.category_name


class Product(models.Model):        
    product_name = models.CharField(max_length=88)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'products'   

    def __str__(self):
        return self.product_name


# *************************************faq model************************        

class Faq(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField()
    attachment=models.FileField(upload_to="file_data/", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        db_table ="faqs"


    def __str__(self):
        return self.question  
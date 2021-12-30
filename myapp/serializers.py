from myapp.models import Category, Product, Faq
from rest_framework import serializers

# class ProductSerializer(serializers.ModelSerializer):
#     created_at=serializers.DateTimeField(read_only=True)
#     updated_at=serializers.DateTimeField(read_only=True)
#     class Meta:
#         model=Product
#         fields=["id", "product_name", "created_at", "updated_at"]

# class CategorySerializer(serializers.ModelSerializer):
#     created_at=serializers.DateTimeField(read_only=True)
#     updated_at=serializers.DateTimeField(read_only=True)
#     class Meta:
#         model=Category
#         fields=["id", "category_name", "created_at", "updated_at"]        





# *********************************for nested serializer *************************

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=['id', 'category_name', "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
     # CHANGE "category" here to match your one-to-one field name
    category=CategorySerializer()
    class Meta:
        model=Product
        fields=['id',"product_name", "category", "created_at", "updated_at"]  

   
    def create(self, validated_data):
        # first we create category_data for category model
        category_data=validated_data.pop('category')
        category_model=Category.objects.create(**category_data)
        #now we create the product and and set product.category to fk
        product=Product.objects.create(category=category_model, **validated_data)
        # return product instance
        return product



    def update(self, instance, validated_data): 
        # CHANGE "category" here to match your one-to-one field name
        if "category" in validated_data:
            nested_serializer=self.fields["category"]
            nested_instance=instance.category
            nested_data=validated_data.pop("category")

            # Runs the update on whatever serializer the nested data belongs to
            nested_serializer.update(nested_instance, nested_data)
        # Runs the original parent update(), since the nested fields were
        # "popped" out of the data
        return super().update(instance, validated_data) 
        

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields="__all__"        
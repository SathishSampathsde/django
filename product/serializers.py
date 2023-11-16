from rest_framework import serializers
from core.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "image", "price"]
        read_only_fields = ["id"]

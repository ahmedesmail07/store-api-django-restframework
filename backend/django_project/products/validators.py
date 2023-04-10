from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


def validate_title(value):
    queryset = Product.objects.filter(title__iexact=value)
    if queryset.exists():
        raise serializers.ValidationError(
            f"This {value} is already exists as a title of another product"
        )
    return value


def validate_title_no_title_word(value):
    if "title" in value.lower():
        return serializers.ValidationError(
            f"{value} is not allowed to be a name of the title of the product"
        )
    return value


unique_prodcut_title = UniqueValidator(queryset=Product.objects.all())

from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import (
    validate_title,
    validate_title_no_title_word,
    unique_prodcut_title,
)


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name="product-delete", lookup_field="pk"
    )
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="product-update", lookup_field="pk"
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title, validate_title_no_title_word, unique_prodcut_title]
    )

    # fake_title = serializers.CharField(source="title", read_only=True)
    # Or u can inhreite from the Forienkey >= user.email
    class Meta:
        model = Product
        fields = [
            # "user",
            "url",
            "pk",
            "title",
            # "fake_title",
            "content",
            "price",
            "sale_price",
            "delete_url",
            "edit_url",
            # "email",
        ]

    def validate_title(self, value):
        queryset = Product.objects.filter(title__iexact=value)
        if queryset.exists():
            raise serializers.ValidationError(
                f"This {value} is already exists as a title of another product"
            )
        return value

    def create(self, validated_data):
        obj = super().create(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.get("email")
        return instance


"""
You can also make the reverse url using the following

"""


# class ProductSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Product
#         fields = ["url", "pk", "title", "content", "price", "sale_price"]

#     def get_url(self, obj):
#         # return f"/api/products/{obj.pk}/"
#         request = self.context.get("request")
#         if request is None:
#             return None
#         return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

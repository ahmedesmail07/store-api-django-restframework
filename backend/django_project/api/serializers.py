from rest_framework import serializers


class UserProductInlineSerialzer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # related_products = serializers.SerializerMethodField(read_only=True)

    # def get_related_products(self, obj):
    #     request = self.context.get("request")
    #     print(obj)
    #     user = obj
    #     product_queryser = user.product_set.all()[:5]
    #     return UserProductInlineSerialzer(
    #         product_queryser,
    #         many=True,
    #         context=self.context).data

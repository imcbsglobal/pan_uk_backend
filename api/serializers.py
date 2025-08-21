# app/serializers.py
from rest_framework import serializers
from .models import Product, ProductImage

CATEGORY_MAP = {
    'mens':       ["Shirt", "T-Shirt", "Jeans", "Cotton Pant", "Footwear", "Co-ords", "Watches", "Track", "Caps", "Jewellery", "Sunglasses", "Wallets", "Combo set"],
    'kidsboys':   ["Shirt", "Pants", "T-shirt", "Jeans", "Co-ords", "Combo set", "Track", "Shorts", "Footwear", "Belt", "Cap", "Sunglasses", "Suit", "Sherwani"],
    'unisex':     ["Shirt", "T-shirt", "Jeans", "Footwear", "Co-ords", "Track", "Watch", "Cap", "Sunglasses", "Jewellery"],
    'imported':   ["Shirt", "T-shirt", "Jacket", "Jeans", "Jewellery", "Sunglasses", "Watches", "Perfume", "Lotion", "Cap", "Footwear", "Crocs"],
    'weddinghub': ["Suit", "Sherwani", "Jodhpuri", "Kurthas", "Dress code"],
}

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'main_category', 'sub_category', 'name', 'price', 'brand', 'material',
            'color', 'size', 'weight', 'description', 'images', 'created_at'
        ]

    def validate(self, attrs):
        main = attrs.get('main_category') or self.instance.main_category
        sub = attrs.get('sub_category') or self.instance.sub_category
        valid_subs = CATEGORY_MAP.get(main, [])
        if sub not in valid_subs:
            raise serializers.ValidationError(
                {'sub_category': f'"{sub}" is not a valid sub category for "{main}".'}
            )
        return attrs


class ProductCreateSerializer(ProductSerializer):
    # Accept multiple files by name "images"
    images = serializers.ListField(
        child=serializers.ImageField(write_only=True),
        write_only=True,
        required=False
    )

    class Meta(ProductSerializer.Meta):
        read_only_fields = ['created_at']

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        product = super().create(validated_data)
        for img in images:
            ProductImage.objects.create(product=product, image=img)
        return product

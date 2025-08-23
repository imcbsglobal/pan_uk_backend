from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    MAIN_CATEGORY_CHOICES = [
        ('mens', "Men's Wear"),
        ('kidsboys', "Kids and Boys"),
        ('unisex', "Unisex"),
        ('imported', "Imported"),
        ('weddinghub', "Wedding Suit"),
    ]

    # We'll validate sub_category on the serializer side.
    SUB_CATEGORY_CHOICES = [
        # Men's
        ('Shirt', 'Shirt'), ('T-Shirt', 'T-Shirt'), ('Jeans', 'Jeans'), ('Cotton Pant', 'Cotton Pant'),
        ('Footwear', 'Footwear'), ('Co-ords', 'Co-ords'), ('Watches', 'Watches'), ('Track', 'Track'),
        ('Caps', 'Caps'), ('Jewellery', 'Jewellery'), ('Sunglasses', 'Sunglasses'), ('Wallets', 'Wallets'),
        ('Combo set', 'Combo set'),
        # Kids/Boys
        ('Pants', 'Pants'), ('Shorts', 'Shorts'), ('Belt', 'Belt'), ('Suit', 'Suit'), ('Sherwani', 'Sherwani'),
        # Unisex
        ('Watch', 'Watch'),
        # Imported
        ('Jacket', 'Jacket'), ('Perfume', 'Perfume'), ('Lotion', 'Lotion'), ('Crocs', 'Crocs'),
        # Wedding
        ('Jodhpuri', 'Jodhpuri'), ('Kurthas', 'Kurthas'), ('Dress code', 'Dress code'),
    ]

    main_category = models.CharField(max_length=32, choices=MAIN_CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=32, choices=SUB_CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    brand = models.CharField(max_length=120, blank=True)
    material = models.CharField(max_length=120, blank=True)
    model_name = models.CharField(max_length=120, blank=True)
    cotton_percentage = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    color = models.CharField(max_length=60, blank=True)
    size = models.CharField(max_length=60, blank=True)
    weight = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def upload_to_product(instance, filename):
    return f'products/{instance.product_id}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_product)

    def __str__(self):
        return f'Image for {self.product_id}'

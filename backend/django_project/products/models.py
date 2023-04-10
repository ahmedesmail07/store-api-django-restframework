from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    # We r setting the null = True so the if the user deleted his item will not be deleted
    # The Default = the first one
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

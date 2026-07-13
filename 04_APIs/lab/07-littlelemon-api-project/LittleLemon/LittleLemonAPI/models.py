from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    # db_index=True: client apps search/filter menu items by this title
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(default=False)
    # PROTECT: a category can't be deleted while menu items still reference it
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menuitems')

    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    # CASCADE: deleting a user also clears their cart
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # quantity * unit_price, computed on save

    class Meta:
        # one row per user per menu item; adding the same item again just updates quantity
        unique_together = ('user', 'menuitem')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # second FK to User: needs its own related_name so Django doesn't clash
    # with the reverse accessor already created by `user` above; null/blank
    # because an order has no delivery crew assigned until a manager sets one
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='delivery_crew'
    )
    status = models.BooleanField(default=False)  # False = not yet delivered
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # quantity * unit_price, computed on save

    class Meta:
        # one row per menu item per order; quantity can still vary
        unique_together = ('order', 'menuitem')

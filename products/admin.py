from django.contrib import admin

from .models import Category, Discount, Product, Customer, Address, Order, OrderItem, Comment, Cart, CartItem

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["name", "top_product"]

class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    list_display = ["discount"]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "category", "price", "inventory",]

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ["first_name", "Last_name", "email", "phone_number",]

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ["customer", "province", "city", "street"]

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["customer", "datetime_created", "status"]

class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ["order", "product", "quantity", "price"]

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["customer", "name", "status"]

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ["created"]

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ["cart", "product", "quantity"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

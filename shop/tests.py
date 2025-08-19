from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Catagory, Product, Cart, Favourite
from . import views


# ------------------------------
# Model Tests
# ------------------------------
class ModelTests(TestCase):

    def setUp(self):
        self.category = Catagory.objects.create(
            name="Electronics",
            description="Electronic Items"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Laptop",
            vendor="Dell",
            quantity=5,
            original_price=50000,
            selling_price=45000,
            description="High performance laptop"
        )
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Electronics")

    def test_product_str(self):
        self.assertEqual(str(self.product), "Laptop")

    def test_cart_total_cost(self):
        cart = Cart.objects.create(user=self.user, product=self.product, product_qty=2)
        self.assertEqual(cart.total_cost, 90000)

    def test_favourite_creation(self):
        fav = Favourite.objects.create(user=self.user, product=self.product)
        self.assertEqual(fav.product.name, "Laptop")


# ------------------------------
# URL Tests
# ------------------------------
class URLTests(TestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, views.home)

    def test_register_url_resolves(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, views.register)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, views.login_page)

    def test_cart_url_resolves(self):
        url = reverse("cart")
        self.assertEqual(resolve(url).func, views.cart_page)


# ------------------------------
# View Tests
# ------------------------------
class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_home_view_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_logout_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

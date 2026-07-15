from django.test import TestCase
from .models import Menu


class MenuModelTest(TestCase):

    def test_create_menu_item(self):
        item = Menu.objects.create(
            title="Pizza",
            price=300,
            inventory=20
        )

        self.assertEqual(item.title, "Pizza")
        self.assertEqual(item.price, 300)
        self.assertEqual(item.inventory, 20)
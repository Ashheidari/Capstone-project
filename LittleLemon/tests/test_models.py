from django.test import TestCase
from Restaurant.models import Menu




class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(title = 'Ice Cream', price = 11, inventory = 80)
        self.assertEqual(item.__str__(), "Ice Cream : 11")

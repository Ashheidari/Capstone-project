from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuItemSerilaizer


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title = 'Test Menu 1', price = 10.99, inventory = 90)
        Menu.objects.create(title = 'Test Menu 2', price = 15.99, inventory = 40)
        Menu.objects.create(title = 'Test Menu 3', price = 8.99, inventory = 50)
    

    def test_getall(self):
        menus = Menu.objects.all()
        serializer_menu = MenuItemSerilaizer(menus, many=True)
        expected_data = [
            {"id":2, "title": "Test Menu 1", "price": "10.99", "inventory" : 90},
            {"id":3, "title": "Test Menu 2", "price": "15.99", "inventory" : 40},
            {"id":4, "title": "Test Menu 3", "price": "8.99", "inventory" : 50},
            
            ]

        self.assertListEqual(serializer_menu.data, expected_data)

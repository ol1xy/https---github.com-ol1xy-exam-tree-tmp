import unittest
from organization import Organisation

class TestOrganisation(unittest.TestCase):
    """
    Класс для тестирования класса "Organisation".
    """

    def test_creating_single(self):
        """
        Тест создания единственного экземпляра объекта по принципу "Одиночка".
        """
        organisation1 = Organisation.__init__(self, "123", "Название 1", "Адрес 1", "12345")
        organisation2 = Organisation.__init__(self, "456", "Название 2", "Адрес 2", "67890")

        self.assertEqual(organisation1, organisation2)

    def test_properties(self):
        """
        Тест получения и обновления свойств объекта.
        """
        organisation = Organisation.__init__(self, "789", "Название 3", "Адрес 3", "01234")

        properties = Organisation.get_properties(self)
        self.assertEqual(properties["code"], "789")
        self.assertEqual(properties["name"], "Название 3")
        self.assertEqual(properties["adress"], "Адрес 3")
        self.assertEqual(properties["post_index"], "01234")

        Organisation.update_properties(self, name="Новое название", adress="Новый адрес")
        properties = Organisation.get_properties(self)
        self.assertEqual(properties["code"], "789")
        self.assertEqual(properties["name"], "Новое название")
        self.assertEqual(properties["adress"], "Новый адрес")
        self.assertEqual(properties["post_index"], "01234")


if __name__ == "__main__":
    unittest.main()

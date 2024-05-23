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
        organisation1 = Organisation("123", "Название 1", "Адрес 1", "12345")
        organisation2 = Organisation("456", "Название 2", "Адрес 2", "67890")

        self.assertEqual(organisation1, organisation2)

    def test_properties(self):
        """
        Тест получения и обновления свойств объекта.
        """
        organisation = Organisation.__init__(self, "789", "Название 3", "Адрес 3", "01234")

        # Получение всех свойств
        self.assertEqual(organisation.code, "789")
        self.assertEqual(organisation.name, "Название 3")
        self.assertEqual(organisation.adress, "Адрес 3")
        self.assertEqual(organisation.postal_code, "01234")

        # Обновление значений через setter
        organisation.adress(self, "Новый адрес")

        # Проверка обновленных значений
        self.assertEqual(organisation.address, "Новый адрес")

        # Обновление одного свойства через setter
        organisation.code = "Новый код"

        # Проверка обновленного значения
        self.assertEqual(organisation.code, "Новый код")
        self.assertEqual(organisation.address, "Новый адрес")

    def test_validation(self):
        """
        Тест валидации значений при обновлении свойств.
        """
        organisation = Organisation.__init__(self, "789", "Название 3", "Адрес 3", "01234")

        # Ожидаемая ошибка при попытке обновить код не строкой
        with self.assertRaises(TypeError):
            organisation.code = 123

        # Ожидаемая ошибка при попытке обновить наименование не строкой
        with self.assertRaises(TypeError):
            organisation.name = 456

        # Ожидаемая ошибка при попытке обновить адрес не строкой
        with self.assertRaises(TypeError):
            organisation.address = True

        # Ожидаемая ошибка при попытке обновить почтовый индекс не строкой
        with self.assertRaises(TypeError):
            organisation.postal_code = None

    def test_nonexistent_property(self):
        """
        Тест обновления несуществующего свойства.
        """
        organisation = Organisation(self, "789", "Название 3", "Адрес 3", "01234")

        # Ожидаемая ошибка при попытке обновить несуществующее свойство
        with self.assertRaises(KeyError):
            organisation.nonexistent_property = "value"


if __name__ == "__main__":
    unittest.main()


class Organisation:
    """
    Класс для хранения и управления свойствами модели "Организация".

    Использует шаблон "Одиночка" для обеспечения доступа к одному экземпляру объекта.
    """

    __instance = None  # Экземпляр объекта

    def __new__(cls):
        """
        Метод создания нового экземпляра класса.

        Обеспечивает доступ к одному экземпляру объекта по принципу "Одиночка".
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, code, name, adress, post_index):
        """ 
        Метод инициализации объекта.

        Присваивает значения атрибутам объекта.
        """

        self.code = code
        self.name = name
        self.adress = adress
        self.post_index = post_index

    def get_properties(self):
        """
        Метод получения всех свойств объекта.

        Возвращает словарь с ключами-названиями атрибутов и значениями.
        """
        return {
            "code": self.code,
            "name": self.name,
            "adress": self.adress,
            "post_index": self.post_index,
        }

    def update_properties(self, **kwargs):
        """
        Метод обновления значений свойств объекта.

        Принимает словарь с ключами-названиями атрибутов и новыми значениями.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

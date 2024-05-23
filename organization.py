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

    def __init__(self, code, name, address, postal_code):
        """
        Метод инициализации объекта.

        Присваивает значения атрибутам объекта.
        """
        self.code = code
        self.name = name
        self.address = address
        self.postal_code = postal_code

    @property
    def code(self):
        """
        Геттер для атрибута "код".
        """
        return self._code

    @code.setter
    def code(self, new_code):
        """
        Сеттер для атрибута "код".
        """
        if not isinstance(new_code, str):
            raise TypeError("Код должен быть строкой")
        self._code = new_code

    @property
    def name(self):
        """
        Геттер для атрибута "наименование".
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Сеттер для атрибута "наименование".
        """
        if not isinstance(new_name, str):
            raise TypeError("Наименование должно быть строкой")
        self._name = new_name

    @property
    def adress(self):
        """
        Геттер для атрибута "адрес".
        """
        return self._address

    @adress.setter
    def adress(self, new_address):
        """
        Сеттер для атрибута "адрес".
        """
        if not isinstance(new_address, str):
            raise TypeError("Адрес должен быть строкой")
        self._address = new_address

    @property
    def postal_code(self):
        """
        Геттер для атрибута "почтовый индекс".
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, new_postal_code):
        """
        Сеттер для атрибута "почтовый индекс".
        """
        if not isinstance(new_postal_code, str):
            raise TypeError("Почтовый индекс должен быть строкой")
        self._postal_code = new_postal_code
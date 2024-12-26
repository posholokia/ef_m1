from copy import copy


class Server:
    """
    Представление объекта сервера.
    """

    __next_ip: int = 0

    def __init__(self):
        self.ip: int = self.__next_ip  # IP сервера
        self.buffer: list[Data] = []  # буфер полученных данных
        self.__router: Router | None = None  # к какому роутеру присоединен

    def __new__(cls, *args, **kwargs):
        cls.__next_ip += 1
        return super().__new__(cls, *args, **kwargs)

    def send_data(self, data: "Data") -> None:
        """
        Отправка пакета данных получателю.

        :param data: Пакет данных.
        :return: None.
        """
        self.__router.buffer.append(data)

    def set_router(self, router: "Router") -> None:
        """
        Связывает сервер с роутером.

        :param router: Роутер.
        :return: None.
        """
        self.__router = router

    def del_router(self) -> None:
        """
        Отсоединить сервер от роутера.

        :return: None.
        """
        self.__router = None

    def get_data(self) -> list["Data"]:
        """
        Получить список принятых пакетов.

        :return: Список принятых пакетов.
        """
        data = copy(self.buffer)
        self.buffer.clear()
        return data

    def get_ip(self) -> int:
        """
        Получить IP сервера.

        :return: IP сервера.
        """
        return self.ip


class Router:
    """
    Представление объекта роутера.
    """

    def __init__(self):
        self.buffer: list[Data] = []  # буфер данных
        self.servers: dict[int, Server] = {}  # присоединенные серверы

    def link(self, server: Server) -> None:
        """
        Добавление сервера к роутеру.

        :param server: Сервер.
        :return: None.
        """
        self.servers[server.ip] = server
        server.set_router(self)

    def unlink(self, server: Server) -> None:
        """
        Отсоединение сервера от роутера.

        :param server: Сервер.
        :return: None.
        """
        self.servers.pop(server.ip)
        server.del_router()

    def send_data(self) -> None:
        """
        Отправка всех пакетов из буфера серверам.

        :return: None.
        """
        for data in self.buffer:
            server = self.servers[data.ip]
            server.buffer.append(data)
        self.buffer.clear()


class Data:
    """
    Представление объекта пакета данных.
    """

    def __init__(self, data: str, ip: int) -> None:
        """
        :param data: Данные.
        :param ip: IP сервера получателя.
        """
        self.data = data
        self.ip = ip

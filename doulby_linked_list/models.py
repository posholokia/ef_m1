from typing import Self, Union


class LinkedList:
    """
    Двусвязный список.
    """

    def __init__(self) -> None:
        self.head: Union["ObjList", None] = None  # первый элемент списка
        self.tail: Union["ObjList", None] = None  # последний элемент списка

    def add_obj(self, node: "ObjList") -> None:
        """
        Добавление нового элемента в конец списка.

        :param node: Новый элемент списка.
        :return: None.
        """
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node

    def remove_obj(self) -> None:
        """
        Удаление последнего элемента списка.

        :return: None.
        :raises IndexError: Список пустой.
        """
        if self.tail is None:
            raise IndexError("Список уже пустой.")

        prev_tail = self.tail.get_prev()

        if prev_tail is None:
            self.head = None
        else:
            prev_tail.set_next(None)

        self.tail.set_prev(None)
        self.tail = prev_tail

    def get_data(self) -> list[str]:
        """
        Получить список данных всего списка в строковом представлении.

        :return: Список значений всех элементов списка.
        """
        if self.head is None:
            return []

        data = []
        next_ = self.head

        while next_:
            data.append(next_.get_data())
            next_ = next_.get_next()

        return data


class ObjList:
    """
    Элемент двусвязного списка.
    """

    def __init__(self, data: str) -> None:
        """
        :param data: Данные элемента списка.
        """
        self.__data = data
        self.__next: Self | None = None  # ссылка на следующий элемент
        self.__prev: Self | None = None  # ссылка на предыдущий элемент

    def set_next(self, next_: Self | None) -> None:
        """
        Установить значение следующего элемента списка.

        :param next_: Следующий элемент списка.
        :return: None
        """
        self.__next = next_

    def set_prev(self, prev: Self | None) -> None:
        """
        Установить значение предыдущего элемента списка.

        :param prev: Предыдущий элемент списка.
        :return: None
        """
        self.__prev = prev

    def set_data(self, data: str) -> None:
        """
        Присвоить значение текущему элементу.

        :param data: Данные списка.
        :return: None.
        """
        self.__data = data

    def get_next(self) -> Self | None:
        """
        Получить данные следующего элемента списка.

        :return: Следующий элемент списка.
        """
        return self.__next

    def get_prev(self) -> Self | None:
        """
        Получить данные предыдущего элемента списка.

        :return: Предыдущий элемент списка.
        """
        return self.__prev

    def get_data(self) -> str:
        """
        Получение значения текущего элемента списка.

        :return: Данные этой текущей ячейки списка.
        """
        return self.__data

from random import SystemRandom


class Cell:
    """
    Клетка игрового поля.
    """
    def __init__(self, around_mines: int, mine: bool) -> None:
        """
        :param around_mines: Количество мин рядом с клеткой.
        :param mine: В этой клетке мина? Да/нет.
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False  # клетка открыта? Да/нет.


class GamePole:
    """
    Игровое поле.
    """

    def __init__(self, size: int, mines: int) -> None:
        """
        :param size: Размер игрового поля.
        :param mines: Кол-во мин на поле.
        """
        self.__size = size
        self.__area: list[list[Cell]] = []
        self.init(mines)

    def init(self, mines: int) -> None:
        """
        Инициализация игрового поля размером NxN, где N = self.size.

        :param mines: Количество мин на поле.
        :return: None.
        """
        self.__area = self.__generate_pole()
        mine_indexes = self.__generate_mine_indexes(mines)
        self.__set_mine_on_pole(self.__area, mine_indexes)

    def show(self) -> None:
        """
        Отображение игрового поля в консоли.

        :return: None.
        """
        for row in self.__area:
            pole_row: list[str] = []

            for cell in row:
                if not cell.fl_open:
                    pole_row.append("#")
                elif cell.mine:
                    pole_row.append("*")
                else:
                    pole_row.append(str(cell.around_mines))
            print(" ".join(pole_row))

    def __generate_pole(self) -> list[list[Cell]]:
        """
        Генерация игрового поля заполненного пустыми клетками.

        :return: Массив клеток без мин.
        """
        area: list[list[Cell]] = []

        for _ in range(self.__size):
            row: list[Cell] = []

            for _ in range(self.__size):
                row.append(Cell(around_mines=0, mine=False))

            area.append(row)

        return area

    def __generate_mine_indexes(self, mines: int) -> list[tuple[int, int]]:
        """
        Случайное распределение мин по полю.

        :return: Список индексов клеток с минами.
        """
        index_matrix: list[tuple[int, int]] = []

        for x in range(self.__size):
            for y in range(self.__size):
                index_matrix.append((x, y))

        random = SystemRandom()
        return random.sample(index_matrix, mines)

    def __set_mine_on_pole(
        self,
        pole: list[list[Cell]],
        mine_indexes: list[tuple[int, int]],
    ) -> None:
        """
        Установка мин в клетки игрового поля.

        :param pole: Игровое поле.
        :param mine_indexes: Координаты мин.
        :return: None.
        """
        for x, y in mine_indexes:
            pole[x][y].mine = True
            around_indexes = self.__get_around_indexes(x, y)

            for around_x, around_y in around_indexes:
                pole[around_x][around_y].around_mines += 1

    def __get_around_indexes(self, x: int, y: int) -> list[tuple[int, int]]:
        """
        По координате клетки выводит координаты окружающих ее клеток на поле.

        :param x: Координата x клетки.
        :param y: Координата y клетки.
        :return: Список (x, y) координат окружающих клеток.
        """
        indexes: list[tuple[int, int]] = []
        # определяем границы координат окружающих клеток,
        # чтобы они не выходили за пределы поля.
        # У правой границы добавляем 2, так как в range последнее значение
        # не включается, и мы получим координаты от x - 1 до x + 1 включительно.
        x_left = x - 1 if x - 1 >= 0 else 0
        x_right = x + 2 if x + 2 <= self.__size else self.__size
        y_left = y - 1 if y - 1 >= 0 else 0
        y_right = y + 2 if y + 2 <= self.__size else self.__size

        for row_index in range(x_left, x_right):
            for col_index in range(y_left, y_right):
                indexes.append((row_index, col_index))

        return indexes


if __name__ == '__main__':
    pole_game = GamePole(10, 12)

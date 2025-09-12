class Piece:
    def __init__(self, color, position=('d',4)):
        self.color = color
        self.position = position

    def get_available_cells(self):
        pass

    """Изменение позиции фигуры"""
    def change_position(self, position):
        if position not in self.get_available_cells():
            return 'ERROR: impossible move'
        else:
            self.position = position
            return 'Changed position successfully'

    """Получение позиции"""
    def get_position(self):
        return self.position

    """Получение цвета"""
    def get_color(self):
        return self.color


class King(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if (x + i == x and y + j == y) or (x + i < 97 or x + i > 104) or (y + j < 1 or y + j > 8):
                    continue
                available_cells.append((chr(x+i), y + j))
        return available_cells

class Rook(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        for i in range(-7,8):
            for j in range(-7,8):
                if (x + i == x and y + j == y) or (x + i < 97 or x + i > 104) or (y + j < 1 or y + j > 8):
                    continue
                if i == 0 or j == 0:
                    available_cells.append((chr(x + i), y + j))
        return available_cells

class Bishop(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        for i in range(-7,8):
            for j in range(-7,8):
                if (x + i == x and y + j == y) or (x + i < 97 or x + i > 104) or (y + j < 1 or y + j > 8):
                    continue
                if abs(i) == abs(j):
                    available_cells.append((chr(x + i), y + j))
        return available_cells

class Queen(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        for i in range(-7,8):
            for j in range(-7,8):
                if (x + i == x and y + j == y) or (x + i < 97 or x + i > 104) or (y + j < 1 or y + j > 8):
                    continue
                if (abs(i) == abs(j)) or (i == 0 or j == 0):
                    available_cells.append((chr(x + i), y + j))
        return available_cells

class Knight(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        for i in range(-2,3):
            for j in range(-2,3):
                if (x + i == x and y + j == y) or (x + i < 97 or x + i > 104) or (y + j < 1 or y + j > 8):
                    continue
                if not ((abs(i) == abs(j)) or (i == 0 or j == 0)):
                    available_cells.append((chr(x + i), y + j))
        return available_cells

class Pawn(Piece):
    def __init__(self, color, position=('d',4)):
        super().__init__(color, position)

    """Получение доступных для хода клеток"""
    def get_available_cells(self):
        available_cells = []
        x = ord(self.position[0])
        y = self.position[1]
        if self.color == 'white' and y == 2:
            available_cells.append((chr(x), y + 2))
            available_cells.append((chr(x), y + 1))
        elif self.color == 'black' and y == 7:
            available_cells.append((chr(x), y - 2))
            available_cells.append((chr(x), y - 1))
        elif self.color == 'white' and y != 8:
            available_cells.append((chr(x), y+1))
        elif self.color == 'black' and y != 1:
            available_cells.append((chr(x), y-1))
        return available_cells


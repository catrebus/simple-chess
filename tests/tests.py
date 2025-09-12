from Pieces import King, Rook, Bishop, Queen, Knight
import pytest

class TestKing:

    @pytest.mark.parametrize('color, expected_color, expected_position', [('white', 'white', ('d', 4)), ('black', 'black', ('d', 4))])
    def test_init(self, color, expected_color, expected_position):
        king = King(color)
        assert king.color == expected_color
        assert king.get_position() == expected_position

    @pytest.mark.parametrize('position, expected_cells', [(('e',8),[('d',8),('d',7),('e',7),('f',7),('f',8)]),
                                                         (('c',5), [('b',4),('b',5),('b',6), ('c',6), ('d',6), ('d',5),('d',4), ('c',4)]),
                                                          (('a',1), [('a',2),('b',2), ('b',1)]),(('h',8),
                                                          [('g',8),('g',7),('h',7)])])
    def test_get_available_cells_king(self, position, expected_cells):
        obj = King('white')
        obj.position = position
        sortedList = sorted(obj.get_available_cells())
        sortedExpectedList = sorted(expected_cells)
        assert sortedList == sortedExpectedList

class TestRook:

    @pytest.mark.parametrize('position, expected_cells', [(('d',4), [('a', 4), ('b', 4), ('c', 4), ('d', 1), ('d', 2), ('d', 3), ('d', 5), ('d', 6), ('d', 7), ('d', 8), ('e', 4), ('f', 4), ('g', 4), ('h', 4)]),
                                                          (('g',2), [('g', 1), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('g', 8), ('a', 2), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2), ('h', 2)]),
                                                          (('a',8), [('a', 7), ('a', 6), ('a', 5), ('a', 4), ('a', 3), ('a', 2), ('a', 1), ('b', 8), ('c', 8), ('d', 8), ('e', 8), ('f', 8), ('g', 8), ('h', 8)]),
                                                          (('g',5), [('g', 1), ('g', 2), ('g', 3), ('g', 4), ('g', 6), ('g', 7), ('g', 8), ('a', 5), ('b', 5), ('c', 5), ('d', 5), ('e', 5), ('f', 5), ('h', 5)])])
    def test_get_available_cells_rook(self, position, expected_cells):
        obj = Rook('white')
        obj.position = position
        sortedList = sorted(obj.get_available_cells())
        sortedExpectedList = sorted(expected_cells)
        assert sortedList == sortedExpectedList

class TestBishop:

    @pytest.mark.parametrize('position, expected_cells', [(('f',7), [('a',2), ('b', 3), ('c', 4), ('d', 5), ('e', 6), ('g', 8), ('e', 8), ('g', 6), ('h', 5)]),
                                                          (('f',3), [('a',8), ('b', 7), ('c', 6), ('d', 5), ('e', 4),('g',2),('h',1), ('d', 1), ('e', 2), ('g', 4), ('h', 5)])])
    def test_get_available_cells_bishop(self, position, expected_cells):
        obj = Bishop('white')
        obj.position = position
        sortedList = sorted(obj.get_available_cells())
        sortedExpectedList = sorted(expected_cells)
        assert sortedList == sortedExpectedList

class TestQueen:

    @pytest.mark.parametrize('position, expected_cells', [(('d',4), [('a', 1), ('b', 2), ('c', 3), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('g', 1), ('f', 2), ('e', 3), ('c', 5), ('b', 6), ('a', 7), ('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), ('g', 4),('h',4), ('d', 1), ('d', 2), ('d', 3), ('d', 5), ('d', 6), ('d', 7), ('d', 8) ]),
                                                          (('a',1), [('b', 2), ('c', 3),('d',4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1),('g',1), ('h', 1)])])
    def test_get_available_cells_queen(self, position, expected_cells):
        obj = Queen('white')
        obj.position = position
        sortedList = sorted(obj.get_available_cells())
        sortedExpectedList = sorted(expected_cells)
        assert sortedList == sortedExpectedList

class TestKnight:

    @pytest.mark.parametrize('position, expected_cells', [(('a',1), [('b',3), ('c',2)]),
                                                          (('b',4), [('a',6), ('a',2), ('c',6), ('c',2), ('d',5),('d',3)])])
    def test_get_available_cells_knight(self, position, expected_cells):
        obj = Knight('white')
        obj.position = position
        sortedList = sorted(obj.get_available_cells())
        sortedExpectedList = sorted(expected_cells)
        assert sortedList == sortedExpectedList
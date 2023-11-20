class Knight:
    move = tuple(zip((-2, -2, -1, 1, -1, 1, 2, 2), (-1, 1, 2, 2, -2, -2, -1, 1)))
    x_map = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    y_map = {8 - i: i for i in range(8)}

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        
    def get_char(self):
        return 'N'
    
    def can_move(self, x, y):
        x, y = self.x_map[x], self.y_map[y]
        for m_x, m_y in self.move:
            if self.x_map[self.horizontal] + m_x == x and \
                self.y_map[self.vertical] + m_y == y:
                return True
        return False
    
    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        field = [['.'] * 8 for _ in range(8)]
        field[self.y_map[self.vertical]][self.x_map[self.horizontal]] = 'N'
        for x, y in self.move:
            if 0 <= (new_x := self.y_map[self.vertical] + y) < 8 and \
               0 <= (new_y := self.x_map[self.horizontal] + x) < 8:
                field[new_x][new_y] = '*'
        for i in field:
            print(*i, sep='')


knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()
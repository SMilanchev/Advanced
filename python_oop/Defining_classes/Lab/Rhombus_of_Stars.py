GROWING: int = 1
SHRINKING: int = -1


def draw_rhombus(size: int):
    def print_line(i: int, direction: int):
        if i == 0:
            return
        print((' ' * (size-i) + '* ' * i).rstrip())
        if i == size:
            direction = SHRINKING
        print_line(i + direction, direction)
    print_line(1, GROWING)

draw_rhombus(10)
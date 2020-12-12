from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])


def read_input(filename):
    instructions = []
    with open(filename) as f:
        for line in f:
            k = line[0]
            v = int(line.strip()[1:])
            instructions.append((k,v))
    return instructions


DIRECTIONS = ['N', 'E', 'S', 'W']


def follow_instr(x, y, dir, instr):
    i_k, i_v = instr
    if i_k == "F":
        return follow_instr(x, y, dir, (dir, i_v))
    if i_k in ["R", 'L']:
        shift = i_v // 90
        cur_index = DIRECTIONS.index(dir)
        new_index = cur_index + shift if i_k == "R" else cur_index - shift
        return(x, y, DIRECTIONS[new_index % 4])
    if i_k == "N":
        return (x, y + i_v, dir)
    if i_k == "S":
        return (x, y - i_v, dir)
    if i_k == "E":
        return (x + i_v, y, dir)
    if i_k == "W":
        return (x - i_v, y, dir)


def follow_waypoint_instr(ship, waypoint, instr):
    i_k, i_v = instr
    sw_diff = Point(waypoint.x-ship.x, waypoint.y-ship.y)
    if i_k == "F":
        return Point(ship.x + i_v * sw_diff.x, ship.y + i_v *sw_diff.y), Point(waypoint.x + i_v * sw_diff.x, waypoint.y + i_v *sw_diff.y)
    if i_k in ["R", 'L']:
        if i_v == 180:
            sw_diff_new = Point(-sw_diff.x, -sw_diff.y)
        elif instr in (("R", 90), ("L", 270)):
            sw_diff_new = Point(sw_diff.y, -sw_diff.x)
        else:
            sw_diff_new = Point(-sw_diff.y, sw_diff.x)
        return ship, Point(ship.x + sw_diff_new.x, ship.y +sw_diff_new.y)
    if i_k == "N":
        return ship, Point(waypoint.x, waypoint.y + i_v)
    if i_k == "S":
        return ship, Point(waypoint.x, waypoint.y - i_v)
    if i_k == "E":
        return ship, Point(waypoint.x + i_v, waypoint.y)
    if i_k == "W":
        return ship, Point(waypoint.x - i_v, waypoint.y)


instr = read_input("../data/input_12.txt")
x = 0
y = 0
dir = "E"
ship = Point(0, 0)
wp = Point(10, 1)
for ins in instr:
    x, y, dir = follow_instr(x, y, dir, ins)
    ship, wp = follow_waypoint_instr(ship, wp, ins)
print(x, y, abs(x)+abs(y))
print(ship, abs(ship.x) + abs(ship.y))

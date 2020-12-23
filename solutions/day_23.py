from tqdm import trange

def create_circle(cups):
    circle = dict()
    c_size = len(cups)
    for i in range(len(cups)):
        circle[cups[i]] = cups[(i + 1) % c_size]
    return circle


def make_move(circle, current):
    next = current
    pickup = []
    for i in range(3):
        next = circle[next]
        pickup.append(next)
    dest_cup = current
    while True:
        dest_cup -= 1
        if dest_cup == 0:
            dest_cup = len(circle)
        if dest_cup not in pickup:
            break
    circle[current] = circle[pickup[-1]]
    circle[pickup[-1]] = circle[dest_cup]
    circle[dest_cup] = pickup[0]
    return circle, circle[current]


cups = list(map(int, list('598162734')))
cups_circle = create_circle(cups)
current = cups[0]
for i in range(100):
    cups_circle, current = make_move(cups_circle, current)
res = []
cur = 1
for i in range(9):
    cur = cups_circle[cur]
    res.append(cur)
print(''.join(map(str, res)))

new_cups = list(range(1, 1000001))
new_cups[:9] = list(map(int, list('598162734')))
cups_circle = create_circle(new_cups)
current = cups[0]
for i in trange(10**7):
    cups_circle, current = make_move(cups_circle, current)
print(cups_circle[1]*cups_circle[cups_circle[1]])
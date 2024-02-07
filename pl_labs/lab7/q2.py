target_hit = [(0, 0), (10, 10), (6, 6), (7, 8)]
radius = 10
for val in target_hit:
    x, y = val
    if x**2+y**2 <= radius**2:
        print("You have hit the target")
    else:
        print("You have missed the target")

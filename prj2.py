def get_pi():
    return 3.14


def get_circumference(radius):
    pi = get_pi()
    return 2 * pi * radius


r = int(input("Radius? "))
answer = get_circumference(r)
print("{0:5.4f}".format(answer))

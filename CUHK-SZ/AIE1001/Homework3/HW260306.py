class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def squaredDistance(self):
        return int(self.x**2 + self.y**2)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def squaredDistance(self):
        return super().squaredDistance() + self.z**2

def displayPoint(point, dx, dy):
    before = point.squaredDistance()
    point.move(dx, dy)
    after = point.squaredDistance()
    print(before, after)

n = int(input())
points = []
for i in range(n):
    values = input().split()
    dimension = int(values[0])
    x = int(values[1])
    y = int(values[2])
    if dimension == 2:
        points.append(Point(x, y))
    else:
        points.append(Point3D(x, y, int(values[3])))
values = input().split()
dx = int(values[0])
dy = int(values[1])
for point in points:
    displayPoint(point, dx, dy)


import math

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> "Vector":
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other) -> "Vector":
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float], end_point: tuple[float]) -> "Vector":
        return cls(x=end_point[0] - start_point[0], y=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (pow(self.x, 2) + pow(self.y, 2)) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(x=self.x / length, y=self.y / length)

    def angle_between(self, other: "Vector") -> int:
        mul = self.__mul__(other)
        mul_length = self.get_length() * other.get_length()
        cos_angle = mul / mul_length
        return math.trunc(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        return math.trunc(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int) -> "Vector":
        radian = math.radians(angle)
        x2 = math.cos(radian) * self.x - math.sin(radian) * self.y
        y2 = math.sin(radian) * self.x + math.cos(radian) * self.y
        return Vector(x=x2, y=y2)

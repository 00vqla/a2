import enum


class Weeks(enum.Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


print(Weeks.MON.value)
print(Weeks(1))

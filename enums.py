# Enums
from enum import Enum


class EnumState(Enum):
    # State
    STATE_INIT = 0
    STATE_READY = 1
    STATE_RUNNING = 2
    STATE_STOP = 3
    STATE_ERROR = 4


print(EnumState.STATE_INIT.value)
print(EnumState.STATE_READY.value)


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Weekday.MONDAY
print(today)  # Output: Weekday.MONDAY
print(today.value)  # Output: 1


for day in Weekday:
    print(day.name, day.value)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)  # Output: Color.RED
print(Color.GREEN.value)  # Output: 2

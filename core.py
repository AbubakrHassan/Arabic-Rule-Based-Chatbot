import regex as re


class ROOMS:
    LIVING_ROOM, DINING_ROOM, KITCHEN, BATHROOM, BEDROOM, OTHER = range(6)
    matchers = {
        LIVING_ROOM:
            [
                "(.*)غرفه المعيشه(.*)",
                "(.*)هول(.*)",
                "(.*)صالون(.*)"
            ],
        DINING_ROOM:
            [
                "(.*)غرفه الاكل(.*)",
                "(.*)غرفه الطعام(.*)"
            ],
        KITCHEN:
            [
                "(.*)مطبخ(.*)"
            ],
        BATHROOM:
            [
                "(.*)حمام(.*)",
                "(.*)دوره المياه(.*)"
            ],
        BEDROOM:
            [
                "(.*)غرفه النوم(.*)"
            ],
        OTHER:
            [

            ]
    }


class User:
    def __init__(self, name):
        self.name = name


class Room:
    def __init__(self, name, room_type, owner=None):
        self.name = name
        self.type = room_type
        self.owner = owner

    def match(self, name):
        if self.name == name:
            return True
        for matcher in ROOMS.matchers[self.type]:
            if re.match(matcher, name):
                return True

from devices import Fan, Temperature, AC, Door, Light
from core import User, Room, ROOMS
import regex as re
import normalizer

"""
    following dictionary contains all the devices in the house,
    each device should be defined as a class which is has it's own properties, right now just assume a string
"""
welcome_message = """مرحبًا بك ، هذا هو النظام الاوتوماتيكي المصمم لإدارة أجهزتك في المنزل ،
                ماذا تريدني ان افعل"""

abubakr = User("Abubakr")
bedroom = Room("غرفه ابوبكر", room_type=ROOMS.BEDROOM, owner=abubakr)
bathroom = Room("الحمام", room_type=ROOMS.BATHROOM, owner=abubakr)
kitchen = Room("مطبخ", room_type=ROOMS.KITCHEN, owner=abubakr)

home = {
    bedroom:
        [
            Fan(bedroom),
            AC(bedroom),
            Door(bedroom),
            Light(bedroom),
            Temperature(bedroom)
        ],
    bathroom:
        [
            Door(bathroom),
            Light(bathroom)
        ],
    kitchen:
        [
            Fan(kitchen),
            AC(kitchen),
            Door(kitchen),
            Light(kitchen),
            Temperature(kitchen)
        ]
}
while True:
    user_reply = input(">> ")
    user_reply = normalizer.normalize(user_reply)
    if re.match(".*(سلام|كيفك|اهلا|اهلين|مرحب).*", user_reply):
        print(welcome_message)
    else:
        room = None
        for r in home.keys():
            if r.match(user_reply):
                room = r
                break
        else:
            print("لم اعرف اين تقصد")
            continue
        is_action_done = False
        for device in home[room]:
            for action in device.actions.keys():
                matchers = device.actions[action]
                for reg_ex in matchers:
                    match_ob = re.match(reg_ex, user_reply)
                    if match_ob:
                        device.perform_action(action, match_ob)
                        is_action_done = True
                        break
        if not is_action_done:
            print("لم اعرف ماذا تقصد")

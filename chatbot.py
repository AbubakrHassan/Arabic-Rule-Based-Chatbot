import sys
from devices import Fan
import regex as re

"""
    following dictionary contains all the devices in the house,
    each device should be defined as a class which is has it's own properties, right now just assume a string
"""
home = {
    "room_a":
        [
            Fan()
        ],
    "room_b":
        [
            Fan()
        ],
    "kitchen":
        [
            Fan()
        ]
}
while True:
    user_reply = input(">> ")
    if re.match(".*(سلام|كيفك|اهلا|اهلين|مرحب)", user_reply):
        print("""مرحبًا بكم ، هذا هو النظام الاوتوماتيكي للمنزل المصمم لإدارة أجهزتك في المنزل ،
                ماذا تريدني ان افعل""")
    else:
        for device in [Fan()]:
            for action in device.actions.keys():
                matchers = device.actions[action]
                for reg_ex in matchers:
                    if re.match(reg_ex,user_reply):
                        print("YES",action)
                    else:
                        print("NO",action)
        # match = re.match("(turn on|open) the (.*) in (.*)", user_reply.lower())
        # if match:
        #     device = match.group(2)
        #     room = match.group(3)
        #     for s_room in home.keys():
        #         if s_room == room:
        #             for s_device in home[s_room]:
        #                 if s_device == device:
        #                     print("turning on the", device, "in", room)
        #                     break
        #             else:
        #                 print("no such device", device, "in room", room)
        #             break
        #     else:
        #         print("no such room", room)
        # else:
        #     print("I'm not yet designed to handle this request")

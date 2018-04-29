import sys
from devices import Fan
import regex as re
import normalizer
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
    user_reply = normalizer.normalize(user_reply)
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

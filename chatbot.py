import sys
from devices import Fan,Temperature
import regex as re
import normalizer

"""
    following dictionary contains all the devices in the house,
    each device should be defined as a class which is has it's own properties, right now just assume a string
"""
home = {
    "غرفه النوم":
        [
            Fan("غرفة النوم")
        ],
    "غرفه الطعام":
        [
            Fan("غرفة الطعام")
        ],
    "المطبخ":
        [
            Fan("المطبخ"),
            Temperature("المطبخ")
        ]
}
while True:
    user_reply = input(">> ")
    user_reply = normalizer.normalize(user_reply)
    if re.match(".*(سلام|كيفك|اهلا|اهلين|مرحب)", user_reply):
        print("""مرحبًا بك ، هذا هو النظام الاوتوماتيكي المصمم لإدارة أجهزتك في المنزل ،
                ماذا تريدني ان افعل""")
    else:
        room = None
        for r in home.keys():
            if user_reply.find(r) != -1:
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
                        is_action_done=True
                        break
        if not is_action_done:
            print("لم اعرف ماذا تقصد")

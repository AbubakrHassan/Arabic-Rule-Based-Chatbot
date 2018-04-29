import sys
import regex as re

"""
    following dictionary contains all the devices in the house,
    each device should be defined as a class which is has it's own properties, right now just assume a string
"""
home = {
    "room_a":
        [
            "light",
            "fan",
            "ac",
        ],
    "room_b":
        [
            "light",
            "fan",
            "ac",
            "heater"
        ],
    "kitchen":
        [
            "light",
            "fan",
            "oven",
        ]
}
while True:
    user_reply = input(">> ")
    if re.match("(hello|hi|hey|sup)", user_reply.lower()):
        print("""Hello there, this is the home automation system designed to manage your devices at home,
               what do you want me to do""")
    else:
        match = re.match("(turn on|open) the (.*) in (.*)", user_reply.lower())
        if match:
            device = match.group(2)
            room = match.group(3)
            for s_room in home.keys():
                if s_room == room:
                    for s_device in home[s_room]:
                        if s_device == device:
                            print("turning on the", device, "in", room)
                            break
                    else:
                        print("no such device", device, "in room", room)
                    break
            else:
                print("no such room", room)
        else:
            print("I'm not yet designed to handle this request")

class Device:
    def perform_action(self, action, match_object):
        method_name = 'action_' + action
        action_method = getattr(self, method_name, self.no_action)
        return action_method(match_object)

    def no_action(self, match_object):
        raise Exception('No action for', match_object.group())


class Fan(Device):
    def __init__(self, room=None):
        self.type = "fan"
        self.room = room
        self.actions = {
            "open":
                [
                    ".*(افتح|شغل|ادر|تشغيل|فتح|ادارة|تدوير)(.*)(مروحه)(.*)(0-6)?.*"
                ],
            "close":
                [
                    ".*(قفل|وقف|اغلق|سد|توقيف|اغلاق|تقفيل|اقفال|تغليق)(.*)(مروحه).*"
                ]
        }

    def action_open(self, match_object):
        print("تم فتح المروحة في ", self.room)
        return True

    def action_close(self, match_object):
        print("تم قفل المروحة في ", self.room)
        return True


class Temperature(Device):
    def __init__(self, room=None):
        self.type = "temp"
        self.room = room
        self.actions = {
            "read_temp":
                [
                    ".*(حراره).*"
                ]
        }

    def action_read_temp(self, match_object):
        # perform reading the tempreture
        t = 32  # place holder for the temperature
        print("درجة الحرارة في", self.room, " هي ", t)
        return True

class ClassroomAgent:
    def __init__(self):
        self.last = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
        if target == self.last:
            send = False
        else:
            send = True
        self.last = target
        return target, send

class Counter(object):
    def __init__(self,
                 name="My Counter",
                 id="00000",
                 info="",
                 previous_value=-1,
                 current_value=-1):
        self.name = name
        self.id = id
        self.info = info
        self.previous_value = previous_value
        self.current_value = current_value

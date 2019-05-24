class Pipe(object):

    def __init__(self, destination=None):
        self.number_of_inputs = 0
        self.number_of_outputs = 0
        self.destination = destination
        self._filters = list()

    def pass_through(self, log_line):
        self.number_of_inputs += 1
        if self.destination and self.should_pass(log_line):
            self.destination.pass_trhough(log_line)
            self.number_of_outputs += 1
            return True
        return False

    def should_pass(self, log_line):
        for _filter in self._filters:
            if _filter.is_matched(log_line.text):
                return False
        return True

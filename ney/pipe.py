class Pipe(object):

    def __init__(self, destination=None):
        self.id = ''
        self.number_of_inputs = 0
        self.number_of_outputs = 0
        self.destination = destination
        self._filters = list()

    def add_filter(self, _filter):
        self._filters.append(_filter)

    def pass_through(self, log_line):
        self.number_of_inputs += 1
        if self.destination and self.should_pass(log_line):
            self.destination.pass_through(log_line)
            self.number_of_outputs += 1
            return True
        return False

    def should_pass(self, log_line):
        for _filter in self._filters:
            if _filter.is_matched(log_line.text):
                return False
        return True

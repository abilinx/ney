class LogLine(object):

    def __init__(self, text):
        self.text = text
        self.tags = set()
        self.debug_track = list()


class LineBuffer(object):

    def __init__(self, size=10):
        self.size = size
        self._buffer = list()

    def push_back(self, log_line):
        if len(self._buffer) == self.size:
            self._buffer = self._buffer[1:]
        self._buffer.append(log_line)

    @property
    def buffer(self):
        return self._buffer

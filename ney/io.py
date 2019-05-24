from .logline import LogLine


class FileInputStream(object):

    def __init__(self, file_path):
        self.file = open(file_path, 'r')

    @property
    def next(self):
        return LogLine(self.file.readline())


class TerminalInputStream(object):

    @property
    def next(self):
        return input()


class FileOutputStream(object):

    def __init__(self, file_path):
        self.file = open(file_path, 'a+')

    def pass_through(self, log_line):
        self.file.write(log_line.text + '\n')


class TerminalOutputStream(object):

    def pass_through(self, log_line):
        print(log_line.text)

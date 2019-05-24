import re


class Filter(object):

    def __init__(self):
        self.number_of_checks = 0
        self.number_of_matches = 0

    def is_matched(self, text):
        raise Exception('unimplemented')


class NeverMatchingFilter(Filter):

    def is_matched(self, text):
        self.number_of_checks += 1
        return False  # never match


class AlwaysMatchingFilter(Filter):

    def is_matched(self, text):
        self.number_of_checks += 1
        self.number_of_matches += 1
        return True  # always match


class RegexFilter(Filter):

    def __init__(self, pattern):
        super().__init__()
        self.regex = re.compile(pattern)

    def is_matched(self, text):
        self.number_of_checks += 1
        if self.regex.match(text):
            self.number_of_matches += 1
            return True
        return False

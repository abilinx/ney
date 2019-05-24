class Configuration(object):

    def __init__(self):
        self.filter = r'.*bad.*'


class XMLConfiguration(Configuration):
    pass


class JSONConfiguration(Configuration):
    pass


class YMLConfiguration(Configuration):
    pass

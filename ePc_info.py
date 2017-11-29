""" pc info  is a data storage program that writes the data into a database
    auther:william kaiga
    version 0.1
"""
class Pc_info:
    """A sample Pc_info class"""

    def __init__(self, first, last, model):
        self.first = first
        self.last = last
        self.model = model

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Pc_info('{}', '{}', {})".format(self.first, self.last, self.model)

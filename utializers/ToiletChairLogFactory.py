from datetime import datetime

import logging

# this is all wrong needs to be redone.
class ToiletChairLogFactory:
    stamp = None
    file_name = None

    def __init__(self):
        self.stamp = str(datetime.now()).replace(':', '_').replace(' ', '_')

    def get_stamp(self):
        return self.stamp

    def set_file_name(self, component):
        self.file_name = self.get_stamp() + component

    def get_file_name(self):
        return self.file_name

    def get_logger(self, name, component):
        self.set_file_name(component)

        logging.basicConfig(filename=self.file_name, level=logging.DEBUG)
        l = logging.getLogger(name)

        return l
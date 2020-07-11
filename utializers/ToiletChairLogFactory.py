from datetime import datetime

import logging

# this is all wrong needs to be redone i think idk.
class ToiletChairLogFactory:
    stamp = None

    def __init__(self):
        self.stamp = str(datetime.now()).replace(':', '.').replace(' ', '_')

    def get_stamp(self):
        return self.stamp

    def get_logger(self, name, component):
        log_file_name = self.get_stamp() + component
        # logging.basicConfig(name, log_file_name,logging.DEBUG)
        logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
        l = logging.getLogger(name)

        return l
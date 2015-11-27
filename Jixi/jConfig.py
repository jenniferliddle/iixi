from ConfigParser import SafeConfigParser
import os.path

class jConfig(SafeConfigParser):

    FILENAME = os.path.expanduser("~/.jixirc")

    def __init__(self, defaults = None):

        SafeConfigParser.__init__(self)
        # read config file, set defaults and save if not found
        if not self.read(self.FILENAME):
            self.add_section('Comms')
            self.set('Comms', 'port', '')
            self.set('Comms', 'baud', '115200')

            self.add_section('Visualizer')
            self.set('Visualizer', 'program', 'tatlin')

            self.save()

    def save(self):
        f = open(self.FILENAME, 'w')
        self.write(f)
        f.close()


import os

from vmhelper.manager.a_manager import AManager


class VmwareManager(AManager):

    def __init__(self, vm_name: str):
        self.type = 'vmware'
        self.name = vm_name

    def start(self):
        if self.status(output=False):
            print('VM {} is up, nothing to do here'.format(self.name))
            return

        config = self.get_config()

        if not os.path.isfile(config.path):
            print('VM {} is not found on drive'.format(self.name))
            return

        os.popen('"{}" start "{}" nogui'.format(self.get_exe(), config.path))
        print('VM {} is now started'.format(self.name))

    def stop(self):
        if not self.status(output=False):
            print('VM {} is down, nothing to do here'.format(self.name))
            return

        config = self.get_config()

        if not os.path.isfile(config.path):
            print('VM {} is not found on drive'.format(self.name))
            return

        os.popen('"{}" stop "{}" nogui'.format(self.get_exe(), config.path))
        print('VM {} is now stopped'.format(self.name))

    def status(self, output: bool = True):
        exe = self.get_exe()
        config = self.get_config()

        stream = os.popen('"{}" list nogui'.format(exe))
        command_output = stream.read()
        rows = command_output.split('\n')

        if output:
            if config.path in rows:
                print('VM {} is up'.format(self.name))
            else:
                print('VM {} is down'.format(self.name))

        return config.path in rows

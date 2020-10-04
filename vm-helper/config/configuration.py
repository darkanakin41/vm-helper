import os

import yaml


class Configuration:

    @staticmethod
    def __base_folder__():
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    def __init__(self):
        self.config = None
        config_file = os.path.join(Configuration.__base_folder__(), "config.yaml")
        with open(config_file, "r") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        if self.config is None:
            print("Please provide the right configuration")
            exit()


class VMConfig:

    @staticmethod
    def parse(config: Configuration) -> []:
        if config.config.get('vm') is None:
            return []

        vms = {}
        for vmName in config.config.get('vm'):
            c = config.config.get('vm').get(vmName)
            vm = VMConfig(vmName, c.get('path'), c.get('type'))
            vms[vmName] = vm

        return vms

    def __init__(self, name: str, path: str, vmType: str):
        self.name = name
        self.path = path
        self.type = vmType

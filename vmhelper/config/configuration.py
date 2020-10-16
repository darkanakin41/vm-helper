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
        for vm_name in config.config.get('vm'):
            c = config.config.get('vm').get(vm_name)
            vm = VMConfig(vm_name,
                          c.get('path'),
                          c.get('type'),
                          c.get('hostname'),
                          c.get('port'),
                          c.get('ssh_username'),
                          c.get('ssh_password'),
                          )
            vms[vm_name] = vm

        return vms

    def __init__(self,
                 name: str,
                 path: str,
                 vm_type: str,
                 hostname: str = None,
                 port: int = None,
                 ssh_username: str = None,
                 ssh_password: str = None):
        self.name = name
        self.path = path
        self.type = vm_type
        self.hostname = hostname
        self.port = port
        self.ssh_username = ssh_username
        self.ssh_password = ssh_password
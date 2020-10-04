from abc import ABC, abstractmethod

from config import configuration, vms
from config.configuration import VMConfig


class AManager(ABC):
    type: str
    name: str

    def get_exe(self):
        return configuration.config.get(self.type).get('exe')

    def get_config(self) -> VMConfig:
        return vms.get(self.name)

    def run(self, action: str):
        if action == "status":
            self.status()
            return
        if action == "start":
            self.start()
            return
        if action == "stop":
            self.stop()
            return
        print('Unknown action')
        exit(1)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass

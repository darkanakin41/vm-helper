from vmhelper.manager.vmware_manager import VmwareManager
from vmhelper.manager.a_manager import AManager

class Manager:

    @staticmethod
    def get_manager(vm_type: str, vm_name: str) -> AManager:
        if vm_type == 'vmware':
            return VmwareManager(vm_name)

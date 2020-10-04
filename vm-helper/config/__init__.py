from .configuration import Configuration, VMConfig

configuration = Configuration()
vms = VMConfig.parse(configuration)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from typing import Optional, Sequence

from vmhelper.config import vms
from vmhelper.manager.manager import Manager
from vmhelper.utils.ssh import try_ssh

parser = argparse.ArgumentParser()
parser.add_argument("name", help="The name of the project you want to create", type=str)
parser.add_argument("action", help="The action to launch (status, start, stop)", type=str)


def main(args: Optional[Sequence[str]] = None):
    argument = parser.parse_args(args)
    vm_config = vms.get(argument.name)

    if vm_config is None:
        print('Unknown VM')
        exit(1)

    manager = Manager.get_manager(vm_config.type, vm_config.name)
    manager.run(action=argument.action)

    if vm_config.hostname:
        try_ssh(hostname=vm_config.hostname,
                port=vm_config.port,
                username=vm_config.ssh_username,
                password=vm_config.ssh_password)


def console_script():  # pragma: no cover
    """
    Console script entrypoint
    """
    main()

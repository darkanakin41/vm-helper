darkanakin41/vm-helper
===

This project is a toolbox to simplify management of virtual machine through CLI. 

Based on config.yaml, it allows you to check status of vms and start and stop thems.

# Development
* Install requirements : 
```bash
pip install -r requirements-dev.txt
```
# Usage
```bash
python vm-helper --help
usage: vm-helper [-h] name action

positional arguments:
  name        The name of the project you want to create
  action      The action to launch (status, start, stop)

optional arguments:
  -h, --help  show this help message and exit
```

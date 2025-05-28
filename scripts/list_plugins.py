import os
import subprocess


command = "ansible-playbook -v -i ./ansible/inventory.txt ./ansible/list_plugins.yml"
print(command)
subprocess.call(command, shell=True)

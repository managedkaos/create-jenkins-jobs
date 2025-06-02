import os
import subprocess
import challenge_settings as settings
cwd = os.getcwd()


for team in settings.teams:
    command = "ansible-playbook -v -i ./ansible/inventory.txt ./ansible/move_jobs.yml --extra-vars 'job_regex="+team+"-.* folder_name="+team+"'"
    print(command)
    subprocess.call(command, shell=True)

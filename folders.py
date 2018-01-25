import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/folder.xml") as config_file:
    config = config_file.read()

for team in settings.teams:
    try:
        j.job_create(team, config)
        for job in settings.jobs:
    except:
        print("Bummer! :/ :D")

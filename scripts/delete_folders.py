import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/folders/base/config.xml") as config_file:
    config = config_file.read()

for team in settings.teams:
    if j.job_exists(team):
        try:
            print("\tDeleting folder: %s" % team)
            j.job_delete(team)
        except:
            print("\tCouldn't delete folder: %s" % team)

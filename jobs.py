import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/job.xml") as config_file:
    config = config_file.read()

for team in settings.teams:
    for job in settings.jobs:
        j.job_create(team + "-" + job, config)

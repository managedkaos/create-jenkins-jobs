import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/jobs/hourly/config.xml") as config_file:
    config = config_file.read()

for team in settings.teams:
    for job in settings.jobs:
        target = team+"-"+job

        if j.job_exists(target):
            print("\tJob exists; skipping: %s" % target)
        else:
            print("\tCreating job: %s" % target)
            j.job_create(team + "-" + job, config)

"""
Build: Builds every job for every team defined in settings
"""
import os
from jenkins import Jenkins, JenkinsError
import settings

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for team in settings.teams:
    for job in settings.jobs:
        target = team+"-"+job

        if j.job_exists(target):
            try:
                print("\tBuiding job: %s" % target)
                j.job_build(target)
            except JenkinsError:
                print("\tCouldn't build job: %s" % target)

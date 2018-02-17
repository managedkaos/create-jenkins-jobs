import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for team in settings.teams:
    if j.job_exists(team):
        try:
            print("\tDeleting job: %s" % team)
            j.job_delete(team)
        except JenkinsError:
            print("\tCouldn't delete job: %s" % team)
    else:
        print("\tJob doesn't exist; skipping: %s" % team)

    for job in settings.jobs:
        target = team+"-"+job

        if j.job_exists(target):
            try:
                print("\tDeleting job: %s" % target)
                j.job_delete(target)
            except JenkinsError:
                print("\tCouldn't delete job: %s" % target)
        else:
            print("\tJob doesn't exist; skipping: %s" % target)

import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for team in settings.teams:
    for job in settings.jobs:
        try:
            j.job_delete(team + "-" + job)
        except JenkinsError:
            print("Error :P")

for job in settings.jobs:
    try:    
        j.view_delete(job)
    except JenkinsError:
        print("Oops :D")


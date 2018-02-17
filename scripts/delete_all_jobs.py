import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for job in j.jobs: 
    try:
        print("\tDeleting job: %s" % team)
        j.job_delete(team)
    except JenkinsError:
        print("\tCouldn't delete job: %s" % team)

for view in j.views:
    if view.name == 'all': 
        continue

    try:
        print("\tDeleting view: %s" % job)
        j.view_delete(job)
    except JenkinsError:
        print("\tCouldn't delete view: %s" % job)

import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for job in j.jobs: 
    try:
        print("\tDeleting job: %s" % job)
        j.job_delete(job)
    except JenkinsError:
        print("\tCouldn't delete job: %s" % job)

for view in j.views:
    if view.name == 'all': 
        continue

    try:
        print("\tDeleting view: %s" % view)
        j.view_delete(view)
    except JenkinsError:
        print("\tCouldn't delete view: %s" % view)

import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
for job in settings.jobs:
    if j.view_exists(job):
        try:
            print("\tDeleting view: %s" % job)
            j.view_delete(job)
        except JenkinsError:
            print("\tCouldn't delete view: %s" % job)

import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
for job in settings.jobs:
    with open("./xml/views/"+job.lower()+"/config.xml") as config_file:
        if j.view_exists(job):
            print("\tView exists; skipping: %s" % job)
        else:
            print("\tCreating view: %s" % job)
            j.view_create(job, config_file.read())

import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
for job in settings.jobs:
    with open("./xml/"+job.lower()+".view.xml") as config_file:
        j.view_create(job, config_file.read())

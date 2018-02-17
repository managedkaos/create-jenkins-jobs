import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/apache-ivy-base-job.xml") as config_file:
    config = config_file.read()

j.job_create("apache-ivy", config)

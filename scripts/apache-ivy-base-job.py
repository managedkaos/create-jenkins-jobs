import os
import settings
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/jobs/apache-ivy-base-job/config.xml") as config_file:
    config = config_file.read()

if j.job_exists("apache-ivy"):
    print("\tapache-ivy job exists. skipping...")
else:
    try:
        print("\tCreating apache-ivy-base-job...")
        j.job_create("apache-ivy", config)
    except JenkinsError:
        print("\tCouldn't create the job")
        

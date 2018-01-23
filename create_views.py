import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
for job in ['BUILD', 'TEST', 'DEPLOY']:
    with open("./xml/"+job.lower()+".view.xml") as config_file:
        j.view_create(job+"-jobs", config_file.read())

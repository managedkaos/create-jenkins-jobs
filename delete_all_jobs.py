import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

for job in j.jobs: 
    job.delete() 

for view in j.views:
    if view.name == 'all': 
        continue
    view.delete()


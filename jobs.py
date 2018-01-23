import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./xml/job.xml") as config_file:
    config = config_file.read()

    with open("./teams.txt") as teams_file:
        for team in teams_file:
            team = team.strip()

            for job in ['BUILD', 'TEST', 'DEPLOY']:
                j.job_create(team + "-" + job, config)

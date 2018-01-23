import os
from jenkins import Jenkins, JenkinsError

# get a handle for the jenkins server
j = Jenkins(os.environ['ENDPOINT'], os.environ['USERNAME'], os.environ['PASSWORD'])

# open the config.xml
with open("./teams.txt") as teams_file:
    for team in teams_file:
        team = team.strip()
        print(team)

        for job in ['BUILD', 'TEST', 'DEPLOY']:
            j.job_delete(team + "-" + job)

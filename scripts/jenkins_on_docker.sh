#!/usr/bin/env bash
export NAME=${1:-jenkins-compose}

if [ $(ps -elf | grep docker | wc -l) -gt 0 ];
then
    echo -n "Waiting for Jenkins process to start ."
    until [ $(curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://127.0.0.1:8080) -eq 403 ];
    do
        echo -n '.';
        sleep 1;
    done
    ADMIN_PASS=$(docker exec ${NAME} cat /var/jenkins_home/secrets/initialAdminPassword)
    echo
    echo "Jenkins URL:"
    echo "    http://localhost:8080"
    echo
    echo "Admin password:"
    echo "    ${ADMIN_PASS}"
    echo
    echo "Admin Token:"
    echo "    ${ADMIN_TOKEN}"
    echo
    echo "To run commands in the container as root:"
    echo "    docker exec --user root -it ${NAME} bash"
else
    echo "Can't find any docker processes.  Is Docker really running? :("
fi

# update-build.sh
# Updates a docker image using Jenkins (or whatever) parameters
# This is designed for the use case of per-environment docker image names
# e.g. $JENKINS_BUILD_ENV would be "staging"
# So the full image name would be like: "megacorporation/ourwebapp-staging"

JENKINS_BUILD_ENV="$1"
echo ">>> Running as environment: $JENKINS_BUILD_ENV"

echo '>>> Get old container id'
CID=$(sudo docker ps | grep "someuniqueimagename" | awk '{print $1}')
echo $CID

echo '>>> Pulling updated image'
sudo docker login -u $DOCKER_INDEX_USER -e $DOCKER_INDEX_EMAIL -p $DOCKER_INDEX_PASSWORD
sudo docker pull $COMPANY_NAME/$APP_NAME-$JENKINS_BUILD_ENV

echo '>>> Stopping old container'
if [ "$CID" != "" ];
then
  sudo docker stop $CID
fi

echo '>>> Starting new container'
docker run -d -p 9000:80 -p 9443:443 -v /dockerized/app/logs:/var/log/logstash -w /usr/bin -e "ENVIRONMENT=$JENKINS_BUILD_ENV" -t $COMPANY_NAME/$APP_NAME-$JENKINS_BUILD_ENV python server.py

echo '>>> Cleaning up containers'
sudo docker ps -a | grep "Exit" | awk '{print $1}' | while read -r id ; do
  sudo docker rm $id
  echo '...success'
done

echo '>>> Cleaning up images'
sudo docker images | grep "^<none>" | head -n 1 | awk 'BEGIN { FS = "[ \t]+" } { print $3 }'  | while read -r id ; do
  sudo docker rmi $id
  echo '...success'
done

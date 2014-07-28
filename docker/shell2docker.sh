# Drop into a docker image using nsenter.
# This is only really useful as a script when you have a single unique docker image running that
# uses $IMAGE_NAME in part of it's image name.
# TODO: Extending it to accept a parameter would make this more extensible.

PID=$(docker inspect --format '{{.State.Pid}}' $(docker ps | grep $IMAGE_NAME | awk '{print $1}'))
nsenter --target $PID --mount --uts --ipc --net --pid

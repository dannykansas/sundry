# Check the status of dd when it's taking forever
# Must sudo

PID=$(pgrep -l '^dd$' | awk '{print $1}')
kill -USR1 $PID 

i=0 # i controls which thread to run test on
while read test; do
    while true; do
	CRUMB=$(curl -k -s "http://$JENKINSIP:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,\":\",//crumb)" --user "$USERNAME":"$USERPASS")
	curl -X GET "http://$JENKINSIP:8080/job/$TESTSUITE-thread$i/lastBuild/api/xml?depth=1&token=$APITOKEN" -k -H "$CRUMB" --user "$USERNAME":"$USERPASS" > thread.json
	THREAD=$(grep -c '<building>false</building>' thread.json)
	if [ "$THREAD" = "1" ]; then
	    echo "Thread $i Available"
	    sleep 1
	    break
	else
	    echo "Thread $i Not Available"
	    sleep 1
	    i=$(($i + 1))
	    i=$(($i % 8)) # assumes 8 threads available
	fi
	sleep 1
    done
    CRUMB=$(curl -k -s "http://$JENKINSIP:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,\":\",//crumb)" --user "$USERNAME":"$USERPASS")
    curl -X POST "http://$JENKINSIP:8080/job/$TESTSUITE-thread$i/buildWithParameters?delay=0sec&TESTCASE=$test&token=$APITOKEN" -k -H "$CRUMB" --user "$USERNAME":"$USERPASS"
    echo "Test $TESTCASE sent to Thread $i"
    sleep 1
done <"$TESTSUITE.conf"

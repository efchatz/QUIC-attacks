while true
do
   sudo seq 1 100 | timeout 5s xargs -n1 -P100 python3 examples/http3_client.py --zero-rtt -k URL
done

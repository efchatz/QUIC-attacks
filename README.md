# QUIC-attacks

## Download and install aioquic
1. git clone https://github.com/aiortc/aioquic
2. sudo apt install libssl-dev
3. cd aioquic
4. pip install -e .
5. pip install asgiref dnslib httpbin starlette wsproto
6. python3 setup.py install
7. add the quic-loris.sh file to the aioquic dir
8. initite the attack

Change the URL parameter to the one of the target. Note that based on the capabilities of the targeted server, different values maybe needed for timeout and sleep commands. The same occur the seq and xargs values that are now at 100.

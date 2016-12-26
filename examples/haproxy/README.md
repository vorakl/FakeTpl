# The example of docker image based on an oficial Nginx's image

## Build

Run this command from the directory with the example

```bash
docker build -t haproxy-test .
```

## Start the container

This HAProxy is gonna use host's network.
In the BACKEND array we've set 3 backend servers with different names and addresses.
All logs could be found in the host's systemd journal.

```bash
input> docker run -d --name haproxy-test -e BACKEND="([web1]=192.168.1.10 [web2]=192.168.2.10 [web3]=192.168.3.10)" --net=host -v /run/systemd/journal/:/host-journal haproxy-test

input> curl http://localhost/

input> docker rm -f haproxy-test
```

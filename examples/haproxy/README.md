# The example of auto-configuring of HAProxy at run-time 

## Build

Run this command from the directory with the example

```bash
docker build -t haproxy-test .
```

## Start the container

This HAProxy is going to use host's network.
In the BACKEND array we've specified 3 backend servers with different names and addresses.
All logs could be found in the host's systemd journal.

Let's start the container, check logs, access the port and remove the container:

```bash
$ docker run -d --name haproxy-test -e BACKEND="([web1]=192.168.1.10 [web2]=192.168.2.10 [web3]=192.168.3.10)" --net=host -v /run/systemd/journal/:/host-journal haproxy-test

$ sudo journalctl -b -f _COMM=haproxy

$ curl http://localhost/

$ docker rm -f haproxy-test
```

# The example of docker image based on an official Nginx's image

## Build

Run this command from the directory with the example

```bash
docker build -t nginx-test .
```

## Start the container without changing variables

```bash
input> docker run -d --name nginx-test -p 80:80 nginx-test
input> curl http://localhost/

output>

<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to f542049bd6d8</h1>
        <div>My name is: <b>default</b></div>
        <div>Random number: <b>22654</b></div>
    </body>
</html>

input> docker rm -f nginx-test
```

## Start the container and change the variable

```bash
input> docker run -d --name nginx-test -e MYNAME=Oleksii -p 80:80 nginx-test
input> curl http://localhost/

output>

<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to 87d141916e04</h1>
        <div>My name is: <b>Oleksii</b></div>
        <div>Random number: <b>27729</b></div>
    </body>
</html>

input> docker rm -f nginx-test
```


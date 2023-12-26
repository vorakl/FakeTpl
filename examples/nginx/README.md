# The example of generating of an Index page using environment variables

## Build

Run this command from the directory with the example

```bash
docker build -t nginx-test .
```

## Start the container without changing variables

```bash
$ docker run -d --name nginx-test -p 80:80 nginx-test

$ curl http://localhost/
<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to f542049bd6d8</h1>
        <div>My name is: <b>default</b></div>
        <div>Random number: <b>22654</b></div>
    </body>
</html>

$ docker rm -f nginx-test
```

## Start the container and change the variable

```bash
$ docker run -d --name nginx-test -e MYNAME=vorakl -p 80:80 nginx-test

$ curl http://localhost/
<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to 87d141916e04</h1>
        <div>My name is: <b>vorakl</b></div>
        <div>Random number: <b>27729</b></div>
    </body>
</html>

$ docker rm -f nginx-test
```


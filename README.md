[![Build Status](https://api.travis-ci.org/vorakl/FakeTpl.png)](https://travis-ci.org/vorakl/FakeTpl)

# FakeTpl - the fake template engine in sh-compatible shells

* [What is it?](#what-is-it)
* [How to get started?](#how-to-get-started)
   * [...as a one-liner.](#as-a-one-liner)
   * [...as an included script.](#as-an-included-script)
   * [Intallation into a docker image (based on CentOS)](#intallation-into-a-docker-image-based-on-centos)
   * [Intallation into a docker image (based on Alpine)](#intallation-into-a-docker-image-based-on-alpine)
* [Examples](#examples)
* [Technical details](#technical-details)
* [Why was it created?](#why-was-it-created)
* [Are there any other similar solutions?](#are-there-any-other-similar-solutions)

## What is it?

It's not a real template engine or a complete program.
This is a working solution for a simple idea of using shell inlines as templates.

Of course, it won't be convenient to use this sort of "templates" with files where are a lot of quotation marks or other expressions sensitive to the shell syntax, because it leads to escaping all these special characters. But, at the same time it is convenient for adding templates to any common configuration files and other similar cases, for which actually `faketpl` was created.

The solution is done as a little function which is called `faketpl`. It's compatible with many sh-like shells because uses only basic instructions, which can be included in any script, either as a one-liner or an external script (after downloading from the Internet). Faketpl was tested in Bourne shell (sh), bash, zsh and ash (Busybox).

Being so simple in terms of the idea and realization, it's, in most cases, much more powerful than real template engines! It allows to use most features of a shell interpreter as templates with the only limitation of writing them in one line. That means, there are conditions, loops, an output result of executing commands, content of files, etc and the only real dependency is a shell.

To eliminate any security issues related to direct executing commands, this solution is meant to be used primarily in the isolated container's environment like Docker and especially for bootstrapping them.

## How to get started?

Being compatible with many shells at the same time, faketpl cannot use one of them by default. But it's not a limitation. It's a freedom of a choice. Just "include" it into your script which is written in any sh-like language and start using as a function. There are two options: include as an one-liner or as a script from the Internet.

### ...as a one-liner.

This is the simplest and the most reliable one. It doesn't require an internet connection but will be hard-coded once it's added. That defines a use case: when you need to integrate the fake template engine with some existing script/environment once and then use it without any requirements. So, just add this string in your shell code:

```bash
faketpl() { export IFS=''; while read -r _line; do eval echo \"${_line}\"; done; }
```

Yep, that's only one line, really. Nothing more! :)
Then, send a text with templates to stdin like here

```bash
(echo -e 'Workers $(grep processor /proc/cpuinfo | wc -l)\nVirtualHost $(cat /proc/sys/kernel/hostname):${RANDOM}\nUsername ${SRV_NAME:-www}' | faketpl)
```

If this command is run in a basic official docker container with Apline Linux with only Busybox on the board, then as a result, you'll see something like this

```bash
Workers 4
VirtualHost 1a614d65b09c:10915
Username www
```

That could be a part of some sort of dynamic config file of a web-server. Of course, more useful examples can be found below ;) And pay attention on using bounding parentheses! They are always needed. The explanation "why?" will be given a bit later.

### ...as an included script.

The use case for this option is to use it in automated build environments, when you build an application from scratch. For example, while your pipeline builds a new docker image with some application, faketpl can be downloaded from the Internet by the instruction from a Dockerfile and then be invoked at run-time from the Entrypoint to transform templates to real configuration files, or html pages, or whatever else. As I've mentioned before, to support several backends (shells) at the same time, faketpl can be used only after "sourcing" it in the script and then being used as a function. 
So, let's download the script from the Github and check sha256 sum.
You DON'T need to set an execution permission!

For a Busybox backend, run as root

```bash
wget -qO /usr/bin/faketpl http://vorakl.github.io/FakeTpl/faketpl && \
( cd /usr/bin && wget -qO - http://vorakl.github.io/FakeTpl/faketpl.sha256 | sha256sum -c )
```

or using curl, run as root

```bash
curl -sSLfo /usr/bin/faketpl http://vorakl.github.io/FakeTpl/faketpl && \
( cd /usr/bin && curl -sSLf http://vorakl.github.io/FakeTpl/faketpl.sha256 | sha256sum -c )
```

Then, include it in the script by `source` or `.` command without specifying a full path (because it's already in the $PATH, in one of the standart directory for binaries)

```bash
source faketpl
```

and then, set some values for variables from our "template" file. To render the file, just send it to the function and write an output to a real file:

```bash
export MYNAME=Oleksii
(faketpl < index.html.ftpl > index.html)
```
If the `index.html.ftpl` has this text:

```bash
<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to $(cat /proc/sys/kernel/hostname)</h1>
        <div>My name is: <b>${MYNAME:-default}</b></div>
        <div>Random number: <b>${RANDOM}</b></div>
    </body>
</html>
```

then, `index.html` will have this result

```bash
<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to marche</h1>
        <div>My name is: <b>Oleksii</b></div>
        <div>Random number: <b>20812</b></div>
    </body>
</html>
```

### Intallation into a docker image (based on CentOS)

```bash
FROM centos:latest

RUN curl -sSLfo /usr/bin/faketpl http://vorakl.github.io/FakeTpl/faketpl && \
    ( cd /usr/bin && curl -sSLf http://vorakl.github.io/FakeTpl/faketpl.sha256 | sha256sum -c )

```

### Intallation into a docker image (based on Alpine)

```bash
FROM alpine:latest

RUN wget -qP /usr/bin/ http://vorakl.github.io/FakeTpl/faketpl && \
    ( cd /usr/bin && wget -qO - http://vorakl.github.io/FakeTpl/faketpl.sha256 | sha256sum -c )
```

## Examples

* To get more familiar with basic technics I suggest to try [one-liners](https://github.com/vorakl/FakeTpl/tree/master/examples/one-liners) first
* The example of [auto-configuring of HAProxy](https://github.com/vorakl/FakeTpl/tree/master/examples/haproxy) at run-time
* The example of [generating of an Index page](https://github.com/vorakl/FakeTpl/tree/master/examples/nginx) using environment variables

## Technical details

Basically, it's as simple as go line by line trough the whole stream from stdin and print them out after the evaluation. That means if the shell can recognize some expressions they will be evaluated before printing out. To make this reading possible, the value of IFS variable is changed and this can screwed up you current running environment. That's why it's highly important to do all transformation in the sub-shell by putting the whole command in the parentheses. Another consequence is to use all desirable "templates" within one line. That's all. Only two requirement: to run inside `( )` and to write all expressions in one line.


## Why was it created?

I was looking for such kind solution for awhile and the reason is "12 Factors" of Cloud Native Applications with its 3rd statment [Store config in the environment](https://12factor.net/config). It basically says that an application has to be delivered with the configuration in most generic form, to make it's ready to be run in any specific environment without rebuilding or modifications of the base "package". It has to be done by supplying a configuration for a particular instance (copy of an application) for a particular environment in terms of environment variables. For example, if some orchestration system runs a container with an application, it supplies all needed configuration as environment variables. In case of Docker, it would look like

```bash
docker run -d -e RUN_ENV=dev -e UPLOAD_HOST=1.2.3.4 -e MY_DOMAIN=domain.com some-image-with-app
```

That basically means that something inside the container has to modify the configuration of an application, at a boot time,
to make it applicable for the current running environment. This can be achived easyly if the application is developed in-house and it supports such kind of behavior. For most popular programming languages there are available a lot of libraries with different template engines. But what if it doesn't support templates or there is a need to run 3rd party application on which we don't have any influence?

Actually, this is the most common case when you need to run in the container on the Cloud some arbitrary application which is delivered as a unified image. If this application has a configuration stored in text files, then one of possible and convenient way to support 3rd statment of the "12 Factors" is to deliver the application with the most generic form of configuration using templates. Then, at run-time, just finalize configuration based on supplied environment variables by using some template engine.

Of course, there are dozens of different template engines for many languages. It's not a big deal to install some scripting language, like Python, with template library and write a simple script. But! With containers the size matters ;) There is always a need to have a minimal image, without any unnecessary tools and the Shell is that reasonable minimum base which almost all containers have. Yes, there are templates engines in pure Bash but usually they support only simple traslation of variables (arrays) to their values, plus loops, but nothing more. So, you'll have to use some "dialect" of templates anyway. Honestly, this last option works pretty well. You can build a container image based on Alpine Linux with only Busybox inside, add one of a shell template engine and that's all. But suddenly, I came across a quite nice idea which opened a door to the full power of the shell that can be used as a sort of templates. Without any extra packages or additional syntax. Just pure shell one-liner in-lines and a simple function which tranlates them to values.

## Are there any other similar solutions?

Just a few examples... 

The idea, which made it possible to create faketpl, was found in [alterway/docker-keepalived repo](https://github.com/alterway/docker-keepalived). That was exactly what I needed and was looking for. At the same time I didn't like the implementation. In my opinion, it has a big drawback because it's limited by the size of files. But it wasn't a goal for the guys and their solution works pretty good for them. Their implementation puts the whole file in the command line before the evaluation and that's why it's limited and depends on the system. Anyway, it won't allow to deal with files bigger than `getconf ARG_MAX` bytes. Although, I was needed a scalable solution.

In the repo with [the official docker image of Nginx](https://github.com/nginxinc/docker-nginx) maintainers added a similar functionality of configuring Nginx using simple variables as templates. For this purpose they use `envsubst` tool from the `gettext` package. It works fine but supports substituting only simple variables like ${var}. There is no possibility to set default values like ${var:-defult} or use other features of a shell.

The Authors of [HAProxy](http://www.haproxy.org/) included the same feature directly in the application. There is an ability to use environment variables inside the configuration files without a need to run any external tools. That's really useful because you can inject them from the file before running the main process of HAProxy but it's limited only by using "flat" variables. There are no arrays, loops, etc. It's impossile, for instance, to build the whole config file with all backends from a little template. The example of how to do this using faketpl can be found below.


##### Version: v1.1.2
##### Copyright (c) 2016 by Oleksii Tsvietnov, me@vorakl.name

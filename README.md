# FakeTpl - a fake template engine in sh-compatible shells

Table of Contents
=================

* [What is it?](#what-is-it)
* [How to get started?](#how-to-get-started)
* [Where is it used?](#where-is-it-used)
* [Why was it created?](#why-was-it-created)
* [Technical details](#technical-details)
* [Examples](#examples)

## What is it?

It's not a real template engine or a compleate program.
This is a working solution for a simple idea of using shell inlines as a templates.

The solutions is done as a little function which is called `faketpl`. It's compatible with many sh-like shells because uses only basic instructions, which can be included in any script, either as a one-liner or an external script (after downloading from the Internet). Faketpl was tested in Bourne shell (sh), bash, zsh and ash (Busybox).

Being so simple in terms of the idea and realization, it's, in most cases, much more powerful than real template engines! It allows to use most features of a shell interpreter as templates with the only limitation of writing them in one line. That means, there are conditions, loops, a result of executing commands, content of files, etc and the only real dependency is a shell.

## How to get started?

Being compatible with many shells at the same time, faketpl cannot use one of them by default. But it's not a limitation. It's a freedom of a choice. Just "include" it into your script which is written in any sh-like language and start using as a function. There are two options: include as an one-liner or as a script from the Internet.

### As a one-liner.

This is a simplest and the most reliable one. It doesn't require an internet connection but will be hard-coded once it's added. That defines a use case: when you need to integrate the fake engine with some existing script/environment once and use then without any requirements. 
So, just put this string in your shell code:

```bash
faketpl() { export IFS=''; while read -r _line; do eval echo \"${_line}\"; done; }
```

Yep, that's only one line, really. Nothing more.
Then, send a text with templates to stdin like:

```bash
(echo -e "Workers $(grep processor /proc/cpuinfo | wc -l)\nVirtualHost $(cat /proc/sys/kernel/hostname):${RANDOM}\nUsername ${SRV_NAME:-www}" | faketpl)
```

If this command is run in a basic official docker container with Apline linux with only Busybox on the board, then as a result, you'll see something like this

```bash
Workers 4
VirtualHost 1a614d65b09c:10915
Username www
```

That could be a config file of a web-server, for example. Of course, more useful examples can be found below ;) And pay attention on using parentheses! They are always needed. The explanation "why?" will be given a bit later.

### As an included script.

The use case for this option is to use in automated build environments, when you build an application from scratch. For example, while your pipeline builds a new docker image with some application, faketpl can be downloaded from the Internet by the instruction from a Dockerfile and then be invoked at run-time from the Entrypoint to transform templates to real configuration files, or html pages, or whatever else. As I've mentioned before, to support several backends (shells) at the same time, faketpl can be used only after "sourcing" it in the script and then being invoked as a function. 
So, let's download the script from the Github (faketpl.vorakl.name is an alias to the Github).

For a Busybox backend, as root:

```bash
wget -qO /usr/bin/faketpl.sh http://faketpl.vorakl.name/faketpl.sh
```

or using curl, as root:

```bash
curl -sSLfo /usr/bin/faketpl.sh http://faketpl.vorakl.name/faketpl.sh
```

Then, include it in the script by `source` or `.` command without specifying a full path:

```bash
source faketpl.sh
```

and then, set some values for variables in our "template" file. To render the file, just send to the function this text with "templates" and write an output to a real file:

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

## Where is it used?

## Why was it created?

## Technical details?

## Examples


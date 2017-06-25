# One-liners

I assume that you've installed FakeTpl some how as was described [here](https://github.com/vorakl/FakeTpl#how-to-get-started)
To try all these examples, let's 'source' it:

```bash
source faketpl
```

And now, everything is ready to go ;)

## default values

```bash
$ echo '[${MYVAR:-default}]' | faketpl
[default]
```

```bash
$ MYVAR=something; echo '[${MYVAR:-default}]' | faketpl
[something]
```

## if some variable wasn't set, then raise an error

To raise an error we need `set -u`

```bash
$ (set -u; faketpl <<< '${ASD}' 2>/dev/null) || echo "Error: ASD variable has to be set"
Error: ASD variable has to be set
```
or

```bash
$ (set -u; echo '${ASD}' | faketpl 2>/dev/null) || echo "Error: ASD variable has to be set"
Error: ASD variable has to be set
```
or

```bash
$ (set -u; faketpl < some.conf.ftpl > some.conf 2> /dev/null) || echo "Error: ASD variable has to be set"
Error: ASD variable has to be set
```

## how to use arrays?

To use arrays we need a shell that supports them, like BASH. Don't forget to declare an array as `declare -a VAR` first, especially if it's an associative array as `declare -A VAR`.

```bash
$ declare -A FRIENDS

$ FRIENDS=([Max]="Krakow" [Alex]="Rome")

$ faketpl << -=END=-
> I came from $(hostname)
> $(IFS=' '; for name in $(tr ' ' '\n' <<< ${!FRIENDS[@]} | sort -n | tr '\n' ' '); do echo "${name} came from ${FRIENDS[${name}]}"; done)
> -=END=-

I came from marche
Alex came from Rome
Max came from Krakow
```

## go through all sub-directories and render all templates

Let's assume we have a path tree like

```bash
$ tree ftpls
ftpls
├── 1
│   ├── 2
│   │   └── index.html.ftpl
│   └── index.html.ftpl
└── index.html.ftpl
```

to get real files just run

```bash
source faketpl
find ftpls/ -name "*.ftpl" | \
while read fn; do \
    faketpl < ${fn} > ${fn%%.ftpl}; \
done
```

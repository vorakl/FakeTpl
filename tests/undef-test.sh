#!/usr/bin/env roundup

source ../faketpl

describe "Checks if it fails on undefined variables"

before() {
    cd ..
}

after() {
    cd -
}

it_gets_failed_on_undef_pipe() {
    ( set -u; echo '$var' | faketpl ) || e=1
    test ${e} -eq 1
}

it_gets_failed_on_undef_stdin() {
    ( set -u; faketpl <<< '$var' ) || e=1
    test ${e} -eq 1
}

it_gets_failed_on_undef_file() {
    bash -c 'set -u; source faketpl; faketpl < <(echo "\$var")' || e=1
    test ${e} -eq 1
}

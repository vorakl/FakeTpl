#!/usr/bin/env roundup

describe "Checks different ways to invoke"

before() {
    cd ..
}

after() {
    cd -
}

it_gets_data_from_pipe() {
    output=$(bash -c 'source faketpl; self="FakeTpl"; echo "I am \$self" | faketpl')
    test "${output}" = "I am FakeTpl"
}

it_gets_data_from_stdin() {
    output=$(bash -c 'source faketpl; self="FakeTpl"; faketpl <<< "I am \$self"')
    test "${output}" = "I am FakeTpl"
}

it_gets_data_from_file() {
    output=$(bash -c 'source faketpl; self="FakeTpl"; faketpl < <(echo "I am \$self")')
    test "${output}" = "I am FakeTpl"
}

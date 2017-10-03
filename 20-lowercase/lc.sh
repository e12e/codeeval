#!/usr/bin/env bash
#
# Challenge is to translate uppercase to lowercase -
# clearly a job for "tr"/"bash"...

cat "${1}" | tr A-Z a-z

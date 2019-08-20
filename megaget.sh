#!/bin/bash
set -e

SCRIPT_PATH=$(dirname $(realpath -s $0))

source $SCRIPT_PATH/config.sh

megaget -u $USER --no-ask-password -p $PASS $@

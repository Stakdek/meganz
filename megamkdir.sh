#!/bin/bash
set -e

source config.sh

megamkdir -u $USER --no-ask-password -p $PASS $@

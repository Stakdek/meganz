#!/bin/bash
set -e

source config.sh

megals -u $USER --no-ask-password -p $PASS $@

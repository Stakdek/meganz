#!/bin/bash
set -e

source config.sh

megarm -u $USER --no-ask-password -p $PASS $@

#!/bin/bash
set -e

source config.sh

megadl -u $USER --no-ask-password -p $PASS $@

#!/bin/bash
set -e

source config.sh

megadf -u $USER --no-ask-password -p $PASS $@

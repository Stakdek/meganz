#!/bin/bash
set -e

source config.sh

megaput -u $USER --no-ask-password -p $PASS $@

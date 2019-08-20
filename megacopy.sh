#!/bin/bash
set -e

source config.sh

megacopy -u $USER --no-ask-password -p $PASS $@

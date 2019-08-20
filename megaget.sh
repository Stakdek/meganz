#!/bin/bash
set -e

source config.sh

megaget -u $USER --no-ask-password -p $PASS

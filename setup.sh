#!/bin/bash

virtualenv --python $(which python3) .app
source .app/bin/activate
python main.py

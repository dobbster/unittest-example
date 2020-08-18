#!/bin/bash

pip3 install virtualenv
virtualenv --python $(which python3) .app
source .app/bin/activate
python main.py

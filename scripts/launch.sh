#!/usr/bin/env bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python3 src/main.py
#!/bin/bash

while inotifywait -e close_write main.py; do ./env/bin/python3 main.py; done

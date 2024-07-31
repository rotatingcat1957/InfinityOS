#!/bin/bash

if [ ! -f "user_data/password.txt" ]; then
    if [ ! -f "user_data/username.txt" ]; then
        ./run_me_first.py
    fi
else
    ./main.py
fi

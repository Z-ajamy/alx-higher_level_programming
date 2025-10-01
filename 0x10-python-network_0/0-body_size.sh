#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -eq 1 ]; then
    curl -s "$1" | wc -m
fi

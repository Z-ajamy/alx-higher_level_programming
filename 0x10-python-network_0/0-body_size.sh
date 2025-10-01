#!/bin/bash
# Check if exactly one argument is provided
curl -s "$1" | wc -m

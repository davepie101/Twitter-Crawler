#!/bin/sh
mkdir data
mkdir parsed

echo "Streaming twitter data to /data/twitter_data*.txt"
python3 crawler.py
echo "Parsing data"
python3 parse.py
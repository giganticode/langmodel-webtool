#!/bin/sh
cd server
pip install -r requirements.txt
python webservice.py 
$SHELL
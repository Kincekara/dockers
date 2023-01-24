#!/bin/bash

# rMLST Species identification via RESTful API
# Kutluhan Incekara - kutluinct@gmail.com
# 2023-01-24

version="0.1"

helpFunction()
{
   echo ""
   echo "Usage: $0 contigs.fasta"
   exit 1 # Exit 
}

printVersion()
{
    echo "Version $version"
    exit 1
}

while getopts "vh" opt
do
   case "$opt" in
      v ) printVersion ;;
      h ) helpFunction ;;
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$1" ]
then
   echo "Please check your contig/scaffold file";
   helpFunction
fi

# rMLST Species identification via RESTful API
(echo -n '{"base64":true,"details":true,"sequence": "'; base64 $1; echo '"}') | curl -s -H "Content-Type: application/json" -X POST "http://rest.pubmlst.org/db/pubmlst_rmlst_seqdef_kiosk/schemes/1/sequence" -d @- > rmlst.json

# parse predicted taxon
jq -r '.taxon_prediction[0].taxon' rmlst.json > taxon_prediction.rmlst.txt


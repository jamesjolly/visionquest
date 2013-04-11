#!/usr/bin/env bash

wget https://dl.dropboxusercontent.com/s/ig06a6k1o176irr/data.tar.gz
if [ ! -f "data.tar.gz" ];
then
    echo "failure downloading example data"
else
    TEST=$(md5sum data.tar.gz | cut -f 1 -d " ")
    CHECKSUM="887bce7b2be8a52492146be1b3a40b80"
    if [ $CHECKSUM != $TEST ];
    then
        echo "checksum failed, wrong or corrupted data.tar.gz"
    else
        tar -xzf data.tar.gz
        echo "installed examples, try:
        ./process_dir.py ex_dataset dataset
        ./process_dir.py ex_queries queries
        ./batch_search.py queries dataset"
    fi
fi


#!/usr/bin/env bash

trap ctrl_c INT

function ctrl_c {
	cd ..
	echo "Program ended."
}

cd push_index/
./main.py | ../test_client/app.py $1 | ../server/main.py

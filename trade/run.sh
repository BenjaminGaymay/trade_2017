#!/usr/bin/env bash

trap ctrl_c INT

function ctrl_c {
	cd ..
	echo "Program ended."
}

cd push_index/
./main.py 0.01 360 | ../test_client/app.py | ../server/main.py

#!/usr/bin/env bash

for dir in One_Piece/*/;     
do
		for filename in "${dir}"*.jpg;
		do
			python main.py --file "${filename}"
		done 
done
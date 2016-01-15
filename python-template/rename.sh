#!/bin/bash

i=4
for file in `ls -r python-exercise-template-*`
do
    mv $file $file.py
    let i=i-1
done


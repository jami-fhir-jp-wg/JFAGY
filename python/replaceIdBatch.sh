#!/bin/sh

dir_path="../input/fsh/codesystems/*"
out_dir="../input/fsh/codesystems_new/"
dirs=`find $dir_path -maxdepth 0 -type f -name *.fsh`

for dir in $dirs;
do
#    echo $dir
    filebase=`basename $dir` 
    python3 createId.py $dir > $out_dir$filebase
done
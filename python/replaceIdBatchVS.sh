#!/bin/sh

dir_path="../input/fsh/valuesets/*"
out_dir="../input/fsh/valuesets_new/"
dirs=`find $dir_path -maxdepth 0 -type f -name *.fsh`

for dir in $dirs;
do
#    echo $dir
    filebase=`basename $dir` 
    python3 createIdVS.py $dir > $out_dir$filebase
done
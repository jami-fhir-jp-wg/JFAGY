#!/bin/sh
# このスクリプトは、ルート/codesystemsディレクトリ直下のすべてのfshファイルに対して、1500件を超えるcodeがあるファイルについて
# 　超える部分をカットし、^content = fragmentに変更して、codesystems_forIGディレクトリに出力する。
# 起動は、python/replaceIdBatchAbb.shにより行うことを前提としている。
#  codesystems_orgの1階層したのフォルダまで処理する（ -maxdepth 1 ）
dir_path="./codesystems_org/*"
out_dir="./codesystems_forIG/"
dirs=`find $dir_path -maxdepth 1 -type f -name *.fsh`
rm -rf $out_dir
mkdir -p $out_dir
for dir in $dirs;
do
#    echo $dir
    filebase=`basename $dir` 
    python3 python/createIdAbbreviated.py $dir 1000 > $out_dir$filebase
done

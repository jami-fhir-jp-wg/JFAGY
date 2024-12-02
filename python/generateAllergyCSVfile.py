# 入力ファイルはカンマ区切りCSVファイル（UTF8 LF) 1行目ヘッダあり
# 入力ファイルはエクセル公開ファイルをエクセルの機能でCSV(UTF-8)保存したもので、ヘッダはその後に以下に置換してあるファイル。
# 出力ファイルはカンマ区切り、二重引用符囲み、CSVファイル（UTF8 CRLF)　 1行目ヘッダあり
# 出力ファイル名は第２パラメータ（path付き）で指定すること 出力は、第２パラメータのフォルダ名とファイル名の間にutf8フォルダまたはsjsフォルダを指定して、それぞれUTF8 CRLF と Shift-JIS CRLF の２つを生成する

import re
import sys
import csv
import os

with open(sys.argv[1], "r",  encoding='utf-8', newline='') as f:  # encoding='shift_jis', encoding='utf-8' newline=None, ''(改行コードの自動変換なし), '\n', '\r', '\r\n'
    reader = csv.reader(f, delimiter=',' )   # quoting=csv.QUOTE_NONE によりcsv.QUOTE_NONEとすると、引用符に対して特別な処理がされなくなる。引用符で囲まれた部分の区切り文字も要素の区切りとして扱われる。
    filename = os.path.basename(sys.argv[2])
    pathfolder = os.path.dirname(sys.argv[2])
    with open(pathfolder + "/utf8/" + filename, 'w',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
        for row in reader:
            writer.writerow(row)

with open(sys.argv[1], "r",  encoding='utf-8', newline='') as f:  # encoding='shift_jis', encoding='utf-8' newline=None, ''(改行コードの自動変換なし), '\n', '\r', '\r\n'
    reader = csv.reader(f, delimiter=',' )   # quoting=csv.QUOTE_NONE によりcsv.QUOTE_NONEとすると、引用符に対して特別な処理がされなくなる。引用符で囲まれた部分の区切り文字も要素の区切りとして扱われる。
    filename = os.path.basename(sys.argv[2])
    pathfolder = os.path.dirname(sys.argv[2])
    with open(pathfolder + "/sj/" + filename, 'w',encoding='shift_jis') as f:
        writer = csv.writer(f,delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
        for row in reader:
            writer.writerow(row)
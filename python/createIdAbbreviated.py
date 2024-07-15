
import sys
import re
# コマンド　　ひとつのCodeSystemファイルパス　N
#　コードをN件（Nはargs[2]で与える）までのファイルにする。（あとはカット）
# 　Id: は　CodeSystem:の値を変換して置き換える

if __name__ == '__main__':
    args = sys.argv
    filename = args[1]
    maxcount = int(args[2])
#    print (filename)
    count = 0
    content = "#complete"
    # 件数を数えてmaxcountを超えるなら#fragmentを設定する
    with open(filename) as f:
        for s_line in f:
            if s_line.replace(" ", "").startswith("*#"):
                count = count + 1
                if count > maxcount:
                    content = "#fragment"
    contentFlag = False
    contenteCount = count         
    count = 0
    with open(filename) as f:
        for s_line in f:
            s_line = s_line.replace("\n", "")
            if s_line.replace(" ", "").startswith("*^valueSet="):
                continue
            elif s_line.startswith("Description: "):
                if content == "#fragment":
                    m = re.search(r'"(.*)"',s_line)
                    s_line1 = 'Description: "' + m.group(1) + ' --- 最初の' + str(maxcount) + ' 件だけの表示に限定（fragment化）, CodeSystem件数:' + str(contenteCount)+ ' ---"'
                    print (s_line1)
                else:
                    print (s_line)
            elif s_line.startswith("CodeSystem:"):
                id = s_line.replace("CodeSystem:", "")
                id = id.replace(" ", "")
                id = id.lower().replace("_","-").replace(".","-")
                print (s_line)
            elif s_line.startswith("Id: "):
                s_line = s_line.replace("Id: ", "")
                s_line = s_line.replace(" ", "")
                print ("Id: "+id)
            elif s_line.replace(" ", "").startswith("*^content="):
                print ("* ^content = "+content)
                contentFlag = True
            else:
                if s_line.replace(" ", "").startswith("*#"):
                    if count == 0 and contentFlag == False:
                        print ("* ^content = "+content)
                        contentFlag = True
                    count = count + 1               
                print (s_line)
            if count >= maxcount:
                break







import sys







# コマンド　　ひとつのCodeSystemまたはValueSetファイルパス　
#
if __name__ == '__main__':
    args = sys.argv
    filename = args[1]
#    print (filename)
    count = 0
    with open(filename) as f:
        for s_line in f:
            s_line = s_line.replace("\n", "")
            if s_line.replace(" ", "").startswith("*^valueSet="):
                continue
            elif s_line.startswith("CodeSystem:"):
                id = s_line.replace("CodeSystem:", "")
                id = id.replace(" ", "")
                id = id.lower().replace("_","-").replace(".","-")
            if s_line.startswith("Id: "):
                s_line = s_line.replace("Id: ", "")
                s_line = s_line.replace(" ", "")
                print ("Id: "+id)
            else:
                print (s_line)
#                count = count + 1
#            if count > 15:
#                break
# =======================================================
# sushi-config.yaml　special url　生成スクリプト
# 処理概要：
# cannonical urlの命名規則の警告を避けるため、リソースファイル
# url情報を抽出し、sushi-config.yamlを書き換える処理を行なう。
# =======================================================
require "json"
require "uri"

# リソース格納フォルダ
genenareted = "./fsh-generated/resources/"
# sushi-configパス
maptablePath="maptable.txt"

#--- URL抽出処理 ---
def fillUrl(prefix, sb, extension = false)
  files = Dir.glob(prefix + "-*.json").sort
  for fl in files
      File.open(fl) do |f|
          h = JSON.load(f)
          if (h["type"] == "Extension") == extension then
            url = h["url"].to_s
            if url.start_with?("urn:") == false then                    
                urlfile = File.basename(URI.parse(url).path)
                sb << "ln -s " + fl + " " + urlfile + "\n"
            end
          end
      end
  end
end

# configの読み込み
def getConfingText(path)
  File.open(path, 'r') do |fr|
    return fr.read()
  end
end

# configの書き込み
def setConfigText(path, text)
  File.open(path, 'w') do |fw|
    fw.write(text)
  end
end

# -------------------------------------------------------
# メイン処理（エントリポイント）
# -------------------------------------------------------
sb = "mapping:\n"

Dir.chdir(genenareted)  #カレントディレクトリ移動(fshgenerated/resouces)

p 'url情報取得'
fillUrl("StructureDefinition", sb)
fillUrl("StructureDefinition", sb, true)
fillUrl("CapabilityStatement", sb)
fillUrl("SearchParameter", sb)
fillUrl("CodeSystem", sb)
fillUrl("ValueSet", sb)

Dir.chdir('../..')  ##カレントディレクトリ移動(project配下)

#p 'sushi-configの取得'
#allText = getConfingText(sushiconfigPath)
allText = sb

#p '正規表現による置換'
#regex = /\s{2}special-url:\n(\s{4}-\s(http|urn:oid:).*\n)*/
#allText.gsub!(regex, sb)

#p 'sushi-configによる書き込み'
setConfigText(maptablePath, allText)

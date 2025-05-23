
###  J-FAGYアレルゲンコード

アレルギー原因物質のコード表JFAGYは、「食品」、「非医薬品・食品」のカテゴリーに分けて、アレルゲンのコードを定義したコード表です。<br>
また、「医薬品」については、個別医薬品コード（通称YJコード）、薬剤成分アレルギー用コード(注1)、WHO-ATCコードのいずれかを使用して表現できるようになっています。ただし、電子カルテ情報共有サービスでは、このうち個別医薬品コード（通称YJコード）、薬剤成分アレルギー用コードのどちらかを使用することになっています。

###  JFAGYアレルゲンコードの概要
JFAGYコードは、メタコードと呼ばれる3文字コード列と、それに続く文字コード列の結合した文字コード（コアコード）により表現される。

####  メターコード
メタコード3桁は、次のような意味をもって構成されており、後続のコアコードのコード体系、その文字数、アレルゲン領域区分からなる。

  - 1桁目：コアコードのコード体系識別文字。J=JFAGYコード、Y=個別医薬品コード（YJ）、P=厚生労働省一般処方マスターのコード、G=薬剤成分アレルギー用コード（注1）、A=WHO-ATC分類コード（7桁コード）、D=ダミーコード（注2）、0（ゼロ）=コアコードなし。
  - 2桁目：コアコードの文字数を36進数で表した1文字（0〜9、A、B、C、D、…）。現在のバージョンでは、最大16桁（0〜F）としている。現在のバージョンでは、0、7、9、C(10進数の12)だけが使われる。
  - 3桁目：コアコードが対象とするアレルゲン領域区分識別コード。F=食品、M=医薬品、N=非食品・非医薬品、0=全領域（領域不明の特定できない一つ以上のアレルゲン）。


<table border="1" class="table-page" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>1桁目</th>
      <th>2桁目</th>
      <th>3桁目</th>
      <th>メタコード</th>
      <th>コアコード名称　</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>J</td>
      <td>9</td>
      <td>F</td>
      <td>J9F</td>
      <td>JFAGY食品コード</td>
    </tr>
    <tr>
      <td>J</td>
      <td>9</td>
      <td>N</td>
      <td>J9N</td>
      <td>JFAGY非食品・非医薬品コード</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>C</td>
      <td>M</td>
      <td>YCM</td>
      <td>薬剤アレルギー用コード（個別医薬品コード（YJ））</td>
    </tr>
    <tr>
      <td>G</td>
      <td>C</td>
      <td>M</td>
      <td>GCM</td>
      <td>剤形・規格・銘柄不明コード(注1)</td>
    </tr>
    <tr>
      <td>A</td>
      <td>7</td>
      <td>M</td>
      <td>A7M</td>
      <td>WHO-ATC分類コード  電子カルテ情報共有サービスでは使用しない。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>F</td>
      <td>D9F</td>
      <td>食品ダミーコード(注2) 。コアコードとして”000000000”(9桁の文字0) を使用する。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>M</td>
      <td>D9M</td>
      <td>医薬品ダミーコード(注2) 。同上。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>N</td>
      <td>D9N</td>
      <td>非食品・非医薬品ダミーコード(注2） 。同上。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>000</td>
      <td>コアコードなし、全アレルゲン。電子カルテ情報共有サービスでは使用しない。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>M</td>
      <td>00M</td>
      <td>コアコードなし、医薬品アレルゲン。同上。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>F</td>
      <td>00F</td>
      <td>コアコードなし、食品アレルゲン。同上。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>N</td>
      <td>00N</td>
      <td>コアコードなし、非食品・非医薬品アレルゲン。同上。</td>
    </tr>
  </tbody>
</table>

###  コアコード
コアコードは、メタコードに続く7から12桁のコードで、個別のアレルゲンを識別する。ただし、メタコードが0で始まる場合には、コアコードは存在しない。したがって、メタコード3桁だけとなる。

<table border="1" class="table-page" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>メタコード1桁目</th>
      <th>コアコード名称　</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>J</td>
      <td>JFAGYコード（食品、非食品・非医薬品）</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>個別医薬品コード（YJ）</td>
    </tr>
    <tr>
      <td>G</td>
      <td>剤形・規格・銘柄不明コード(注1)</td>
    </tr>
    <tr>
      <td>A</td>
      <td>WHO-ATC分類コード。電子カルテ情報共有サービスでは使用しない。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>ダミーコード（注2）</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>コアコードなし</td>
    </tr>
  </tbody>
</table>

  - 注1： 剤形・規格・銘柄不明コードとは、個別医薬品コード（YJ）12桁のうち末尾の3桁を"ZZZ"に置き換え、製剤剤形や規格や銘柄（販売会社名など）に関する違いに関するコード部分を削除した、電子カルテ情報共有サービスで使用するために作成されたコード。 剤形・規格・銘柄不明が不明なレベルで表現したい場合に使用できる。<br>
  system　URL: "http://jpfhir.jp/fhir/core/CodeSystem/GCM/JP_JfagyMedicationAllergen_CS"
  - 注2： ダミーコードとは、特定のアレルゲンを記述したい場合であって、適切な表現コードが提供されているコード表のコードでは記述できないと判断された場合に使用するもので、"コード化不可コード"として使用する。<br>
  コアコードとして、"000000000"を使用する。
  <br>ダミーコードは、厚生労働省電子カルテ情報共有サービスにおいて導入された独自コード体系である。ダミーコードを使用した場合には、別の方法でアレルゲンを文字列表現する必要がある。FHIRのCodeableConceptデータタイプを使用する場合にはtext要素にアレルゲン名称をフリーテキストで記述することとする。


###  領域別のFHIR CodeSystemとValueSet
FHIR規格でJFAGYコードおよびその体系を使用するために次のCodeSystemとValueSetを定義している。

###  CodeSystem


<table class="table-page" border="1" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>領域</th>
      <th>CodeSystem名称</th>
      <th>CodeSystem URL　</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>食品</td>
      <td>JP_JfagyFoodAllergen_CS</td>
      <td><a href="https://jpfhir.jp/fhir/core/terminology/igv1/CodeSystem-jp-jfagyfoodallergen-cs.html">http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyFoodAllergen_CS</a></td>
    </tr>
    <tr>
      <td>非食品・非医薬品</td>
      <td>JP_JfagyNonFoodNonMedicationAllergen_CS</td>
      <td><a href="https://jpfhir.jp/fhir/core/terminology/igv1/CodeSystem-jp-jfagynonfoodnonmedicationallergen-cs.html">http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyNonFoodNonMedicationAllergen_CS</a></td>
    </tr>
    <tr>
      <td>医薬品(薬剤アレルギー用コード)</td>
      <td>JP_JfagyMedicationAllergenYCM_CS</td>
      <td><a href="https://jpfhir.jp/fhir/core/terminology/igv1/CodeSystem-jp-jfagymedicationallergenycm-cs.html">http://jpfhir.jp/fhir/core/CodeSystem/YCM/JP_JfagyMedicationAllergen_CS</a></td>
    </tr>
    <tr>
      <td>医薬品(薬剤成分アレルギー用コード)</td>
      <td>JP_JfagyMedicationAllergenGCM_CS</td>
      <td><a href="https://jpfhir.jp/fhir/core/terminology/igv1/CodeSystem-jp-jfagymedicationallergengcm-cs.html">http://jpfhir.jp/fhir/core/CodeSystem/GCM/JP_JfagyMedicationAllergen_CS</a></td>
    </tr>
  </tbody>
</table>

  - 食品（JP_JfagyFoodAllergen_CS）CodeSystemには、すべてのJFAGY食品コード("00F"を含む)、および食品ダミーコード("D9F000000000")が含まれ、コード構成にはメタコード3桁が先頭に含まれる。
  - 非食品・非医薬品（JP_JfagyNonFoodNonMedicationAllergen_CS）CodeSystemには、すべてのJFAGY非食品・非医薬品コード("00N"を含む)、および非食品・非医薬品ダミーコード("D9N000000000")が含まれ、コード構成にはメタコード3桁が先頭に含まれる。
  - 医薬品（薬剤アレルギー用コード）（JP_JfagyMedicationAllergenYCM_CS）CodeSystemには、保険診療適用可能な範囲の医薬品コードである「個別医薬品コード（YJコード）リストコード」、医薬品ダミーコード（"D9M000000000"）、および医薬品アレルゲン"00M"コードが含まれる。コード構成にはメタコード3桁が先頭に含まれる。<br>
  - 医薬品（薬剤成分アレルギー用コード）（JP_JfagyMedicationAllergenGCM_CS）CodeSystemには、保険診療適用可能な範囲の医薬品に含まれる成分に対するコードである「薬剤成分アレルギーコード」が含まれる。コード構成にはメタコード3桁が先頭に含まれる。<br>
  なお、WHOーATC分類コードは、厚生労働省電子カルテ情報共有サービスにおけるアレルギーコードとしては使用しないため、含まれない。

###  対応するValueSet

<table class="table-page" border="1" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>ValueSet名称</th>
      <th>ValueSet URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JP_AllergyIntolerance_VS</td>
      <td><a href="http://jpfhir.jp/fhir/core/ValueSet/JP_AllergyIntolerance_VS">http://jpfhir.jp/fhir/core/ValueSet/JP_AllergyIntolerance_VS</a></td>
    </tr>
  </tbody>
</table>

<br>含まれるCodeSystem:   

  - JP_JfagyMedicationAllergenYCM_CS
  - JP_JfagyMedicationAllergenGCM_CS
  - JP_JfagyFoodAllergen_CS
  - JP_JfagyNonFoodNonMedicationAllergen_CS

##  コード表入手先・ダウンロード先
ここに収載のコード表は、それぞれ著作権、使用範囲の制限があるものがありますので、各ページ記載情報に留意してください。

[【ダウンロード用ページへ】](download.html)

##  参考文献

  - [Kawazoe,Y. et.al.Development of a code system for allergens and its integration into the HL7 FHIR AllergyIntolerance resource](https://www.sciencedirect.com/science/article/pii/S1386505624004027)
  - 河添 悦昌, 永島 里美, 大江 和彦. アレルギー情報の標準化を目指すJ-FAGYアレルゲン用語集. 第43回医療情報学連合大会.2023
  - [河添 悦昌, 永島 里美, 大江 和彦. アレルギー情報の標準化を目指すJ-FAGYアレルゲン用語集とアレルゲンコードシステム. 第42回医療情報学連合大会.2022](https://mhlw-grants.niph.go.jp/system/files/report_pdf/202222057A-sonota2.pdf)

{% include markdown-link-references.md %}
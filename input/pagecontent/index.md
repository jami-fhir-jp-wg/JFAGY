.table-page {
  margin-left: 5%;
}


###  J-FAGYアレルゲンコード

アレルギー原因物質のコード表JFAGYは、「食品」、「非医薬品・食品」のカテゴリーに分けて、アレルゲンのコードを定義したコード表です。<br>
また、「医薬品」については、個別医薬品コード（通称YJコード）、[一般処方マスター（一般厚生労働省保険局）](https://www.mhlw.go.jp/seisakunitsuite/bunya/kenkou_iryou/iryouhoken/shohosen_200401.html)、YJコード派生コード（注1）、[WHO-ATCコード](https://www.who.int/tools/atc-ddd-toolkit/atc-classification) のいずれかを使用して表現できるようになっています。

###  JFAGYアレルゲンコードの概要
JFAGYコードは、メタコードと呼ばれる3文字コード列と、それに続く文字コード列の結合した文字コード（コアコード）により表現される。

####  メターコード
メタコード3桁は、次のような意味をもって構成されており、後続のコアコードのコード体系、その文字数、アレルゲン領域区分からなる。

  - 1桁目：コアコードのコード体系識別文字。J=JFAGYコード、Y=個別医薬品コード（YJ）、P=厚生労働省一般処方マスターのコード、G=YJ派生コード（注1）、A=WHO-ATC分類コード（7桁コード）、D=ダミーコード（注2）、0（ゼロ）=コアコードなし。
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
      <td>個別医薬品コード（YJ）</td>
    </tr>
    <tr>
      <td>P</td>
      <td>C</td>
      <td>M</td>
      <td>PCM</td>
      <td>厚生労働省一般処方マスターのコード</td>
    </tr>
    <tr>
      <td>G</td>
      <td>C</td>
      <td>M</td>
      <td>GCM</td>
      <td>YJ派生コード(注1)</td>
    </tr>
    <tr>
      <td>A</td>
      <td>7</td>
      <td>M</td>
      <td>A7M</td>
      <td>WHO-ATC分類コード</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>F</td>
      <td>D9F</td>
      <td>食品ダミーコード(注2) 。コアコードとして”999999999”(9桁の文字9) を使用する。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>M</td>
      <td>D9F</td>
      <td>医薬品ダミーコード(注2) 。同上。</td>
    </tr>
    <tr>
      <td>D</td>
      <td>9</td>
      <td>N</td>
      <td>D9F</td>
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
      <td>000</td>
      <td>コアコードなし、医薬品アレルゲン。同上。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>F</td>
      <td>000</td>
      <td>コアコードなし、食品アレルゲンs。同上。</td>
    </tr>
    <tr>
      <td>0（ゼロ）</td>
      <td>0（ゼロ）</td>
      <td>N</td>
      <td>000</td>
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
      <td>P</td>
      <td>厚生労働省一般処方マスターのコード。電子カルテ情報共有サービスでは使用しない。</td>
    </tr>
    <tr>
      <td>G</td>
      <td>YJ派生コード（注1）</td>
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

  - 注1： YJ派生コードとは、個別医薬品コード（YJ）12桁のうち末尾の3桁を"ZZZ"に置き換えたコード。末尾3桁は通常、同一規格内での順序番号とチェックデジットを表している部分であり、同一規格で複数社から供給されているケースを区別するために使用されていることが多い。これをZZZで置き換えることで、複数社の区別をしない（できない）医薬品コードで表現したい場合に使用できる。<br>
  厚生労働省電子カルテ情報共有サービスにおいて導入された独自コード体系であり、チェックデジットの機能が使用できなくなっていることに留意が必要である。
  - 注2： ダミーコードとは、特定のアレルゲンを記述したい場合であって、適切な表現コードが提供されているコード表のコードでは記述できないと判断された場合に使用するもので、"コード化不可コード"として使用する。<br>
  コアコードとして、"999999999"を使用する。
  <br>厚生労働省電子カルテ情報共有サービスにおいて導入された独自コード体系である。ダミーコードを使用した場合には、別の方法でアレルゲンを文字列表現する必要がある。FHIRのCodeableConceptデータタイプを使用する場合にはtext要素にアレルゲン名称をフリーテキストで記述することとする。

<br>

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
      <td><a href="http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyFoodAllergen_CS">http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyFoodAllergen_CS</a></td>
    </tr>
    <tr>
      <td>非食品・非医薬品</td>
      <td>JP_JfagyNonFoodNonMedicationAllergen_CS</td>
      <td><a href="http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyNonFoodNonMedicationAllergen_CS">http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyNonFoodNonMedicationAllergen_CS</a></td>
    </tr>
    <tr>
      <td>医薬品</td>
      <td>JP_JfagyMedicationAllergen_CS</td>
      <td><a href="http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyMedicationAllergen_CS">http://jpfhir.jp/fhir/core/CodeSystem/JP_JfagyMedicationAllergen_CS</a></td>
    </tr>
  </tbody>
</table>

  - 食品（JP_JfagyFoodAllergen_CS）CodeSystemには、すべてのJFAGY食品コード("00F"を含む)、および食品ダミーコード("D9F000000000")が含まれ、コードにはメタコード3桁が含まれる。
  - 非食品・非医薬品（JP_JfagyNonFoodNonMedicationAllergen_CS）CodeSystemには、すべてのJFAGY非食品・非医薬品コード("00N"を含む)、および非食品・非医薬品ダミーコード("D9N000000000")が含まれ、コードにはメタコード3桁を含まれる。
  - 医薬品（JP_JfagyMedicationAllergen_CS）CodeSystemには、すべての個別医薬品コード（YJ）、およびそれの末尾3桁をZZZに置き換えたYJ派生コードのすべてが含まれ、コードにはメタコード3桁が含まれる。<br>
  また、医薬品ダミーコード（"D9M000000000"）、および医薬品アレルゲン
  "00M"コードが含まれる。<br>
  なお、現時点では、厚生労働省一般処方マスターのコード、WHOーATC分類コードは、厚生労働省電子カルテ情報共有サービスで使用しないため含まれない。

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

  - JP_JfagyFoodAllergen_CS
  - JP_JfagyMedicationAllergen_CS
  - JP_JfagyNonFoodNonMedicationAllergen_CS

##  コード表入手先・ダウンロード先
ここに収載のコード表は、それぞれ著作権、使用範囲の制限があるものがありますので、各ページ記載情報に留意してください。

###  CSV、エクセル形式
  - [JFAGYコード表（エクセル）](https://jpfhir.jp/fhir/core/terminology/JFAGY/excel_files/JFAGY_20240709V2.xlsx) （医薬品領域を除く）[Copyright CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.ja#s3)
  - [個別医薬品コード表](http://www.capstandard.jp/)
  - [厚生労働省一般処方マスター](https://www.mhlw.go.jp/seisakunitsuite/bunya/kenkou_iryou/iryouhoken/shohosen_200401.html)

###  FHIR CodeSystem JSON形式

  - 準備中

###  FHIR CodeSystem FSH形式

  - 準備中



{% include markdown-link-references.md %}
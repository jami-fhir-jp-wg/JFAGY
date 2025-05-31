
###  J-FAGYアレルゲンコード表のダウンロードページ

J-FAGYアレルゲンコードの概要と解説については、[【こちら】](index.html)をご覧ください。<br>
このページに掲載している情報、ファイルの著作権は次のとおりです。<br>

著作権表示：Copyright　国立大学法人東京大学、一般社団法人日本医療情報学会<br>
発行者：東京大学大学院医学系研究科医療情報学分野<br>
著作権ポリシー：CC BY 4.0(<a href="https://creativecommons.org/licenses/by/4.0/deed.ja">表示 4.0 国際</a>)<br>

#### CSVファイル
  - カンマ区切りのテキスト形式
  - 各カラムは二重引用符で囲まれる。
  - カラムデータにカンマが含まれることがある。
  - 文字コード　UTF-8またはShiftJIS、BOMなし
  - 改行コード　CR LF

詳細仕様は、<a href="download_files/JFAGY_J9FN_CSV_Format_v1.pdf">こちらをダウンロード</a>

<table border="1" class="table-page" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>リリース日付</th>
      <th>同日内版数</th>
      <th>元データバージョン日付</th>
      <th>文字コード</th>
      <th>ファイル名リンク(*3)</th>
      <th>備考</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td  rowspan="2">2025-05-31</td>
      <td  rowspan="2">1</td>
      <td  rowspan="2">2025-04-01-V2</td>
      <td>UTF-8 (*1)</td>
      <td><A href="download_files/utf8/JFAGY_J9FN_20250401_R01-utf8.zip">JFAGY_J9FN_20250401_R01-utf8.zip</a></td>
      <td rowspan="2">"オレンジ"の追加と関連する2つの柑橘類をその下位に移し、コード変更。</td>
    </tr>
      <tr><td>shift-jis (*2)</td>
          <td><A href="download_files/sj/JFAGY_J9FN_20250401_R01-sjis.zip">JFAGY_J9FN_20250401_R01-sjis.zip</a></td>
      </tr>
          <tr>
      <td  rowspan="2">2024-11-25</td>
      <td  rowspan="2">1</td>
      <td  rowspan="2">2024-07-09-V3</td>
      <td>UTF-8 (*1)</td>
      <td><A href="download_files/utf8/JFAGY_J9FN_20240709_R01-utf8.zip">JFAGY_J9FN_20240709_R01-utf8.zip</a></td>
      <td rowspan="2">CSV形式の初回リリース</td>
    </tr>
      <tr><td>shift-jis (*2)</td>
          <td><A href="download_files/sj/JFAGY_J9FN_20240709_R01-sjis.zip">JFAGY_J9FN_20240709_R01-sjis.zip</a></td>
      </tr>
  </tbody>
</table>
*1 utf-8: MacOS でデフォルトで使用される文字コード。Excelではデフォルトでshift-jisコードが使われることがある。<br>
*2 shift-jis : WindowsのExcelなどでデフォルトで使用されることが多い文字コード<br>
*3 ブラウザのセキュリティー設定によってはzip圧縮形式のファイルをリンク先クリックだけではダウンロードできない場合がある。右ボタンクリックで表示されるメニューから「名前をつけて保存する」ことでダウンロードできることがある。zip形式のファイルを展開後のCSVファイル名は、utf-8、shift-jisの文字コードによらず同一ファイル名であるので、注意すること。

<br>

###  Excelファイル

CSVファイルのデータカラムに加えて、ツリー形式表示用カラムなどが追加されています。

<table border="1" class="table-page" style="border-collapse: collapse">
  <thead>
    <tr>
      <th>データバージョン日付</th>
      <th>ダウンロードリンク</th>
      <th>備考</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2024-07-09-V2</td>
      <td><A href="download_files/JFAGY_20240709V3.xlsx">JFAGY_20240709V3.xlsx</a></td>
      <td></td>
    </tr>
    <tr>
      <td>2025-04-01-V2</td>
      <td><A href="download_files/JFAGY_20250401V2.xlsx">JFAGY_20250401V2.xlsx</a></td>
      <td></td>
    </tr>
  </tbody>
</table>


###  参考情報
  - [個別医薬品コード（YJコード）リストの掲載ページ](http://www.capstandard.jp/)

### 問い合わせ先
  - email: office＠jpfhir.jp 　(＠を全角から半角に変更してください。)


{% include markdown-link-references.md %}
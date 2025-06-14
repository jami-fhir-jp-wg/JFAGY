### 変更履歴　

#### version: "2025.05.22" (2025.06.03修正リリース)
  - ファイル中の変更区分：CXGCATEGORYカラムに変更区分を修正設定。
    - J9FA32113211 "ネーブルオレンジ" 変更区分 1 (今版で追加)
    - J9FA32111600 "ネーブルオレンジ" 変更区分 3 (今版で削除)
    - J9FA32113212 "バレンシアオレンジ" 変更区分 1 (今版で追加)
    - J9FA32111700 "バレンシアオレンジ" 変更区分 3 (今版で削除)
    - 今回変更にならなかったすべてのレコードの変更区分を0（今版で変更なし）

#### version: "2025.05.22" (2025.05.31修正リリース)
  - ファイル中の変更区分：CXGCATEGORYカラムに変更区分を設定。
    - J9FA32113200 "オレンジ"　変更区分 1 (今版で追加)
    - J9FA32113211 "ネーブルオレンジ" 変更区分 2 (今版で変更)
    - J9FA32111600 "ネーブルオレンジ" 変更区分 3 (今版で削除)
    - J9FA32113212 "バレンシアオレンジ" 変更区分 2 (今版で変更)
    - J9FA32111700 "バレンシアオレンジ" 変更区分 3 (今版で削除)

#### version: "2025.05.22" (2025.05.21リリース)
  - JP_JfagyFoodAllergen_CSに以下のコード追加と変更を行った。
    - J9FA32113200 "オレンジ"　を追加
    - J9FA32113211 "ネーブルオレンジ" をオレンジの下位に移動してコード変更
    - J9FA32111600 "ネーブルオレンジ" を廃止コードクラスに移動
    - J9FA32113212 "バレンシアオレンジ" をオレンジの下位に移動してコード変更
    - J9FA32111700 "バレンシアオレンジ" を廃止コードクラスに移動
  - 廃止コードクラス コード"X"を新設。
  - 20250401版をリリース。

#### version: "2024.12.05"

  - ダウンロードページを新設した。
  - エクセルデータ中の用語、用語のふりがなに、Windows固有文字の記号（ダッシュ）が含まれていたのを半角マイナスに修正した。
  - 用語中にカンマが含まれる用語について、CSVファイル処理の問題があり、不正な表記になっていたのを修正した。
  - ダミーコードがコード表の最初と最後に２度出現したので、最後のほうを削除した。
  - 参考文献を掲載した。
  
#### version: "2024.10.08"

  - 医薬品アレルギーコードとして使用可能な薬剤成分アレルギーコードが追加され、これに伴い、薬剤アレルギーコードのURLが変更された。
  - メタコード一覧表に誤記があったので修正。
  
#### version: "2024.9.20"

  - ダミーコードの記述方法としてall '9'、　all '0' の記載が混在していたのを訂正し、all '0' (9桁の’0')に統一した。
  - JFAGY医薬品アレルギーコードについて、YJコードの末尾3桁をZZZに変更したコード体系を含んでいたが、これを削除した。これは今後別のコード表となる予定。
  - メターコード表で、ダミーコード3種類に対応するメタコードに誤記があったのを修正。

#### version: "2024.7.9"

初回公開版

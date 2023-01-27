# FutabaDownloader-Python
##ふたばちゃんねるの画像を一括DLするだけのCUIツール
![にゃん](https://booth.pximg.net/b51ae20d-21b7-4796-abc5-7dbd7426050c/i/3926464/4463e690-ab35-4a4a-8614-190a85a9ff25_base_resized.jpg)
############################################################<br>
ふたばだうんろーだー<br>
ver1.0 / works on windows7 , 10 , 11<br>
############################################################<br>

-------------------------------ウイルス誤検知に関して-------------------------------<br>
プログラムの仕様上、ディレクトリの新規作成やファイルの生成を行うため、<br>
ウイルス(トロイの木馬)として削除されることがあります。<br>
申し訳ございませんが、セキュリティソフトの除外リストへの追加や、<br>
手動での起動承認をお願いいたします。<br>
------------------------------------------------------------------------------------------<br>

・なんだこのツール
    
    画像掲示板「ふたばちゃんねる(http://www.2chan.net/)」のスレッドから画像をDLするだけのツールです。
    先駆者の方が作っていたツールが合わなかったので自作した次第です。

    バグなどもあるかと思いますが、ご了承願います。
    ツールの更新は気が向いたらやります。気が向かなければやりません。

    もし良かったらお賽銭ください(乞食)

・どう使うん？
    
    0 : 同じディレクトリにある"FubataDL.exe"をダブルクリックで起動するとCUIが出てきます。
    CUI内に書かれている文字に従えば基本的に問題はないかと思います。

    1 : 「ふたばちゃんねるのスレッドのURL(末尾.htm)を入力してください。」
    と出たら、ふたばちゃんねるのスレッドのURL(板全体ではないので注意)をコピペして入力。
    入力が終わり次第、Enterキーを押してください。
    ※ふたばちゃんねる以外のURLが入力されるとプログラムが強制終了いたします。

    2 : 「https:// と 2chan.netの間の文字を入力してください。」
    と出たら、1で入力したURLを見て、指示通りの文字を入力してください。
    (※https://hoge.2chan.net なら hoge を入力する感じです。)
    入力が終わり次第、Enterキーを押してください。
    ※不正文字や一致しない場合はスレッド参照ができないためエラーを起こし、最終的に画像が保存できません。

    3 : 「動画ファイルを保存しますか？( 1 = 保存する | 0 = 保存しない )」
    と出たら、1 or 0 を入力し、選択肢を入れ、Enterキーを押してください。
    (ここで言われる動画ファイルは.mp4を指しています。)

    4 : 画像ファイルの自動取得が始まります。
    速度は回線に依存しますので気長にお待ち下さい。

    5 : 「Enterを押すとプログラムを終了します」
    と出たら、Enterキーでプログラムを終了してください。

    保存した画像は、実行ファイルのディレクトリにある画像フォルダの中に保存されています。
    スレッド名ごとに保存フォルダを分けているので沢山ダウンロードしても大丈夫です。

・更新履歴
    2022/06/06 : 初版公開。DLはReleaseから。
    一番新しいものは : https://booth.pm/ja/items/3926464 にあります

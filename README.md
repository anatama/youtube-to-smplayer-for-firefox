youtube-to-smplayer-for-firefox
===============================
Youtubeの動画と再生リストをsmplayer上で再生できるようにする。
FirefoxとFirefoxの拡張 AppLauncher を組み合わせることを想定している。

メリット
------
* 再生にブラウザが必要無いので、使用リソースを軽減できる（はず）
* Youtubeのサイト上で流れる広告等が挿入されない
* Flashのクラッシュが起こらない

インストール方法
------
任意のディレクトリにファイルを配置する。以下は`$HOME/usr/src`に配置する例。

    $ cd ~/usr/src
    $ git clone git@github.com:anatama/youtube-to-smplayer-for-firefox.git

Firefoxを起動し、AppLauncherをインストールする。検索すれば出てくる。

AppLauncherに次の設定を追加する。

* Name -> `smplayerで再生する` (任意)
* Path -> `/home/username/youtube-to-smplayer-for-firefox/tube-to-smplayer`
* Arguments -> `&turl;`

使い方
------
Youtubeで観たい動画を検索する。

1. 動画か再生リストのハイパーリンクを右クリックする
2. コンテキストメニューから「AppLauncher」を選ぶ
3. 「smplayerで再生する」をクリックする
4. フォームで「smplayerで再生する」または「smplayerのプレイリストに追加する」どちらかを選ぶ

動作確認した環境
------
* Ubuntu 12.04 LTS
* Firefox 13.0.1
* smplayer 0.8.0
* Python 2.7.3

smplayerについては、Youtubeの再生に対応した0.7.0以降が少なくとも必要。

おまけ
------
gitをインストールする方法。

    $ sudo apt-get install git

最新版のsmplayerのインストール方法(0.7.0以降であれば必要ない)。

    $ sudo add-apt-repository ppa:rvm/smplayer
    $ sudo apt-get update

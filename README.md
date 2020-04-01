[en](./README.en.md)

# Python.TTF2PNG.BitmapFont

　ビットマップフォント作成（TTF→PNG）

# 特徴

* CLI: 指定したTTFから256*256のPNGを出力する

# 開発環境

* <time datetime="2020-03-30T19:12:23+0900">2020-03-30</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspbian](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2019-09-26 <small>[setup](http://ytyaru.hatenablog.com/entry/2019/12/25/222222)</small>
* bash 5.0.3(1)-release
* Python 3.7.3
* [pyxel][] 1.3.1

[pyxel]:https://github.com/kitao/pyxel

```sh
$ uname -a
Linux raspberrypi 4.19.97-v7l+ #1294 SMP Thu Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux
```

# インストール

　pyenvで3.7以上のPythonをインストールする。

　次に以下のように[pyxel][]をインストールする。

* [pyxel/README](https://github.com/kitao/pyxel/blob/master/README.ja.md#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)

```sh
sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev
git clone https://github.com/kitao/pyxel.git
cd pyxel
make -C pyxel/core clean all
pip3 install .
```

# 使い方

```bash
git clone https://github.com/Python.TTF2PNG.BitmapFont.20200401124848
cd Python.TTF2PNG.BitmapFont.20200401124848/src
./run.sh
```

## 引数

引数|値
----|--
`-f`|ttf形式ファイルパス
`-w`|png出力時における1字あたりのピクセル幅
`-h`|png出力時における1字あたりのピクセル高さ

```sh
$ GenerateBitmapFont.py --help
usage: GenerateBitmapFont.py [-f FONTFILE] [-w WIDTH] [-h HEIGHT] [--help]

ビットマップフォント作成（.ttfから.pngを出力）

optional arguments:
  -f FONTFILE, --fontfile FONTFILE
                        ttf形式ファイルパス (default: x8y12pxTheStrongGamer.ttf)
  -w WIDTH, --width WIDTH
                        png出力時における1字あたりのピクセル幅 (default: 8)
  -h HEIGHT, --height HEIGHT
                        png出力時における1字あたりのピクセル高さ (default: 12)
  --help                ヘルプ表示する
```

# 著者

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# ライセンス

　このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

## 謝辞

　デフォルト値にあるフォントの作者様は以下。感謝。

* [00FF © 2018 hicc 患者長ひっく](http://www17.plala.or.jp/xxxxxxx/00ff/)
* [Pythonでゲーム用にビットマップフォントを読み込む話](https://0xd.jp/post/pyxel_draw_custom_font/)


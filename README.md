# create_shogi_pieces

## 概要

本ソフトウェアを使って、[MyShogi](https://github.com/yaneurao/MyShogi)の下記画像を作成することができます。

| ファイル名 | 説明 |
----|----
| hand\_number\_v1\_864\_96.png | 駒台に置かれた駒の数を表す画像 |
| hand\_box\_number\_v1\_864\_96.png | 駒箱に置かれた駒の数を表す画像 |
| number\_v1\_873\_19.png | 将棋盤の筋(１から９)に使用する画像 |
| number\_v1\_22\_954.png | 将棋盤の段(一から九)に使用する画像 |
| number\_v2\_873\_19.png | 将棋盤の筋(1から9)に使用する画像 |
| number\_v2\_22\_954.png | 将棋盤の段(aからi)に使用する画像 |
| number\_v1\_485\_19.png | 5五将棋の筋(１から５)に使用する画像 |
| number\_v1\_22\_530.png | 5五将棋の段(一から五)に使用する画像 |
| number\_v2\_485\_19.png | 5五将棋の筋(1から5)に使用する画像 |
| number\_v2\_22\_530.png | 5五将棋の段(aからe)に使用する画像 |

## 対応環境

- Ubuntu 18.04

## 前提作業

実行する前に、以下のパッケージをインストールして下さい。

* python3
* python3-opencv
* python3-pil
* python3-numpy

また、下記を実行し /usr/bin/python3.6 を選択することによって、
python3をデフォルトのpythonにすることができます。

    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
    $ sudo update-alternatives --config python

## 使い方

(1) 作業用ディレクトリに移動し、本レポジトリを取得します。

    $ cd <作業用ディレクトリ>
    $ git clone https://github.com/tsugibayashi/create_numbers

(2) スクリプト "create\_numbers.sh" を実行し、画像を生成します。

    $ cd create_numbers/
    $ ./create_numbers.sh <画像の種類>

| 画像の種類 | 説明 |
----|----
| normal | hand\_number\_v1\_864\_96.pngを生成する |
| box | hand\_box\_number\_v1\_864\_96.pngを生成する |
| row1 | number\_v1\_873\_19.pngを生成する |
| column1 | number\_v1\_22\_954.pngを生成する |
| row2 | number\_v2\_873\_19.pngを生成する |
| column2 | number\_v2\_22\_954.pngを生成する |
| 55-row1 | number\_v1\_485\_19.pngを生成する |
| 55-column1 | number\_v1\_22\_530.pngを生成する |
| 55-row2 | number\_v2\_485\_19.pngを生成する |
| 55-column2 | number\_v2\_22\_530.pngを生成する |

(3) ./images/ に移動し、画像データ \*.png を MyShogiにコピーします。

    $ cd images/
    $ cp -pv *.png <MyShogiのインストール先>/image/

## 各画像ファイルの説明

| ファイル名 | 説明 |
----|----
| hand\_number\_v1\_864\_96.png | 駒台に置かれた駒の数を表す画像 |
| hand\_box\_number\_v1\_864\_96.png | 駒箱に置かれた駒の数を表す画像 |
| number\_v1\_873\_19.png | 将棋盤の筋(１から９)に使用する画像 |
| number\_v1\_22\_954.png | 将棋盤の段(一から九)に使用する画像 |
| number\_v2\_873\_19.png | 将棋盤の筋(1から9)に使用する画像 |
| number\_v2\_22\_954.png | 将棋盤の段(aからi)に使用する画像 |
| number\_v1\_485\_19.png | 5五将棋の筋(１から５)に使用する画像 |
| number\_v1\_22\_530.png | 5五将棋の段(一から五)に使用する画像 |
| number\_v2\_485\_19.png | 5五将棋の筋(1から5)に使用する画像 |
| number\_v2\_22\_530.png | 5五将棋の段(aからe)に使用する画像 |

## ライセンス

Apache-2.0 License


以上

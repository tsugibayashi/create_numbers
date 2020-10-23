# create_shogi_pieces

## 概要

本ソフトウェアを使って、[MyShogi](https://github.com/yaneurao/MyShogi)の画像 hand_number_v1_864_96.png を作成することができます。

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

(2) スクリプト "create_numbers.sh" を実行し、画像を生成します。

    $ cd create_numbers/
    $ ./create_numbers.sh <画像の種類>

| 画像の種類 | 説明 |
----|----
| normal | hand_number_v1_864_96.pngを生成する |
| box | hand_box_number_v1_864_96.pngを生成する |

(3) ./images/ に移動し、画像データ hand_number_v1_864_96.png を MyShogiにコピーします。

    $ cd images/
    $ cp -pv hand_number_v1_864_96.png <MyShogiのインストール先>/image/

## 各画像ファイルの説明

| ファイル名 | 説明 |
----|----
| hand_number_v1_864_96.png | 駒台に置かれた駒の数を表す画像 |
| hand_box_number_v1_864_96.png | 駒箱に置かれた駒の数を表す画像 |

## ライセンス

Apache-2.0 License


以上

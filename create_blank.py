#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import cv2
import numpy

### variables
output = './tmp/blank.png'

# 引数から、画像のサイズを取得する
args = sys.argv
width = int(args[1])
height = int(args[2])

# 出力用のブランク画像の作成
img = numpy.zeros((height, width, 3), numpy.uint8)
 # 全データ (x, y, BGR) の値を 白色に指定する
img[:, :, :] = 255

# img にアルファチャンネルを追加した画像 img_output を作成する
img_output = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

# img に対して白色の位置を 透過色(アルファチャンネルの値が0) に設定する
img_output[:, :, 3] = numpy.where(numpy.all(img == 255, axis=-1), 0, 255)

### img_output の保存
cv2.imwrite(output, img_output)


#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image

### functions
def print_usage():
    print('[使い方]')
    print('      $ python rotate_number.py <数字>')
    print('  例. $ python rotate_number.py 1')

# 引数から、画像に描く数字(number) を取得する
args = sys.argv
number = args[1]

# 引数に数字が指定されているか判定する
if ( not number.isdecimal() ):
    print('[Error] 引数に数字が指定されていない')
    print_usage()
    sys.exit()

# 入力ファイル
input_filename = './tmp/number_' + number + '.png'

# 保存するファイル名
output         = './tmp/rotated_number_' + number + '.png'


### main routine
# 画像の読み込み
img = Image.open(input_filename)

# 画像のリサイズ
img_rotate = img.rotate(180)

# リサイズした画像の保存
img_rotate.save(output)


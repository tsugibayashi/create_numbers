#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont

### functions
def print_usage():
    print('[使い方]')
    print('      $ python draw_number.py <数字>')
    print('  例. $ python draw_number.py 1')


### variables
# 入力ファイル
input_filename = './tmp/blank.png'

# 枠線の色
box_color  = (0, 0, 0)         #黒色
# 塗りつぶす色
fill_color = (255, 255, 255)   #白色

# フォント
font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipag.ttf"  #IPAゴシック
#font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"  #IPA明朝

# フォントサイズ
font_size = 40

# フォントの色 (R,G,B)
font_color1 = (0, 0, 0)      #黒色
#font_color1 = (180, 65, 21)  #朱色

# 引数から、画像に描く数字(number) を取得する
args = sys.argv
number = args[1]

# 引数に数字が指定されているか判定する
if ( not number.isdecimal() ):
    print('[Error] 引数に数字が指定されていない')
    print_usage()
    sys.exit()

# 半角数字1から9 を 全角数字に変換
if (number == '1'):
    text1 = '１'
elif (number == '2'):
    text1 = '２'
elif (number == '3'):
    text1 = '３'
elif (number == '4'):
    text1 = '４'
elif (number == '5'):
    text1 = '５'
elif (number == '6'):
    text1 = '６'
elif (number == '7'):
    text1 = '７'
elif (number == '8'):
    text1 = '８'
elif (number == '9'):
    text1 = '９'
else:
    text1 = number

# 出力ファイル
output = './tmp/number_' + number + '.png'


### main routine
# 画像の読み込み
img = Image.open(input_filename)
draw = PIL.ImageDraw.Draw(img)

# 枠線を描く
draw.rectangle([(5, 5), (img.size[0]-5, img.size[1]-5)], 
               fill=fill_color, outline=box_color)

# フォント
font = PIL.ImageFont.truetype(font_ttf, font_size) 

# テキストの大きさを取得
text_size1 = font.getsize(text1)

# 文字の場所
text_pos1 = ((img.size[0] - text_size1[0]) / 2, 
             (img.size[1] - text_size1[1]) / 2)

# 文字を描く
draw.text(text_pos1, text1, font=font, fill=font_color1)

# 画像の保存
img.save(output)


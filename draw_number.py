#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont

### functions
def print_usage():
    print('[使い方]')
    print('      $ python draw_number.py <種類> <数字>')
    print('  例. $ python draw_number.py normal 1')


### variables
# 入力ファイル
input_filename = './tmp/blank.png'

# フォント
font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipag.ttf"  #IPAゴシック
#font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"  #IPA明朝

# 引数から、画像に描く数字(number) を取得する
args = sys.argv
type = args[1]
number = args[2]

# 引数に数字が指定されているか判定する
if ( not number.isdecimal() ):
    print('[Error] 引数に数字が指定されていない')
    print_usage()
    sys.exit()

if type == 'normal' or type == 'row1' or type == '55-row1':
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
elif type == 'column1' or type == '55-column1':
    # 半角数字1から9 を 漢字に変換
    if (number == '1'):
        text1 = '一'
    elif (number == '2'):
        text1 = '二'
    elif (number == '3'):
        text1 = '三'
    elif (number == '4'):
        text1 = '四'
    elif (number == '5'):
        text1 = '五'
    elif (number == '6'):
        text1 = '六'
    elif (number == '7'):
        text1 = '七'
    elif (number == '8'):
        text1 = '八'
    elif (number == '9'):
        text1 = '九'
    else:
        text1 = number
elif type == 'row2' or type == '55-row2':
    # 半角数字1から9
    text1 = number
elif type == 'column2' or type == '55-column2':
    # 半角数字1から9 を アルファベットに変換
    if (number == '1'):
        text1 = 'a'
    elif (number == '2'):
        text1 = 'b'
    elif (number == '3'):
        text1 = 'c'
    elif (number == '4'):
        text1 = 'd'
    elif (number == '5'):
        text1 = 'e'
    elif (number == '6'):
        text1 = 'f'
    elif (number == '7'):
        text1 = 'g'
    elif (number == '8'):
        text1 = 'h'
    elif (number == '9'):
        text1 = 'i'
    else:
        text1 = number

# フォントサイズ
if type == 'normal':
    font_size = 48
elif type == 'row1' or type == 'row2':
    font_size = 20
elif type == 'column1' or type == 'column2':
    font_size = 20
elif type == '55-row1' or type == '55-row2':
    font_size = 20
elif type == '55-column1' or type == '55-column2':
    font_size = 20

# フォントの色 (R,G,B)
if type == 'normal':
    font_color1 = (180, 65, 21)  #朱色
elif type == 'row1' or type == 'row2':
    font_color1 = (0, 0, 0)      #黒色
elif type == 'column1' or type == 'column2':
    font_color1 = (0, 0, 0)      #黒色
elif type == '55-row1' or type == '55-row2':
    font_color1 = (0, 0, 0)      #黒色
elif type == '55-column1' or type == '55-column2':
    font_color1 = (0, 0, 0)      #黒色

# 出力ファイル
output = './tmp/number_' + number + '.png'


### main routine
# 画像の読み込み
img = Image.open(input_filename)
draw = PIL.ImageDraw.Draw(img)

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


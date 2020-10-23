#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import cv2
import numpy as np

### functions
def print_usage():
    print('[使い方]')
    print('      $ python concat_numbers.py')

# def hconcat_18files (output, file1, file2, file3, file4, file5, \
#                              file6, file7, file8, file9, file10, \
#                              file11, file12, file13, file14, file15, \
#                              file16, file17, file18):
# {{{
def hconcat_18files (output, file1, file2, file3, file4, file5, \
                             file6, file7, file8, file9, file10, \
                             file11, file12, file13, file14, file15, \
                             file16, file17, file18):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)
    img3 = cv2.imread(file3, -1)
    img4 = cv2.imread(file4, -1)
    img5 = cv2.imread(file5, -1)
    img6 = cv2.imread(file6, -1)
    img7 = cv2.imread(file7, -1)
    img8 = cv2.imread(file8, -1)
    img9 = cv2.imread(file9, -1)
    img10 = cv2.imread(file10, -1)
    img11 = cv2.imread(file11, -1)
    img12 = cv2.imread(file12, -1)
    img13 = cv2.imread(file13, -1)
    img14 = cv2.imread(file14, -1)
    img15 = cv2.imread(file15, -1)
    img16 = cv2.imread(file16, -1)
    img17 = cv2.imread(file17, -1)
    img18 = cv2.imread(file18, -1)

    # 画像を水平結合する
    img_h = cv2.hconcat([img1,  img2])
    img_h = cv2.hconcat([img_h, img3])
    img_h = cv2.hconcat([img_h, img4])
    img_h = cv2.hconcat([img_h, img5])
    img_h = cv2.hconcat([img_h, img6])
    img_h = cv2.hconcat([img_h, img7])
    img_h = cv2.hconcat([img_h, img8])
    img_h = cv2.hconcat([img_h, img9])
    img_h = cv2.hconcat([img_h, img10])
    img_h = cv2.hconcat([img_h, img11])
    img_h = cv2.hconcat([img_h, img12])
    img_h = cv2.hconcat([img_h, img13])
    img_h = cv2.hconcat([img_h, img14])
    img_h = cv2.hconcat([img_h, img15])
    img_h = cv2.hconcat([img_h, img16])
    img_h = cv2.hconcat([img_h, img17])
    img_h = cv2.hconcat([img_h, img18])

    # 結合した画像を保存する
    cv2.imwrite(output, img_h)
# }}}

# def vconcat_2files (output, file1, file2):
# {{{
def vconcat_2files (output, file1, file2):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)

    # 画像を垂直結合する
    img_v = cv2.vconcat([img1,  img2])

    # 結合した画像を保存する
    cv2.imwrite(output, img_v)
# }}}


### main routine
# 出力ファイル名
output1 = './tmp/hconcat1.png'
output2 = './tmp/hconcat2.png'

# 引数から、出力ファイル名を判断する
args = sys.argv
output_name = args[1]
if (output_name == 'normal'):
    output  = './images/hand_number_v1_864_96.png'
else:
    output  = './images/hand_box_number_v1_864_96.png'

# 画像ファイル名
# 1段目
filename1 = './tmp/number_1.png'
filename2 = './tmp/number_2.png'
filename3 = './tmp/number_3.png'
filename4 = './tmp/number_4.png'
filename5 = './tmp/number_5.png'
filename6 = './tmp/number_6.png'
filename7 = './tmp/number_7.png'
filename8 = './tmp/number_8.png'
filename9 = './tmp/number_9.png'
filename10 = './tmp/number_10.png'
filename11 = './tmp/number_11.png'
filename12 = './tmp/number_12.png'
filename13 = './tmp/number_13.png'
filename14 = './tmp/number_14.png'
filename15 = './tmp/number_15.png'
filename16 = './tmp/number_16.png'
filename17 = './tmp/number_17.png'
filename18 = './tmp/number_18.png'

# 2段目
filename19 = './tmp/rotated_number_18.png'
filename20 = './tmp/rotated_number_17.png'
filename21 = './tmp/rotated_number_16.png'
filename22 = './tmp/rotated_number_15.png'
filename23 = './tmp/rotated_number_14.png'
filename24 = './tmp/rotated_number_13.png'
filename25 = './tmp/rotated_number_12.png'
filename26 = './tmp/rotated_number_11.png'
filename27 = './tmp/rotated_number_10.png'
filename28 = './tmp/rotated_number_9.png'
filename29 = './tmp/rotated_number_8.png'
filename30 = './tmp/rotated_number_7.png'
filename31 = './tmp/rotated_number_6.png'
filename32 = './tmp/rotated_number_5.png'
filename33 = './tmp/rotated_number_4.png'
filename34 = './tmp/rotated_number_3.png'
filename35 = './tmp/rotated_number_2.png'
filename36 = './tmp/rotated_number_1.png'

# 18個の画像を結合する
hconcat_18files(output1, filename1, filename2, filename3, filename4, \
                filename5, filename6, filename7, filename8, filename9, \
                filename10, filename11, filename12, filename13, filename14, \
                filename15, filename16, filename17, filename18)

hconcat_18files(output2,  filename19, filename20, filename21, filename22, \
                filename23, filename24, filename25, filename26, filename27, \
                filename28, filename29, filename30, filename31, filename32, \
                filename33, filename34, filename35, filename36)

# 2つの画像を結合する
vconcat_2files(output, output1, output2)


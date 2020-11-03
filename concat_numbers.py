#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import cv2
import numpy as np

### functions
def print_usage():
    print('[使い方]')
    print('      $ python concat_numbers.py <種類>')
    print('  例. $ python concat_numbers.py normal')

def hconcat_2files (output, file1, file2):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)
    # 画像を水平結合する
    img_h = cv2.hconcat([img1,  img2])
    # 結合した画像を保存する
    cv2.imwrite(output, img_h)

def vconcat_2files (output, file1, file2):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)
    # 画像を垂直結合する
    img_v = cv2.vconcat([img1,  img2])
    # 結合した画像を保存する
    cv2.imwrite(output, img_v)

### main routine
# 出力ファイル名
output1 = './tmp/hconcat1.png'
output2 = './tmp/hconcat2.png'

# 引数から、出力ファイル名を判断する
args = sys.argv
output_name = args[1]
if output_name == 'normal':
    output  = './images/hand_number_v1_864_96.png'
elif output_name == 'box':
    output  = './images/hand_box_number_v1_864_96.png'
elif output_name == 'row1':
    output = './images/number_v1_873_19.png'
elif output_name == 'column1':
    output = './images/number_v1_22_954.png'
elif output_name == 'row2':
    output = './images/number_v2_873_19.png'
elif output_name == 'column2':
    output = './images/number_v2_22_954.png'
elif output_name == '55-row1':
    output = './images/number_v1_485_19.png'
elif output_name == '55-column1':
    output = './images/number_v1_22_530.png'
elif output_name == '55-row2':
    output = './images/number_v2_485_19.png'
elif output_name == '55-column2':
    output = './images/number_v2_22_530.png'

# 画像ファイル名
if output_name == 'normal' or output_name == 'box':
    # 1段目
    filename1 = []
    for i in range(1,19):
        filename1.append('./tmp/number_' + str(i) + '.png')
    # 2段目
    filename2 = []
    for i in range(18,0,-1):
        filename2.append('./tmp/rotated_number_' + str(i) + '.png')
elif output_name == 'row1' or output_name == 'row2':
    filename1 = []
    for i in range(9,0,-1):
        filename1.append('./tmp/number_' + str(i) + '.png')
elif output_name == 'column1' or output_name == 'column2':
    filename1 = []
    for i in range(1,10):
        filename1.append('./tmp/number_' + str(i) + '.png')
elif output_name == '55-row1' or output_name == '55-row2':
    filename1 = []
    for i in range(5,0,-1):
        filename1.append('./tmp/number_' + str(i) + '.png')
elif output_name == '55-column1' or output_name == '55-column2':
    filename1 = []
    for i in range(1,6):
        filename1.append('./tmp/number_' + str(i) + '.png')

if output_name == 'normal' or output_name == 'box':
    # 18個の画像を結合する
    hconcat_2files(output1, filename1[0], filename1[1])
    for i in range(2,18):
        hconcat_2files(output1, output1, filename1[i])
    # 18個の画像を結合する
    hconcat_2files(output2, filename2[0], filename2[1])
    for i in range(2,18):
        hconcat_2files(output2, output2, filename2[i])
    # 2つの画像を結合する
    vconcat_2files(output, output1, output2)
elif output_name == 'row1' or output_name == 'row2':
    # 9個の画像を結合する
    hconcat_2files(output, filename1[0], filename1[1])
    for i in range(2,9):
        hconcat_2files(output, output, filename1[i])
elif output_name == 'column1' or output_name == 'column2':
    # 9個の画像を結合する
    vconcat_2files(output, filename1[0], filename1[1])
    for i in range(2,9):
        vconcat_2files(output, output, filename1[i])
elif output_name == '55-row1' or output_name == '55-row2':
    # 5個の画像を結合する
    hconcat_2files(output, filename1[0], filename1[1])
    for i in range(2,5):
        hconcat_2files(output, output, filename1[i])
elif output_name == '55-column1' or output_name == '55-column2':
    # 5個の画像を結合する
    vconcat_2files(output, filename1[0], filename1[1])
    for i in range(2,5):
        vconcat_2files(output, output, filename1[i])


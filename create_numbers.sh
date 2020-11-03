#!/bin/bash

# ディレクトリ作成
if [ ! -d images ]; then
    mkdir -v images
fi
if [ ! -d tmp ]; then
    mkdir -v tmp
fi

case $1 in
    normal|box|row1|column1|row2|column2)
        ACTION=$1
    ;;
    55-row1|55-column1|55-row2|55-column2)
        ACTION=$1
    ;;
    *)
        echo '[Error] input $1, action'
        echo '  normal     : 枠のない数字の画像を出力する'
        echo '  box        : 枠に囲まれた数字の画像を出力する'
        echo '  row1       : 将棋盤の筋(１から９)に使用するための画像を出力する'
        echo '  column1    : 将棋盤の段(一から九)に使用するための画像を出力する'
        echo '  row2       : 将棋盤の筋(1から9)に使用するための画像を出力する'
        echo '  column2    : 将棋盤の段(aからi)に使用するための画像を出力する'
        echo '  55-row1    : 55将棋の筋(１から５)に使用するための画像を出力する'
        echo '  55-column1 : 55将棋の段(一から五)に使用するための画像を出力する'
        echo '  55-row2    : 55将棋の筋(1から5)に使用するための画像を出力する'
        echo '  55-column2 : 55将棋の段(aからe)に使用するための画像を出力する'
        exit 1
    ;;
esac

case $ACTION in
    normal|box)
        # 何も書かれていない画像 (48x48) を作成する
        python create_blank.py 48 48
    ;;
    row1|row2|55-row1|55-row2)
        # 何も書かれていない画像 (97x19) を作成する
        python create_blank.py 97 19
    ;;
    column1|column2|55-column1|55-column2)
        # 何も書かれていない画像 (22x106) を作成する
        python create_blank.py 22 106
    ;;
esac

# 文字の書かれた画像を作成する
case $ACTION in
    normal)
        for i in `seq 1 18`; do
            python draw_number.py $ACTION $i
        done
    ;;
    box)
        for i in `seq 1 18`; do
            python draw_box_number.py $i
        done
    ;;
    row1|column1)
        for i in `seq 1 9`; do
            python draw_number.py $ACTION $i
        done
    ;;
    row2|column2)
        for i in `seq 1 9`; do
            python draw_number.py $ACTION $i
        done
    ;;
    55-row1|55-column1)
        for i in `seq 1 5`; do
            python draw_number.py $ACTION $i
        done
    ;;
    55-row2|55-column2)
        for i in `seq 1 5`; do
            python draw_number.py $ACTION $i
        done
    ;;
esac

# 180度回転した画像を作成する
case $ACTION in
    normal|box)
        for i in `seq 1 18`; do
            python rotate_number.py $i
        done
    ;;
esac

# 作成した全ての画像を結合し、出力する
python concat_numbers.py $ACTION


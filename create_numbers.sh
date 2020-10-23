#!/bin/bash

# ディレクトリ作成
if [ ! -d images ]; then
    mkdir -v images
fi
if [ ! -d tmp ]; then
    mkdir -v tmp
fi

# 引数に normal が指定されていると、枠のない数字の画像を出力する
# 引数に box が指定されていると、枠に囲まれた数字の画像を出力する
case $1 in
    normal)
        ACTION='normal'
    ;;
    box)
        ACTION='box'
    ;;
    *)
        ACTION='normal'
    ;;
esac

# 何も書かれていない画像 (48x48) を作成する
python create_blank.py

# 文字の書かれた画像を作成する
if [ $ACTION = 'box' ]; then
    for i in `seq 1 18`; do
        python draw_box_number.py $i
    done
else
    for i in `seq 1 18`; do
        python draw_number.py $i
    done
fi

# 180度回転した画像を作成する
for i in `seq 1 18`; do
    python rotate_number.py $i
done

# 作成した全ての画像を結合し、出力する
python concat_numbers.py $ACTION


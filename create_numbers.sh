#!/bin/bash

# ディレクトリ作成
if [ ! -d images ]; then
    mkdir -v images
fi
if [ ! -d tmp ]; then
    mkdir -v tmp
fi

# 何も書かれていない画像 (48x48) を作成する
python create_blank.py

# 文字の書かれた画像を作成する
for i in `seq 1 18`; do
    python draw_number.py $i
done

# 180度回転した画像を作成する
for i in `seq 1 18`; do
    python rotate_number.py $i
done

# 作成した全ての画像を結合する
python concat_numbers.py


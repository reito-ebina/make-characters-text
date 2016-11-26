# -*- coding: utf-8 -*-

import sys
import os
import chardet

from os.path import join, splitext, split

# 入力ディレクトリと出力ディレクトリを指定
readdir = sys.argv[1]
outdir = sys.argv[2]

print "readdir:\t", readdir
print "outdir:\t", outdir

# ディレクトリのファイル一覧を取得
txts = os.listdir(readdir)

for txt in txts:
    if not (txt.split(".")[-1] == "txt"):   # 拡張子がtxt以外を無視
        continue
    txt = os.path.join(readdir, txt)
    print txt

    fp = open(txt, "rb")

    # ファイルの文字コードを取得
    f_encode = chardet.detect(fp.read())["encoding"]

    fp = open(txt, "rb")
    lines = fp.readlines()

    for line in lines:
        # unicodeに変換
        line_u = unicode(line, f_encode)

        # キャラ名を取得
        char_name = line_u[:line_u.find(u"「")]
        outfname = os.path.join(outdir, char_name + ".txt")

        # キャラ名のファイルがあるかどうか確認
        if os.path.exists(outfname):
            # ある場合は上書きモードで
            outfp = open(outfname, "a")
        else:
            # ない場合は新規作成
            outfp = open(outfname, "w")

        # セリフのみ抽出
        line_format = line_u[line_u.find(u"「") + 1:line_u.find(u"」")] + "\n"
        # セリフ書き込み
        outfp.write(line_format.encode("utf-8"))

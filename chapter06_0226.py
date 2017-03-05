#coding:utf-8

import codecs
import csv
import nltk
import pandas as pd
import numpy as np
import re

def data_loader():

	f = open("./nlp.txt","rb")
	nlp_data = f.read()
	print nlp_data

	return nlp_data


def task_50(nlp_data):

	# 50. 文区切り
	# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

	fin = codecs.open('nlp.txt', 'r', 'utf_8')
	# punctuation = ""

	# パターンを以下で定義
	pattern = r'\.\s[A-Z]|\;\s[A-Z]|\:\s[A-Z]|\?\s[A-Z]|\!\s[A-Z]'
	"""
	(参照) http://kenichia.hatenablog.com/entry/2016/02/15/174813
	正規表現の意味
	\ => ここから始まり
	\s => スペース(空白文字)
	[A-Z] => 英大文字
	| => または
	つまり、".などの記号+スペース+英大文字"の組み合わせをorで4種類作っているということ
	若干これは冗長な気がする。記号の部分をひとつにまとめられたらきっともっとすっきりするはず。
	"""
	regex = re.compile(pattern)
	print regex.match(fin)


	return



if __name__ == '__main__':
	nlp_data = data_loader()
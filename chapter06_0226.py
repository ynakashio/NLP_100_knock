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
	# print nlp_data

	return nlp_data


def task_50(nlp_data):

	# 50. 文区切り
	# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

	pattern = r'\.\s[A-Z]|\;\s[A-Z]|\:\s[A-Z]|\?\s[A-Z]|\!\s[A-Z]'
	sentences = re.finditer(pattern, nlp_data)

	index_list=[]
	sentence_list = []
	for i,so in enumerate(sentences):
		if i == 0:
			_0_index = so.end()-1
			sentence_list.extend([nlp_data[:_0_index].rstrip()])

			print nlp_data[:_0_index].rstrip()
			index_list.extend([_0_index])

		else:
			start_index = index_list[i-1]
			end_index = so.end()-1
			sentence_list.extend([nlp_data[start_index:end_index]])

			print nlp_data[start_index:end_index]
			index_list.extend([end_index])

	"""
	* パターンの定義の仕方
	pattern = r'\.\s[A-Z]|\;\s[A-Z]|\:\s[A-Z]|\?\s[A-Z]|\!\s[A-Z]'

	(参照) http://kenichia.hatenablog.com/entry/2016/02/15/174813

	* 正規表現の意味
	\ => ここから始まり
	\s => スペース(空白文字)
	[A-Z] => 英大文字
	| => または

	つまり、".などの記号+スペース+英大文字"の組み合わせをorで4種類作っているということ
	若干これは冗長な気がする。記号の部分をひとつにまとめられたらきっともっとすっきりするはず。
	"""

	"""
	* 正規表現で文字列を探すとき
	(参照)http://qiita.com/wanwanland/items/ce272419dde2f95cdabc
		- re.split()は、patternを削除して分割する
		- re.match/search/findall/finditer とかの使い分けが大事
	"""

	return sentence_list


def task_51(sentence_list):

	"""
	51. 単語の切り出し
	空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
	"""

	word_list = []
	for sentence in sentence_list:
		for word in re.split(" ", sentence):
			if word[:-1] == ".":
				print word,"\n"

				eos_word = word+"\n"
				word_list.extend([eos_word])
			else:
				print word
				word_list.extend([word])

	return word_list


def task_52(word_list):


	return


if __name__ == '__main__':
	nlp_data = data_loader()
	sentence_list = task_50(nlp_data)
	word_list = task_51(sentence_list)
	task_52(word_list)


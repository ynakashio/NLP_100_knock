#coding:utf-8

import csv
import codecs
import numpy as np
from nltk import tokenize
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import pandas as pd


# ひとまず早いのでnltkで実装してみる。
# 余裕があれば Stanford coreNLPを使ってみるということで。。


def data_loader():

	input_name = './sample.txt'
	# file_name = "./enwiki-20150112-400-r100-10576.txt"
	f = codecs.open(input_name, "r","utf-8")
	wiki_data = str(f.read()).decode("utf-8")
	f.close

	return wiki_data


def task_80(wiki_data):

	"""
	80. コーパスの整形
	文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．
    トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
    空文字列となったトークンは削除
	以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
	"""

	# これを参考にした
	# => http://qiita.com/segavvy/items/ea485e66dd96eee891da

	output_name = './80_sample.txt'

	word_list=[]
	for chunk in wiki_data.split(' '):
		token = chunk.strip('.,!?;:()[]\'"').strip()
		if len(token) > 0:
			word_list.append(str(token))

	output_str = ""
	for word in word_list:
		output_str = output_str + " " + word
	print output_str
	f = open(output_name,"w")
	f.write(output_str)
	f.close

	# 以下は正規表現でやろうとして失敗。誰か教えてくださいw
	# for tokenized_word in tokenize.word_tokenize(wiki_data):
	# 	word_list.append(re.sub(re.compile(".,!?;:()\[]"), "", str(tokenized_word)))

	return


def task_81(wiki_data):

	"""
	81. 複合語からなる国名への対処
	英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
	そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．
	しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．
	インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
	"""
	# 国名かここから
	# http://www.listofcountriesoftheworld.com/

	# tokenizeして、一単語目が同じだったらくっつけるメソッド


	country_name_file = "./country_name.txt"
	f = open(country_name_file,"r")
	countries = f.read()

	# 一単語目をkey、単語全体をvalueとして入れている
	country_name_dic = {}
	for name in countries.split("\n"):
		if len(name.split(" ")) > 2:
			country_name_dic.update({name.split(" ")[0]:name})
	print "以下を単語辞書としてマッチさせる\n",country_name_dic

	# とりあえず先に進む

	return

def task_82()


	return

if __name__ == '__main__':
	wiki_data = data_loader()
	# task_80(wiki_data)
	task_81(wiki_data)
	task_82(wiki_data)




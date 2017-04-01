#coding:utf-8

import csv
import codecs
from collections import Counter,OrderedDict
from itertools import chain
import random
import numpy as np
from nltk import tokenize
import os
from sklearn.decomposition import PCA
import pickle
from scipy import sparse, io
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

	word_list=[]
	for chunk in wiki_data.split(' '):
		token = chunk.strip('.,!?;:()[]\'"').strip()
		if len(token) > 0:
			word_list.append(str(token))

	output_str = ""
	for word in word_list:
		output_str = output_str + " " + word
	print output_str

	output_name = './80_sample.txt'
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

	"""
	ここのコード・考え方を参照している
	http://qiita.com/segavvy/items/216888c3549cea3d8e81

	国名一覧を読み込んで集合と辞書作成、ただし1語の国は含めない。
	辞書には{ 最初の1語, [全体の語数1, 全体の語数2...] }を登録し、
	全体の語数は降順でソートして格納する。
	たとえば最初の1語が'United'の国は次の6つある。
		United States of America
		United Mexican States
		United Kingdom of Great Britain and Northern Ireland
		United Arab Emirates
		United Republic of Tanzania
		United States
	この場合、全体の語数が4語、3語、8語、2語のものがあるので、
	辞書には { 'United', [8, 4, 3, 2] } を登録する。
	全体の個数を降順ソートするのは最長一致でマッチングさせるため。
	"""

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


def task_82(wiki_data):

	"""
	82. 文脈の抽出
	81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
    ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
    単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
	"""

	# つまり、全ての単語に対して、文脈幅dをランダムに選んで表示するという問題?

	f = open("./80_sample.txt","r")
	wiki_data = f.read()

	# リストにして配列番号で処理
	splited_data = wiki_data.split(" ")

	output_string = ""
	for target_index,target_word in enumerate(splited_data):

		plut_count = random.randint(1,5)
		minus_count = 0 - int(plut_count)

		for i in range(minus_count,plut_count):
			if i != 0:
				context_index = int(target_index)+int(i)

				try:
					tab_separted_context = target_word+"\t"+splited_data[context_index]+"\n"
					output_string = output_string + tab_separted_context
					print target_word,"\t",splited_data[context_index],"\n"
				except:
					print context_index,"nan"
	print output_string

	output_file = "82_sample.txt"
	g = open(output_file,"w")
	g.write(output_string)

	print "Alexanderなどバグ取りがまだ"

	return


def task_83(wiki_data):

	"""
	83. 単語／文脈の頻度の計測
	82の出力を利用し，以下の出現分布，および定数を求めよ．
    f(t,c):	単語tと文脈語cの共起回数
    f(t,∗):	単語tの出現回数
	f(∗,c):	文脈語cの出現回数
	N: 		単語と文脈語のペアの総出現回数
	"""
	# input_file = "resample.txt"
	input_file = "./82_sample.txt"
	f = open(input_file,"r")
	tabbed_context = f.read()

	# 任意の組み合わせについて、上記の4種類を計算するという感じ

	# 組み合わせを作る => Counter使ったら楽そう
	tabbed_list = []
	for context in tabbed_context.split("\n"):
		context_tmp = [i.lower() for i in context.split("\t")]
		context_tmp = tuple(context_tmp)
		tabbed_list.append(context_tmp)
	print len(tabbed_list),"=>",len(set(tabbed_list))
	collocated_list = set(filter(lambda x: len(x)>1,tabbed_list))

	frequency_list=[]
	for collocation in collocated_list:
		# print collocation,"の組み合わせをチェックする"
		_search = collocation[0]+"\t"+collocation[1]

		# print "f(t,c):\t",tabbed_context.count(_search)
		# print "f(t,*):\t",tabbed_context.count(collocation[0])
		# print "f(*,c):\t",tabbed_context.count(collocation[1])
		tmp = [_search,tabbed_context.count(_search),tabbed_context.count(collocation[0]),tabbed_context.count(collocation[1])]
		frequency_list.append(tmp)

	print frequency_list
	print "N:",len(tabbed_list)

	output_file = "./83_sample.csv"
	g = open(output_file,"w")
	g.write(str(len(tabbed_list)))
	g.write("\n")

	writer=csv.writer(g)
	for i in frequency_list:
		writer.writerow(i)
	g.close

	return

def task_84(wiki_data):

	"""
	84. 単語文脈行列の作成
	83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
	f(t,c)≥10 ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
	f(t,c)<10 ならば，Xtc=0
	ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
	"""

	# 一部ここを参考にした
	# http://qiita.com/segavvy/items/21455b802e34a9e49f92d
	# http://d.hatena.ne.jp/billest/20090906/1252269157

	N = int(87867)

	# 一行目を削除してからファイルを開いてください
	input_file = "./83_sample.csv"
	freq_df = pd.read_csv(input_file,header=None)
	freq_df.columns = ["collocation","tc","t*","*c"]
	# print freq_df
	over10_df = freq_df.query("tc >= 10")
	under10_df = freq_df.query("tc < 10")
	print len(freq_df),"のうち計算するのは",len(over10_df),"だけ"

	def calc_PPMI(tc_list):
		N = int(87867)
		return max(np.log(N*tc_list[1]/tc_list[1]*tc_list[2]),0)

	_dic = {}
	for i,tc_row in over10_df.iterrows():
		_dic.update({tc_row[0]:{"ppmi":calc_PPMI(tc_row.tolist())}})
	ppmi_df = pd.DataFrame.from_dict(_dic).T

	freq_df["term"] = freq_df["collocation"].str.split("\t").apply(lambda x: x[0])
	freq_df["col"] = freq_df["collocation"].str.split("\t").apply(lambda x: x[1])

	dict_index_t = OrderedDict((key, i) for i, key in enumerate(set(freq_df["term"].tolist())))
	dict_index_c = OrderedDict((key, i) for i, key in enumerate(set(freq_df["col"].tolist())))

	size_t = len(dict_index_t)
	size_c = len(dict_index_c)
	matrix_x = sparse.lil_matrix((size_t, size_c))

	for k, f_tc in freq_df.iterrows():
		if f_tc.tolist()[1] >= 10:
			ppmi = calc_PPMI(f_tc.tolist())
			matrix_x[dict_index_t[f_tc[4]], dict_index_c[f_tc[5]]] = ppmi
	# print matrix_x

	fname_matrix_x = 'matrix_x'
	io.savemat(fname_matrix_x, {'matrix_x': matrix_x})
	print matrix_x

	fname_dict_index_t = 'dict_index_t'
	with open(fname_dict_index_t, 'w') as data_file:
	    pickle.dump(dict_index_t, data_file)

	return


def task_85(wiki_data):

	"""
	85. 主成分分析による次元圧縮
	84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
	"""
	input_name = "./84_sample.csv"
	main_df = pd.read_csv()

	pca = PCA(n_components=2)
	pca.fit(X)
	print pca.get_covariance()

	return



if __name__ == '__main__':
	wiki_data = data_loader()
	# task_80(wiki_data)
	# task_81(wiki_data)
	task_82(wiki_data)
	# task_83(wiki_data)
	task_84(wiki_data)
	# task_85(wiki_data)


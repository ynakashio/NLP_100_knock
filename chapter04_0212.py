#coding:utf-8

import pandas as pd
import sys
# sys.setdefaultencoding("utf-8")
import MeCab
import codecs
from nltk.tokenize import word_tokenize


def import_Mecab_file():

	"""
	調べたところ -> http://tech.mof-mof.co.jp/blog/mecab-install.html
	mecab neko.txt -Ochasen > neko.txt.mecab
	上記のコマンド1つでファイルができるようです。
	"""

	f = codecs.open("neko.txt","r","utf-8")
	neko_data = str(f.read())
	# MeCab.Taggerはstr型しか受け取らない？ここは要確認。
	f.close

	tagger = MeCab.Tagger('-Ochasen')
	# tagger = MeCab.Tagger('mecabrc')
	print sys.getdefaultencoding()
	taggered_result = tagger.parse(neko_data)

	g = open("neko.txt.mecab","w")
	g.write(taggered_result)
	g.close

	return


def task_30():

	"""
	30. 形態素解析結果の読み込み
	形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

	この"マッピング型"というのは、pythonの辞書型を指すみたいです。
	つまり、表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）の4つをキーとして、単語をidentifyする辞書を作るということのよう。
	"""

	# f = open("neko.txt.mecab","r")
	f = open("mecab_sample.mecab","r")
	neko_pos_data = f.read()
	# readlinesはリスト型で返す。その代わり、リスト内のindexを指定すればutf-8で表示。

	print "形態素解析された後の単語の数は",len(neko_pos_data),"個"

	sentence_dict={}
	for i,sentence in enumerate(neko_pos_data.split("EOS")[2:]):
		print i,"番目のsentenceを操作中..."
		splited_list = sentence.split("\t")[0:4]

		pos_dict={}
		if len(splited_list)>1:
			for j,taggered in enumerate(splited_list):
				pos_dict.update({j :{
									"surface": splited_list[0].lstrip('\n'),
									"base"   : splited_list[1].lstrip('\n'),
									"pos"    : splited_list[2].lstrip('\n'),
									"pos1"   : splited_list[3].lstrip('\n')
									}})

			sentence_dict.update({i:pos_dict})
	print sentence_dict

	main_df = pd.DataFrame.from_dict(sentence_dict).T
	print main_df#.info()
	print "一応これで整理"
	print "EOS (End of Sentence)で区切り、行でindexを作る"

	return main_df


def task_31(main_df):

	"""
	31. 動詞
	動詞の表層形をすべて抽出せよ．

	main_dfの"surface"から抽出します。
	"""
	print "元のデータはこれ"
	print main_df[main_df["pos1"].str.contains("動詞")]["surface"],"\n"

	# print "重複を削除すると以下"
	# print set(main_df["surface"])
	# for i in set(main_df["surface"]):
	# 	print i

	return


def task_32(main_df):

	"""
	32. 動詞の原形
	動詞の原形をすべて抽出せよ．
	"""
	print main_df[main_df["pos1"].str.contains("動詞")]["base"],"\n"

	return


def task_33(main_df):

	"""
	33. サ変名詞
	サ変接続の名詞をすべて抽出せよ．
	"""
	print main_df[main_df["pos1"].str.contains("サ変接続")]["surface"],"\n"

	return


def task_34(main_df):

	"""
	34. 「AのB」
	2つの名詞が「の」で連結されている名詞句を抽出せよ．
	"""

	print main_df.query("pos1 == 動詞")

	return


def task_35(main_df):


	return




if __name__ == '__main__':
	# import_Mecab_file()
	main_df = task_30()
	task_31(main_df)
	task_32(main_df)
	task_33(main_df)
	task_34(main_df)
	task_35(main_df)
	task_36(main_df)
	task_37(main_df)
	task_38(main_df)
	task_39(main_df)


	# encoded_result =tagger.parseToNode(neko_data)
	# result = encoded_result.decode('utf-8')
	# print result
	# print word_tokenize(neko_data)


	# tmp = [splited_neko[0]]
	# _tmp=  splited_neko[1].split(",")
	# tmp.extend(_tmp)
	# print len(tmp)
	# これで確認
	# for i in tmp:
	# 	print i
	# tmpリストの中に、


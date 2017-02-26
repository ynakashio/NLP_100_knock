# NLP_100_knock


## インストールするもの -- Anaconda環境にて

下記の要領でMeCabとmecab-pythonをインストール。
<br>実際の形態素解析で用いるのは、"-Ochasen"

### MecabとMecab-ipadic-neologd
http://taku910.github.io/mecab/
<br>ここを参考にすると、そのままコマンドをコピペするだけでできます。
<br>ダウンロードして、./configureをして、make/make installです。
<br>mecabrcにMecab-ipadic-neologdのPATHを追加

mecabインストール時に、utf-8でインストール。
```bash
./configure --with-charset=UTF8
```


### mecab-python
Anacondaの下に入っているpipでインストールする必要があります。
<br>ホーム画面の下にある
<br>
```bash
.pyenv/versions/anaconda2-2.5.0/bin/pip install mecab-python
```
でokです。


### 第5章にてCaboCha
https://shogo82148.github.io/blog/2012/11/01/cabocha/
<br>など参考に。
<br>上と同じ要領で、
```bash
./configure --with-charset=UTF8
make
make install
```
でok.<br>
ただし、インストール時に、utf-8の設定を忘れずに。。。泣
<br> 間違えた場合はフォルダごと削除して再度tarしてコマンドを流すとok


## 文字コードについて
http://qiita.com/puriketu99/items/55e04332881d7b679b00
<br>ここを参考にする。<br>
Anacondaの下のpython2.7/site-packages/の下に、sitecustomize.pyとファイルを作って
<br>

```python
import sys
sys.setdefaultencoding("utf-8")
```

<br>を記述する。

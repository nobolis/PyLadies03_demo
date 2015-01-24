
# coding: utf-8

## PyLadies Tokyo #3 demo

### はじめに

# * このファイルはPyLadies Tokyo meet up \#3 (2015/01/23)のために作成したデモファイルです。 
# * コードレビュー歓迎です！

### 利用メモ

# 1. ipython notebookの起動  
# 
#   ipython notebook --matplotlib inline  
#   
#   とすると、図がインライン表示される  
#  
# 2．基本ショートカット
# * Shift-enter  セル実行（セル内の最後の行の結果が出力される）
# * Ctr-Enter    その場でセル実行（実行後次のセルに移動しない）
# * Alt-Enter    セル実行＋下にセルを作成
# * Ctr-m        Ctr-mの後に文字を打つことでショートカットを実行  
#   x cut  
#   c copy  
#   v paste 
#   d delete  
#   z undo last cell deletion  
#   \- split cell
#   a insert cell above  
#   b insert cell below  
#   o toggle output  
#   O toggle output scroll   
#   l toggle line numbers   
#   s save notebook  
#   j move cell down  
#   k move cell up  
#   y code cell  
#   m markdown cell  
#   t raw cell  
#   1-6 heading 1-6 cell  
#   p select previous  
#   n select next  
#   i interrupt kernel  
#   . restart kernel  
#   h show keyboard shortcuts  
#   
# 
# 【参考】  
#   * iPython Notebookの--pylab Inlineは使うのをやめようという話  
#   http://yagays.github.io/blog/2014/08/15/ipython-notebook-matplotlib-inline/   
#   * Keyboard shortcuts  
#   http://ipython.org/ipython-doc/rel-1.1.0/interactive/notebook.html#keyboard-shortcuts  

### Library

# In[1]:

import numpy as np #特に意味はないがお約束の書き方。numpyをnpと省略して書ける
import pandas as pd #特に意味はないがお約束の書き方。pandasをpdと省略して書ける
import scipy as spy
import matplotlib.pyplot as plt #描画，python xyをつかうなら不要
import itertools
import random #「通常の乱数発生」で利用

from scipy import stats
from pandas import DataFrame
from itertools import combinations
from itertools import permutations


### Numpy

# In[2]:

#2.x系環境で書いたコード（2系ではすぐに評価されるが、3系環境で実行するとすぐに評価されない）
dat1 = range(3) #= [0, 1, 2]
dat2 = range(3,6)#= [3, 4, 5]
dat3 = range(6,9)#= [6, 7, 8]
dat4 = range(9,12)#= [9, 10, 11]

#3.x系環境で書いたコード（listを加えることによって、3系環境でも2系環境で得たのと同様の結果となるが、計算上は無意味）
#dat1 = list(range(3))
#dat2 = list(range(3,6))
#dat3 = list(range(6,9))
#dat4 = list(range(9,12))

dat12 = [dat1, dat2]
dat34 = [dat3, dat4]

dat34


# In[3]:

dat12 + dat34 #通常のPythonの足し算の場合


# ##追記φ(.. ) 
# 「2系で書いたのが3系で正しく動かない」と思っていたところ、Slack #onairで「range() はいける気がする」とコメントが入ったので調べてみたところ、以下の記事をみつけました：  
# 
# 言語としての一貫性を重視したPython 3の進化 (1/2)  
# http://qiita.com/Qiita/items/c686397e4a0f4f11683d
# >Python 3.0では、これまでリストを返していたメソッドや組み込み関数がイテレータやview（ビュー）と呼ばれる軽量のイテレータ風オブジェクトを返すようになりました。
# 
# 　イテレーターってなに？って感じなんですが、とりあえず大きく変わっているってことと理解。

# In[4]:

npa12 = np.array(dat12) #上で評価されなかったdat12がここで評価される
npa34 = np.array(dat34)
npa12 


# In[5]:

npa12 + npa34 #np.arrayの足し算の場合、行列の足し算になる


# In[6]:

np.zeros(5) #ゼロだけの配列


# In[7]:

np.zeros((2,3)) #ゼロだけの配列（2x3)


# In[8]:

np.arange(5) #等差数列


### 乱数発生

# In[9]:

#通常の乱数発生の場合
mean = 1.0
sd = 0.1

i=0
rdat2 = []
while i < 1000:
    rdat = random.gauss(mean, sd)
    rdat2.append(rdat)    
    #print(rdat)
    i += 1
    
np.mean(rdat2)
#rdat2


# In[10]:

plt.hist(rdat2, bins=50)


# In[11]:

#numpyによる乱数発生
mean = 1.0
sd = 0.1

rdat3 = np.random.normal(mean, sd, 1000)
        
np.mean(rdat3)


# In[12]:

plt.hist(rdat3, bins=50)


# In[13]:

#線形回帰 slope, intercept, r-value, p-value, stderr（結果はタプルで表示される）
x1 = [1, 2, 3, 4, 5]
y1 = [1.2, 3.4, 5.7, 8.2, 9.4]
regr = stats.linregress(x1, y1) 
regr


# In[14]:

plt.scatter(x1, y1)
#ax.plot(x2, y2)


### pandasのデータフレーム

# In[15]:

dat5 = range(1, 6)
dat6 = range(6,11)


# In[20]:

list(dat5)


# In[17]:

dat6


# In[21]:

#データをデータフレームに格納
df1=DataFrame(list(dat5)) #df1=DataFrame(dat5)だと,3系ではエラーになる
df2=DataFrame(list(dat6))
df1


# In[22]:

df3 = df1 + df2 #データフレームの足し算
df3


# In[23]:

df3.describe() #記述統計量


### pandasによるCSVファイルのインポート

# In[24]:

#csvファイルが入っているフォルダのパス
csvpath ='K:/Dropbox/002_PRIVATE/PROJECT/150123_PyLadiesTokyo_Meet-up003/'

#CSVファイルパス
data_path = csvpath + "demo_data2.csv" 
pg_level_path = csvpath + "demo_pg_level.csv"
py_level_path = csvpath + "demo_py_level.csv"

#データの読み込み(データのデータフレームへの格納)
data = pd.read_csv(data_path, header=0) #indexなしデータ
pg_level = pd.read_csv(pg_level_path, header=0)
py_level = pd.read_csv(py_level_path, header=0)
#1行目はheaderとして自動的に取得される（そのためheader=0でOK）
#index行のヘッダは不要（あるとデータとしてカウントされてしまう）


# In[25]:

data.dtypes


# In[26]:

data #データ


# In[27]:

pg_level #プログラミングレベル


# In[28]:

py_level #Pythonレベル


# In[29]:

data.head(3) #最初から3つめまでのデータ


# In[30]:

data.tail(2) #後ろから2つのデータ


# In[31]:

data[2:4] #2-3番目のデータ


# In[32]:

data[10:] #10番目以降のデータ


# In[33]:

data['pg_level'] #'pg_level'のデータを表示


# In[34]:

data['py_level'].head(3) #'pg_level'のデータを3つ表示


# In[35]:

py_level_c = data['py_level'].value_counts() #'pg_level'のデータ数をカウント
py_level_c


# In[36]:

py_level


# In[37]:

py_level_c.plot(kind='barh') #縦型にプロット
#横型にする場合はkind='barh'


# In[38]:

pg_level_c = data['pg_level'].value_counts() #'pg_level'のデータ数をカウント
pg_level_c


# In[39]:

pg_level


# In[40]:

pg_level_c.plot(kind='bar') #縦型にプロット


# In[41]:

merge1 = pd.merge(data, pg_level, on='pg_level')
merge2 = pd.merge(merge1, py_level, on='py_level')
merge2.head(3)


## itertools

# チュートリアル「PyData入門」の受講メモより:  
# * itertoolsはfor文だと面倒なところを省略してくれる  
# * forでやろうとする前にiteratoolsのツールを探せ！
# 

# In[42]:

#combinations 組み合わせリスト作成

d1 = ['spam', 'ham', 'egg']

for x in itertools.combinations(d1,2):
    print(x)


# In[43]:

#permutations 順列のリスト生成

d2 = ['Py', 'Ladies', 'Tokyo']

for y in itertools.permutations(d2):
    print(y)


# statistics module  
# mean  
# median  
# pstdev  
# Python3.4から標準搭載
# 

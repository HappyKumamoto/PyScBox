#今の時刻
import datetime
py.write(datetime.tatetime.now())

#Pythonのバージョン
import sys
py.write(f'バージョン: {sys.version_info}')


#降雨量
import pandas as pd
import matplotlib.pyplot as plt

the_url = 'https://www.data.jma.go.jp/stats/data/mdrr/pre_rct/alltable/predaily00_rct.csv'

df = pd.read_csv(
    the_url,
    encoding = 'sjis')

header_day = str(df['現在時刻(日)'][0]) + "日の値(mm)"
plt.scatter(df['観測所番号'], df[header_day])


#最高風速
import pandas as pd
import matplotlib.pyplot as plt

the_url = 'https://www.data.jma.go.jp/stats/data/mdrr/wind_rct/alltable/mxwsp00_rct.csv'

df = pd.read_csv(
    the_url,
    encoding = 'sjis')

header_day = str(df['現在時刻(日)'][0]) + "日の最大値(m/s)"
plt.scatter(df['観測所番号'], df[header_day] , c="green")


#sinのグラフ
import matplotlib.pyplot as plt
import numpy as np

cm = plt.get_cmap("Spectral")

x = np.linspace(0, 2*np.pi)
for i in range(11):
    y=np.sin(x+np.pi*i/50)
    plt.plot(x,y,color = cm(i/10))



#講義5.2.1 関数のグラフ sinをcosに変えたもの

import numpy as np # NumPy というライブラリを利用する
import matplotlib.pyplot as plt

cm = plt.get_cmap("Spectral")  #11色

x = np.linspace(0, 0.01 + 2 * np.pi, 629) # x は 0 から 2π まで 628分割
n = 11 # 描く本数

y = [0 * x] * (n + 1) # y をリストで最初に定数関数 y=0 で定義しておく。x の関数であることを明示する。

for k in range(n): # 関数 y[k] が定義されていたとして、y[k + 1] を定義する
    if k % 2 == 0:
        y[k + 1] = y[k] + np.cos((k + 1) * x) / (k + 1)
    else:
        y[k + 1] = y[k] - np.cos((k + 1) * x) / (k + 1)

plt.figure(figsize=(4 * np.pi,8)) # 描画の大きさ
plt.xlim(0, 2 * np.pi) # x座標の範囲
plt.ylim(-3.5, 1.5) # y座標の範囲
plt.xlabel("x") # x方向の軸名
plt.ylabel("y") # y方向の軸名
plt.grid(which="major", color="black", alpha=0.5) # 補助線

for k in range(n): # 定義された関数 y[0], y[1], ... y[n - 1] を描画する
    plt.plot(x, y[k])

plt.show()

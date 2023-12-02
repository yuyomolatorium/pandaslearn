import pandas as pd
df = pd.read_csv('california_housing_train.csv')
print(type(df))
print(df['longitude'].head(3)) #列longitudeについて上から3行目まで確認

print(df.shape) #データサイズの確認

print(df.describe()) #データ代表値を表示

print(df.corr()) #データの相関係数を表示

print(df.sort_values(by='total_rooms')) #列total_roomsについて昇順並び替え,降順のときoptionにascending=Falseを追加

t = df.iloc[:,-1] #データのうちすべての行、最後の列を選択
print(t)

mask = df['median_house_value'] > 70000 #条件を満たすかどうかのbool列が生成
print(df[mask].head()) #条件を満たすデータだけの列が生成


df_dropna = df.dropna() # 欠損値のあるレコードを削除


df_fillna =  df.fillna(mean) # 欠損値を mean で補完
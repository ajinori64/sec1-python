import csv
# 各要素のリスト
name, tell, mail, passwd = [], [], [], [] # パスワード
"""
csvファイルを読み込む際、エンコーディングを行う
BOM(unicodeによる不可視文字)を避けるため、「utf-8-sig」でエンコーディング
"""
# csvファイルを読み込んで各リストに追加
# with文は処理終了時にcloseメソッドを自動的に実行してくれる
with open('information.csv', encoding='utf-8-sig') as info:
    # 区切り文字を指定する(今回「,」)
    reader = csv.reader(info, delimiter=',')
    # リストに追加
    for row in reader:
        name.append(row[0])
        tell.append(row[1])
        mail.append(row[2])
        passwd.append(row[3])

# 確認用
print(f"name   = {name}")
print(f"tell   = {tell}")
print(f"mail   = {mail}")
print(f"passwd = {passwd}\n")

"""
氏名、電話、メールについてマスキングを行う
匿名加工情報制度を基におこなう
URL: https://www.ppc.go.jp/personalinfo/tokumeikakouInfo/
"""
# マスキング用リスト
m_name, m_tell, m_mail, m_passwd = [], [], [], []

# 氏名：すべてマスキング
for i in range(len(name)):
    m_name.append(len(name[i]) * '*')

print(f"n_name = {m_name}")

# 電話番号：下4桁以外マスキング



# メール：5文字目以降マスキング



# パスワードのハッシュ化(今回「sha256」)


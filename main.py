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
# 各要素のマスキング用リスト
m_name, m_tell, m_mail, m_passwd = [], [], [], []

# 氏名：すべてマスキング
for i in range(len(name)):
    m_name.append(len(name[i]) * '*')

# 電話番号：下4桁以外マスキング
for row in tell:
    # 前方桁
    cnt_before = 0
    for item in row:
        # 数字部分を数える
        if item == '-':
            break
        cnt_before += 1
    # 中央桁
    cnt_middle = 0
    # 前方桁以降から数える(+1はハイフン1個)
    for item in row[cnt_before+1:]:
        # 数字部分を数える
        if item == '-':
            break
        cnt_middle += 1
    # 後方桁
    cnt_after = cnt_before + cnt_middle
    # 中央桁以降から数える(+1はハイフン1個)
    for item in row[cnt_after+1:]:
        if item == '-':
            break
        cnt_after += 1
    # ハイフン2個分、cnt_afterに追加して後方桁を出力している
    m_tell.append(cnt_before * '*' + '-' + cnt_middle * '*' + '-' + row[cnt_after+2:])




print(f"m_name = {m_name}")
print(f"m_tell = {m_tell}")
# メール：5文字目以降マスキング



# パスワードのハッシュ化(今回「sha256」)


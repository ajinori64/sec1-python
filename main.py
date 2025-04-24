import sec1_func.output
import sec1_func.csv_reader
import sec1_func.masking
import sec1_func.hashing
import sec1_func.output
# 各オブジェクト変数を生成
out = sec1_func.output
reader = sec1_func.csv_reader
mask = sec1_func.masking
h_sha = sec1_func.hashing
# 各要素のリスト
name, tell, mail, passwd = [], [], [], []   # 元データ
m_name, m_tell, m_mail = [], [], []         # マスキング
h_passwd = []                               # ハッシュ化
# csvファイルを読み込んで各リストに追加
name, tell, mail, passwd = reader.read('information.csv', name, tell, mail, passwd)
"""
氏名、電話、メールについてマスキングを行う
匿名加工情報制度を基におこなう
URL: https://www.ppc.go.jp/personalinfo/tokumeikakouInfo/
"""
# 氏名：すべてマスキング
mask.name_mask(name, m_name)
# 電話番号：下4桁以外マスキング
mask.tell_mask(tell, m_tell)
# メール：5文字目以降マスキング
mask.mail_mask(mail, m_mail)
# 出力
print("\nmasked!\n")
out.output_array('name', m_name)
out.output_array('tell', m_tell)
out.output_array('mail', m_mail)
# パスワードのハッシュ化(今回「sha256」およびソルトを用いる)
salt = 'hello'
h_sha.hashing(passwd, h_passwd, salt)
print("hashed!\n")
out.output_array('passwd', h_passwd)
import hashlib
# array + salt の文字列を sha256 でハッシュ化する
def hashing(array, h_array, salt):
    for row in array:
        # 「パスワード+ソルト」をバイト文字に変換し、16進数に変換
        row += salt
        h_array.append(hashlib.sha256(row.encode()).hexdigest())
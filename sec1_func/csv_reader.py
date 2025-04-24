import csv
"""
csvファイルを読み込む際、エンコーディングを行う
BOM(unicodeによる不可視文字)を避けるため、「utf-8-sig」でエンコーディング
"""
def read(filepath, array1, array2, array3, array4):
    with open(filepath, encoding='utf-8-sig') as info:
    # 区切り文字を指定する(今回「,」)
        reader = csv.reader(info, delimiter=',')
    # リストに追加
        for row in reader:
            array1.append(row[0])
            array2.append(row[1])
            array3.append(row[2])
            array4.append(row[3])
    # 読み込んだデータを返却
    return [array1, array2, array3, array4]
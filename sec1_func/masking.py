# name_mask関数：氏名をマスキングする
def name_mask(array, m_array):
    # 氏名：すべてマスキング
    for i in range(len(array)):
        m_array.append(len(array[i]) * '*')

# tell_mask：電話番号下4桁以外マスキング
def tell_mask(array, m_array):
    for row in array:
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
        m_array.append(cnt_before * '*' + '-' + cnt_middle * '*' + '-' + row[cnt_after+2:])

def mail_mask(array, m_array):
    for row in array:
        m_array.append(row[:4] + len(row[4:].partition('@')[0]) * '*' + '@' + len(row.partition('@')[2]) * '*')
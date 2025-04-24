import time
# リストを出力
def output_array(name, array):
    for i, row in enumerate(array):
        time.sleep(0.25)
        print(f"{name}[{i}]:{row}")
    print()
    time.sleep(0.5)
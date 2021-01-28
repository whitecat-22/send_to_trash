import glob
import send2trash

file_path = "C:\\Users\\xxxxxxxx\\yyyyyyyy\\"    # 末尾の'\\'は必須

for f in glob.glob1(file_path, "*.csv"):    # 対象とするファイルの拡張子やファイル名を指定
    f = file_path + f

    print(f)  # ファイルパス\ファイル名を表示

    send2trash.send2trash(f)    # ゴミ箱へ移す

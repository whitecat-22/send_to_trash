import glob
import send2trash

file_path = "C:/Users/xxxxxxxx/yyyyyyyy/"    # 末尾の'/'は必須

for f in glob.glob1(file_path, "*.csv"):    # 対象とするファイルの拡張子やファイル名を指定
    f = csv_path + f

    print(f.name)  # ファイルパス\ファイル名を表示

    send2trash.send2trash(f.name)    # ゴミ箱へ移す

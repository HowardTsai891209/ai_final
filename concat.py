import pandas as pd
import os

# 設定檔案路徑
folder_path = "data/110"  # 你放csv檔的資料夾路徑
all_data = []

# 自動讀入 11201~11212.csv
for month in range(1, 13):
    filename = f"110{month:02d}.csv"
    filepath = os.path.join(folder_path, filename)
    df = pd.read_csv(filepath, encoding='big5')

    # 假設資料中有 '日期' 欄，轉成 datetime
    df['日期'] = pd.to_datetime(df['日期'])

    all_data.append(df)

# 合併所有月份資料
full_df = pd.concat(all_data, ignore_index=True)

# 排序一下日期
full_df = full_df.sort_values('日期')
full_df.to_csv("combined_110.csv", index=False, encoding="utf-8-sig")
print("done")

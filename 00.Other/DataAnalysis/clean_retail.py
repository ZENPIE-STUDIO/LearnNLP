
import pandas as pd
import os, datetime


work_folder = os.getcwd()
print(f'WorkPath = {work_folder}')
# mkdir
date_foldername = datetime.datetime.now().strftime("%Y%m%d")
print(f'mkdir {date_foldername}')
os.mkdir(date_foldername)

output_path = work_folder + '/' + date_foldername
afterclean_path = output_path + '/' + 'afterclean.csv'
refund_csv_path = output_path + '/' + 'afterclean-refund.csv'
without_refund_csv_path = output_path + '/' + 'afterclean-without-refund.csv'


# Load 原先完整的資料
print('Read Excel File')
df = pd.read_excel("online-retail.xlsx")

# Show All Columns
df.info()

# 資料清理 (去除 空值 及 不合理數)
# - CustomerID 的空值
# - StockCode : 排除字串長度小於5，例如：M,D,POST...

# -------[去除 CustomerID 的空值]---------
print('Clean Empty CustomerID...')
df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')
df = df.dropna(subset=['CustomerID'], axis=0)
df['CustomerID'] = df['CustomerID'].astype(int)


# StockCode 只留下5,6長度，以下資料排除
#           M or D, 因為它有多種價格
#           POST 是運費 (也是多種價格)
#           CRUK 不知道是啥
#           'BANK CHARGES'
stockcode_mask1 = df['StockCode'].str.len() >= 5
stockcode_mask2 = df['StockCode'].str.len() <= 6
df = df.loc[stockcode_mask1]
df = df.loc[stockcode_mask2]
# 新增Column <TotalPrice> 銷售金額 = Quantity * UnitPrice
df['TotalPrice'] = df['UnitPrice'].mul(df['Quantity'])


# 合在一起
print(f'Save to csv > {afterclean_path}')
df.to_csv(afterclean_path)
# 方便資料顯示，可區分 銷售/退貨 兩種資料表
# 銷售
print(f'Save to csv > {without_refund_csv_path}')
df.loc[df['Quantity'] > 0].to_csv(without_refund_csv_path)
# 退款
print(f'Save to csv > {refund_csv_path}')
df.loc[df['Quantity'] < 0].to_csv(refund_csv_path)


# (說明) 取樣30% 大小的資料，用來加速開發
# small_dataset = df.sample(frac=0.3,random_state=200).reset_index(drop=True)
# print("Small Dataset: {}".format(small_dataset.shape))
# small_dataset.to_csv('small-online-retail.csv')
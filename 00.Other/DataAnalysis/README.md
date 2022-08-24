# README

- 資料來源：https://scidm.nchc.org.tw/dataset/ee1bc2a7-a4fd-4ccf-a212-c94136b0e15e/resource/f53fdcce-859e-4ae9-9c58-29719448a2d9/nchcproxy/online-retail.xlsx

- 目的：
  - Pandas 練習
  - 練習資料清理及分析資料



### 報表呈現內容

- 區分國家 列出 銷售總金額(不含運費) 的 中位數、最小值、最大值
- 顯示每個月的銷售金額
- StockCode 商品銷售數量 Top 10
- StockCode 商品銷售金額 Top 10



### 資料清理及處理

- 瀏覽資料內容後，決定：
  - 排除 **CustomerID** 的空值，因為無法用於之後的報表。
  - **Quantity** 大於0 為銷售資料、小於0為退貨資料。
  - 排除 **StockCode** 只留下5, 6長度，以下資料排除
    - M or D, 因為它有多種價格
    - POST 是運費 (也是多種價格)
    - CRUK 不知道是啥
    - BANK CHARGES

- 輸出資料
  - 新增Column  **TotalPrice** (銷售金額) = Quantity * UnitPrice
  - 把資料分成 銷售/退貨 兩個資料檔


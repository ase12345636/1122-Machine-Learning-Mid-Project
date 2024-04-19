# 1122-Machine-Learning-Mid-Project



## 基本資料

### 主題：車牌位置標記

### 成員
- 110321015 陳奕羱
- 110321018 張簡雲翔
- 110321069 王駿彥

### 授課老師：周信宏老師

### 課程：1122機器學習

## 選用模型

### Pretrain Model
- YOLO v8
- YOLO v9
- YOLO v5

## Dataset
### [taiwan-license-plate-recognition-research-tlprr Image Dataset](https://universe.roboflow.com/jackresearch0/taiwan-license-plate-recognition-research-tlprr/dataset/7)
- train：2873
- validation：338
- test：169
#### Data label：每個label共有五個數字，與YOLO標記方式相同，第一個是class ID，後面跟著物件中心的位置（x, y），在跟著兩個數字，寬度以及高度，皆為小數（ID除外），後面的都是在整張圖片的設為1 * 1後計算出來的座標。因為只要標示出車牌，所以只有一個class，設為0。

## Reference
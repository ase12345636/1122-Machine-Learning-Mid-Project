# 1122-Machine-Learning-Mid-Project

### 主題：車牌位置標記

### 成員
- 110321015 陳奕羱
- 110321018 張簡雲翔
- 110321069 王駿彥

### 授課老師：周信宏老師

### 課程：1122機器學習

## 動機&目的
車牌辨識，是一項現在十分常用到的技術，也是一個到處都會看到的東西，雖然但是，我不知道為何我們學校機車道砸道入口遲遲不做？這項技術如此常見，而且資料集也很好收集跟取得，所以我們決定選這項主題。我們推測要完成車牌辨識，應該要分成兩個步驟，第一步：找到車牌的位置，第二步：辨識車牌上的文字，第二步，基本上就跟MNIST有點異曲同工之妙，不外乎，就是用CNN模型去做，基本上作業一大概也都試過了，但是第一步就很有趣了，至少我們都沒有特別玩過物件偵測的主題，所以我們決定，來試試看做找到一張圖片裡面，車牌的位置。當然，如果模型效果很好的話，我們也可以再去建議學校機車道應該要裝車牌辨識系統了，畢竟連一門課的其中專題都能做出一點東西來了，在不裝也說不過去了吧！

## Model
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

## Data PreProcess
基本上照片裡面都會有一個到數個車牌，但是主要都是在地下室或者光線明亮的地方拍攝的，因為Label標示方式，與YOLO的形式一樣，不需要做特別處裡。圖片大小並不相等，在模型的hyperparameter上，有一個image size的參數，可以設定一個長寬最大的大小，之後模型會自己幫我們做resize（長寬比不變）。因為是用pretrain的模型，所以基本上資料量不用太大效果也應該是不錯。

## 分工
- 陳奕羱：YOLOv5、簡報製作、資料收集
- 張簡雲翔：YOLOv8、資料彙整、資料收集
- 王駿彥：Dataset搜尋、YOLOv9、資料收集

## 困難與解決
- Q1：剛開始訓練YOLOv8的時候，發現效果都很差
- A1：Batch size不夠大
- Q2：Batch size太大，導致VRAM不夠多
- A2：使用Colab
- Q3：做到一半學校停電，Colab斷線
- A3：上Dcard噴學校，之後改用手機行動網路


## Reference

### YOLO
- https://hackmd.io/@luckychi/yolov8_simple_tutorial
- https://docs.ultralytics.com/modes/train/#apple-m1-and-m2-mps-training
- https://blog.csdn.net/weixin_40293999/article/details/131856110
- https://github.com/AILab-CVC/YOLO-World/issues/7
- https://blog.csdn.net/qq_41821678/article/details/106113870
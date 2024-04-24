from ultralytics import YOLO
model = YOLO(
    "D:\\Project\\MachineLearning\\1122-Machine-Learning-Mid-Project\\yolov5nu\\runs\\datect\\train5\\weights\\best.pt")
if __name__ == '__main__':
    result = model.predict(
        source="D:\\Project\\MachineLearning\\1122-Machine-Learning-Mid-Project\\self photo",
        mode="predict",
        save=True,
        device="0")

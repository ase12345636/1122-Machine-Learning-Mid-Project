from ultralytics import YOLO
model = YOLO('best.pt')
if __name__ == '__main__':
    result = model.predict(
        source="D:\\Project\\MachineLearning\\1122-Machine-Learning-Mid-Project\\self photo",
        mode="predict",
        save=True,
        device="0")

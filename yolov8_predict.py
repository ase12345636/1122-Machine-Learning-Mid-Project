from ultralytics import YOLO
model = YOLO("runs\\detect\\train\\weights\\best.pt")
if __name__ == '__main__':
    result = model.predict(source="datasets/valid/images",
        mode="predict",
        save=True,
        device="0")
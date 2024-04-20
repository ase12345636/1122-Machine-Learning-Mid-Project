from ultralytics import YOLO
model = YOLO("runs\\detect\\train\\weights\\best.pt")
if __name__ == '__main__':
    result = model.predict(
        #source="datasets/valid/images",
        source = "self photo",
        mode="predict",
        save=True,
        device="0")
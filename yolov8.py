from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                epochs=10,
                imgsz=640,
                device="0")
    
    model = YOLO("runs\\detect\\train\\weights\\best.pt")
    result = model.predict(source="dataset/valid/images",
        mode="predict",
        save=True,
        device="0")
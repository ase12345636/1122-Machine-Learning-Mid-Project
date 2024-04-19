from ultralytics import YOLO
model = YOLO("yolov8n.pt")
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                batch=-1,
                epochs=20,
                imgsz=640,
                device="0")
    val_his = model.val()

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
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                batch=256,
                epochs=20,
                imgsz=640,
                device="0")
    val_his = model.val()

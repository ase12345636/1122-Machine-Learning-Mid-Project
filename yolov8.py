from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                epochs=100,
                imgsz=640,
                device="0")

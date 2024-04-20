from ultralytics import YOLO
model = YOLO('yolov5n.pt')

results = model('path/to/bus.jpg')
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                epochs=50,
                batch = -1,
                imgsz=640,
                device="0")
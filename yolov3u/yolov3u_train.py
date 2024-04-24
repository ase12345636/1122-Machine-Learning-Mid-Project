from ultralytics import YOLO
model = YOLO('yolov3u.pt')

if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                epochs=50,
                batch=-1,
                imgsz=640)
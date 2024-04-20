from ultralytics import YOLO
model = YOLO('best.pt')
if __name__ == '__main__':
    model.train(data="data.yaml",
                mode="detect",
                epochs=50,
                batch = 13,
                imgsz=640,
                device="0")
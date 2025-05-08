import cv2
import os

video_dir = 'data/avenue/frames'
output_dir = 'data/avenue/frames'

for filename in os.listdir(video_dir):
    if filename.endswith('.avi'):
        video_path = os.path.join(video_dir, filename)
        video_name = filename.split('.')[0]
        out_folder = os.path.join(output_dir, video_name)
        os.makedirs(out_folder, exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out_path = os.path.join(out_folder, f"{frame_idx:06}.jpg")
            cv2.imwrite(out_path, frame)
            frame_idx += 1
        cap.release()
        print(f"Extracted {frame_idx} frames from {filename}")

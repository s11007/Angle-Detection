# -*- coding: utf-8 -*-

import os
from datetime import datetime
from video import video

# 主函數

def main(csv_dir, video_dir, output_dir):

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join(output_dir, timestamp)

    for csv_file in os.listdir(csv_dir):
        if csv_file.endswith(').csv'):
            csv_path = os.path.join(csv_dir, csv_file)
            video_file = csv_file.replace('.csv', '.mp4')
            video_path = os.path.join(video_dir, video_file)
            if os.path.exists(video_path):
                video(csv_path, video_path, output_dir)
            else:
                print(f"找不到檔案: {video_file}")

# 執行

if __name__ == '__main__':
    csv_dir = "C:/Users/JJ/Documents/專題/small/"
    video_dir = "C:/Users/JJ/Documents/專題/small/"
    output_dir = "C:/Users/JJ/Downloads/"
    main(csv_dir, video_dir, output_dir)

# -*- coding: utf-8 -*-

import os
import argparse
from datetime import datetime
from video import video

# 主函数
def main(csv_dir, video_dir, output_dir):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join(output_dir, timestamp)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

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
    parser = argparse.ArgumentParser(description="位置")
    parser.add_argument('--csv_dir', type=str, required=True, help="CSV目錄位置")
    parser.add_argument('--video_dir', type=str, required=True, help="影片目錄位置")
    parser.add_argument('--output_dir', type=str, required=True, help="影片輸出位置")

    args = parser.parse_args()

    main(args.csv_dir, args.video_dir, args.output_dir)

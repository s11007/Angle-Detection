import os
import cv2
import numpy as np
import pandas as pd
from check_pushup import check_pushup
from calculate_angle import calculate_angle
from draw_lines_and_angles import draw_lines_and_angles
    
def video(csv_path, video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    df = pd.read_csv(csv_path)
    
    left_hip_angles = []
    left_knee_angles = []
    right_hip_angles = []
    right_knee_angles = []
    left_elbow_angles = []
    right_elbow_angles = []
    left_wrist_angles = []
    right_wrist_angles = []
    
    # 算角度

    for frame in range(len(df)):
        left_shoulder = [df.loc[frame, 'left_shoulder_x'], df.loc[frame, 'left_shoulder_y']]
        right_shoulder = [df.loc[frame, 'right_shoulder_x'], df.loc[frame, 'right_shoulder_y']]
        left_hip = [df.loc[frame, 'left_hip_x'], df.loc[frame, 'left_hip_y']]
        right_hip = [df.loc[frame, 'right_hip_x'], df.loc[frame, 'right_hip_y']]
        left_knee = [df.loc[frame, 'left_knee_x'], df.loc[frame, 'left_knee_y']]
        right_knee = [df.loc[frame, 'right_knee_x'], df.loc[frame, 'right_knee_y']]
        left_ankle = [df.loc[frame, 'left_ankle_x'], df.loc[frame, 'left_ankle_y']]
        right_ankle = [df.loc[frame, 'right_ankle_x'], df.loc[frame, 'right_ankle_y']]
        left_elbow = [df.loc[frame, 'left_elbow_x'], df.loc[frame, 'left_elbow_y']]
        right_elbow = [df.loc[frame, 'right_elbow_x'], df.loc[frame, 'right_elbow_y']]
        left_wrist = [df.loc[frame, 'left_wrist_x'], df.loc[frame, 'left_wrist_y']]
        right_wrist = [df.loc[frame, 'right_wrist_x'], df.loc[frame, 'right_wrist_y']]

        left_angle_hip = calculate_angle(left_shoulder, left_hip, left_knee)
        right_angle_hip = calculate_angle(right_shoulder, right_hip, right_knee)
        left_angle_knee = calculate_angle(left_hip, left_knee, left_ankle)
        right_angle_knee = calculate_angle(right_hip, right_knee, right_ankle)
        left_angle_elbow = calculate_angle(left_shoulder, left_elbow, left_wrist)
        right_angle_elbow = calculate_angle(right_shoulder, right_elbow, right_wrist)
        left_angle_wrist = calculate_angle(left_elbow, left_wrist, left_ankle)
        right_angle_wrist = calculate_angle(right_elbow, right_wrist, right_ankle)
        left_hip_angles.append(left_angle_hip)
        right_hip_angles.append(right_angle_hip)
        left_knee_angles.append(left_angle_knee)
        right_knee_angles.append(right_angle_knee)
        left_elbow_angles.append(left_angle_elbow)
        right_elbow_angles.append(right_angle_elbow)
        left_wrist_angles.append(left_angle_wrist)
        right_wrist_angles.append(right_angle_wrist)


    
    output_video_path = os.path.join(output_dir,
                                       f'{os.path.basename(video_path).split(".")[0]}_with_errors.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path,
                          fourcc,
                          fps,
                          (int(cap.get(3)), int(cap.get(4))))
    first_frame = True
    
    for frame in range(len(df)):
        ret, img = cap.read()
        if not ret:
            break
        if frame < len(left_knee_angles):
            points = {
                'left_shoulder': [int(df.loc[frame,'left_shoulder_x']), int(df.loc[frame,'left_shoulder_y'])],
                'right_shoulder': [int(df.loc[frame,'right_shoulder_x']), int(df.loc[frame,'right_shoulder_y'])],
                'left_hip': [int(df.loc[frame,'left_hip_x']), int(df.loc[frame,'left_hip_y'])],
                'right_hip': [int(df.loc[frame,'right_hip_x']), int(df.loc[frame,'right_hip_y'])],
                'left_knee': [int(df.loc[frame,'left_knee_x']), int(df.loc[frame,'left_knee_y'])],
                'right_knee': [int(df.loc[frame,'right_knee_x']), int(df.loc[frame,'right_knee_y'])],
                'left_ankle': [int(df.loc[frame,'left_ankle_x']), int(df.loc[frame,'left_ankle_y'])],
                'right_ankle': [int(df.loc[frame,'right_ankle_x']), int(df.loc[frame,'right_ankle_y'])],
                'left_elbow': [int(df.loc[frame,'left_elbow_x']), int(df.loc[frame,'left_elbow_y'])],
                'right_elbow': [int(df.loc[frame,'right_elbow_x']), int(df.loc[frame,'right_elbow_y'])],
                'left_wrist': [int(df.loc[frame,'left_wrist_x']), int(df.loc[frame,'left_wrist_y'])],
                'right_wrist': [int(df.loc[frame,'right_wrist_x']), int(df.loc[frame,'right_wrist_y'])]
            }
            
            angles = {
                'left_hip': left_hip_angles[frame],
                'right_hip': right_hip_angles[frame],
                'left_knee': left_knee_angles[frame],
                'right_knee': right_knee_angles[frame],
                'left_elbow': left_elbow_angles[frame],
                'right_elbow': right_elbow_angles[frame],
                'left_wrist': left_wrist_angles[frame],
                'right_wrist': right_wrist_angles[frame]
            }

            position_data = {
                'left_shoulder': points['left_shoulder'],
                'right_shoulder': points['right_shoulder'],
                'left_elbow': points['left_elbow'],
                'right_elbow': points['right_elbow'],
                'left_wrist': points['left_wrist'],
                'right_wrist': points['right_wrist'],
                'left_hip': points['left_hip'],
                'right_hip': points['right_hip'],
                'left_ankle': points['left_ankle'],
                'right_ankle': points['right_ankle']
            }
            
            errors = check_pushup(position_data)
            
            if errors:
                for i, message in enumerate(errors):
                    cv2.putText(img, message, (50, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            shoulder_distance = np.linalg.norm(np.array(points['left_shoulder']) - np.array(points['right_shoulder']))
            if first_frame:
              if shoulder_distance < 50 and np.array(points['left_shoulder'][0]) - np.array(points['left_hip'][0]) > 0:
                  show_side = 'right'
              elif shoulder_distance < 50 and np.array(points['left_shoulder'][0]) - np.array(points['left_hip'][0]) < 0:
                  show_side = 'left'
              else:
                  show_side = 'both'
              first_frame = False
              
            draw_lines_and_angles(img, points, angles, show_side)
        
        out.write(img)  

    cap.release()
    out.release()  

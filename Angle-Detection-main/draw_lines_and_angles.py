# -*- coding: utf-8 -*-

import cv2

# 繪製連線、角度

def draw_lines_and_angles(img, points, angles, show_side):
    
    def valid(point):
        return point is not None and point[0] != 0 and point[1] != 0

    if show_side == 'left' or show_side == 'both':
        if valid(points['left_shoulder']) and valid(points['left_hip']):
            cv2.line(img, tuple(points['left_shoulder']), tuple(points['left_hip']), (255, 180, 90), 4)
        if valid(points['left_hip']) and valid(points['left_knee']):
            cv2.line(img, tuple(points['left_hip']), tuple(points['left_knee']), (255, 180, 90), 4)
        if valid(points['left_knee']) and valid(points['left_ankle']):
            cv2.line(img, tuple(points['left_knee']), tuple(points['left_ankle']), (255, 180, 90), 4)
        if valid(points['left_shoulder']) and valid(points['left_elbow']):
            cv2.line(img, tuple(points['left_shoulder']), tuple(points['left_elbow']), (255, 180, 90), 4)
        if valid(points['left_elbow']) and valid(points['left_wrist']):
            cv2.line(img, tuple(points['left_elbow']), tuple(points['left_wrist']), (255, 180, 90), 4)

        if valid(points['left_shoulder']) and valid(points['left_hip']) and valid(points['left_knee']):
            cv2.putText(img, f'{angles["left_hip"]:.2f}', tuple(points['left_hip']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        if valid(points['left_hip']) and valid(points['left_knee']) and valid(points['left_ankle']):
            cv2.putText(img, f'{angles["left_knee"]:.2f}', tuple(points['left_knee']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        if valid(points['left_shoulder']) and valid(points['left_elbow']) and valid(points['left_wrist']):
            cv2.putText(img, f'{angles["left_elbow"]:.2f}', tuple(points['left_elbow']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)        
        if valid(points['left_elbow']) and valid(points['left_wrist']) and valid(points['left_ankle']):
            left_wrist_angle = 180 - angles["left_wrist"]
            cv2.putText(img, f'{left_wrist_angle:.2f}', tuple(points['left_wrist']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)

    if show_side == 'right' or show_side == 'both':
        if valid(points['right_shoulder']) and valid(points['right_hip']):
            cv2.line(img, tuple(points['right_shoulder']), tuple(points['right_hip']), (255, 180, 90), 4)
        if valid(points['right_hip']) and valid(points['right_knee']):
            cv2.line(img, tuple(points['right_hip']), tuple(points['right_knee']), (255, 180, 90), 4)
        if valid(points['right_knee']) and valid(points['right_ankle']):
            cv2.line(img, tuple(points['right_knee']), tuple(points['right_ankle']), (255, 180, 90), 4)
        if valid(points['right_shoulder']) and valid(points['right_elbow']):
            cv2.line(img, tuple(points['right_shoulder']), tuple(points['right_elbow']), (255, 180, 90), 4)
        if valid(points['right_elbow']) and valid(points['right_wrist']):
            cv2.line(img, tuple(points['right_elbow']), tuple(points['right_wrist']), (255, 180, 90), 4)

        if valid(points['right_shoulder']) and valid(points['right_hip']) and valid(points['right_knee']):
            cv2.putText(img, f'{angles["right_hip"]:.2f}', tuple(points['right_hip']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        if valid(points['right_hip']) and valid(points['right_knee']) and valid(points['right_ankle']):
            cv2.putText(img, f'{angles["right_knee"]:.2f}', tuple(points['right_knee']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        if valid(points['right_shoulder']) and valid(points['right_elbow']) and valid(points['right_wrist']):
            cv2.putText(img, f'{angles["right_elbow"]:.2f}', tuple(points['right_elbow']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)        
        if valid(points['right_elbow']) and valid(points['right_wrist']) and valid(points['right_ankle']):
            right_wrist_angle = 180 - angles["right_wrist"]
            cv2.putText(img, f'{right_wrist_angle:.2f}', tuple(points['right_wrist']),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)

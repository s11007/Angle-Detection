# 判斷肩膀與手腕的相對位置
def check_shoulder_wrist_position(position_data):
    left_shoulder = position_data['left_shoulder']
    left_wrist = position_data['left_wrist']
    right_shoulder = position_data['right_shoulder']
    right_wrist = position_data['right_wrist']

    errors = []

    shoulder_wrist_distance_left = abs(left_wrist[0] - left_shoulder[0]) < (
            abs(left_shoulder[0] - position_data['left_hip'][0]) * 0.4)
    
    shoulder_wrist_distance_right = abs(right_wrist[0] - right_shoulder[0]) < (
            abs(right_shoulder[0] - position_data['right_hip'][0]) * 0.4)

    if not shoulder_wrist_distance_left:
        errors.append("Incorrect position of left shoulder and left wrist")
    
    if not shoulder_wrist_distance_right:
        errors.append("Incorrect position of right shoulder and right wrist")

    return errors
from check_shoulder_wrist_position import check_shoulder_wrist_position
from check_body_straight import check_body_straight
from check_elbow_angle import check_elbow_angle

# 檢查伏地挺身動作的函數
def check_pushup(position_data):
    errors = []
    
    errors.extend(check_shoulder_wrist_position(position_data))
    errors.extend(check_body_straight(position_data))
    errors.extend(check_elbow_angle(position_data))

    return errors
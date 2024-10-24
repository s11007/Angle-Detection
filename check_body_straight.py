# 判斷身體是否保持直線
def check_body_straight(position_data):
    left_shoulder = position_data['left_shoulder']
    left_hip = position_data['left_hip']
    right_shoulder = position_data['right_shoulder']
    right_hip = position_data['right_hip']

    errors = []

    left_distance = abs(left_shoulder[1] - left_hip[1])
    right_distance = abs(right_shoulder[1] - right_hip[1])

    proportion = 0.1
    threshold_left = left_distance * proportion
    threshold_right = right_distance * proportion

    body_straight = (left_distance < threshold_left) and (right_distance < threshold_right)

    if not body_straight:
        errors.append("The body is not straight")

    return errors
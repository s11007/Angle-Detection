from calculate_angle import calculate_angle

def check_body_straight(position_data):
    left_hip_angle = calculate_angle(position_data['left_shoulder'], position_data['left_hip'], position_data['left_knee'])
    right_hip_angle = calculate_angle(position_data['right_shoulder'], position_data['right_hip'], position_data['right_knee'])
    left_knee_angle = calculate_angle(position_data['left_hip'], position_data['left_knee'], position_data['left_ankle'])
    right_knee_angle = calculate_angle(position_data['right_hip'], position_data['right_knee'], position_data['right_ankle'])

    errors = []

    if left_hip_angle < 150 :
        errors.append("Left hip is too high")

    if left_knee_angle < 150 :
        errors.append("Left knee is too low")

    if right_hip_angle < 150 :
        errors.append("Right hip is too high")

    if right_knee_angle < 150:
        errors.append("Right knee is too low")

    return errors

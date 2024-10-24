from calculate_angle import calculate_angle

# 判斷肘部角度
def check_elbow_angle(position_data):
    left_elbow_angle = calculate_angle(position_data['left_shoulder'], position_data['left_elbow'], position_data['left_wrist'])
    right_elbow_angle = calculate_angle(position_data['right_shoulder'], position_data['right_elbow'], position_data['right_wrist'])

    errors = []

    try:  
        if left_elbow_angle >= 120:
            errors.append("Incorrect left elbow angle")
    except (TypeError, NameError):
        errors.append("Left elbow angle is not available or invalid")

    try:
        if right_elbow_angle >= 120:
            errors.append("Incorrect right elbow angle")
    except (TypeError, NameError):
        errors.append("Right elbow angle is not available or invalid")
        
    return errors

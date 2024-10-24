# -*- coding: utf-8 -*-

import numpy as np

"""
# 算夾角 內積公式
a · b = |a| × |b| × cos(θ) -> cos(θ) = a · b / |a| × |b|
θ = acos(a · b / |a| × |b|)
|a| = ab長度 : norm_ab
|b| = bc長度 : norm_bc
角度 = 弧度 × 180 / π : angle
"""

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ab = a - b
    bc = c - b

    dot_product = np.dot(ab, bc)
    norm_ab = np.linalg.norm(ab)
    norm_bc = np.linalg.norm(bc)
    
    if norm_ab == 0 or norm_bc == 0:
        return None

    cos_angle = dot_product / (norm_ab * norm_bc)
    angle = np.arccos(cos_angle) * 180.0 / np.pi

    return angle
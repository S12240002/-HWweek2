# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:34:48 2024

@author: Student
"""

import math

def main():
    # 輸入半徑
    radius = float(input("請輸入圓的半徑："))

    # 計算圓周長
    circumference = 2 * math.pi * radius

    # 計算圓面積
    area = math.pi * radius ** 2

    # 輸出結果
    print("圓周長：", circumference)
    print("圓面積：", area)

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:24:39 2024

@author: Student
"""

name = input("請輸入您的姓名：")
age = int(input("請輸入您的年齡："))
height = float(input("請輸入您的身高（米）："))
favorite_color = input("請輸入您喜愛的顏色：")

# 處理：收集這些資料，並將它們存儲在適當的資料結構中（考慮使用字典）。
user_data = {
    "name": name,
    "age": age,
    "height": height,
    "favorite_color": favorite_color,
}

print("名字:"f"{user_data['name']}, {user_data['age']}歲, 身高{user_data['height']}米, 喜愛的顏色是{user_data['favorite_color']}.")
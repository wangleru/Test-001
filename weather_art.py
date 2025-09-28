import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_weather_data():
    """生成模拟的天气数据（气温）"""
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
    temperatures = []
    
    # 模拟季节性温度变化
    for i, date in enumerate(dates):
        base_temp = 15 + 10 * np.sin(2 * np.pi * i / 365)  # 季节性变化
        daily_variation = random.uniform(-5, 5)  # 每日波动
        temperature = base_temp + daily_variation
        temperatures.append(temperature)
    
    return dates, temperatures

def create_artistic_visualization(dates, temperatures):
    """创建艺术化的气温可视化"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 传统折线图
    ax1.plot(dates, temperatures, color='skyblue', linewidth=2, alpha=0.7)
    ax1.set_title('年度气温变化', fontsize=14, fontweight='bold')
    ax1.set_xlabel('日期')
    ax1.set_ylabel('温度 (°C)')
    ax1.grid(True, alpha=0.3)
    
    # 艺术化可视化 - 极坐标温度玫瑰图
    angles = np.linspace(0, 2 * np.pi, len(temperatures))
    radii = [(temp - min(temperatures)) * 2 for temp in temperatures]  # 标准化半径
    
    # 创建颜色映射基于温度
    colors = plt.cm.plasma((np.array(temperatures) - min(temperatures)) / 
                          (max(temperatures) - min(temperatures)))
    
    ax2 = plt.subplot(122, projection='polar')
    scatter = ax2.scatter(angles, radii, c=colors, s=30, alpha=0.7, cmap='plasma')
    ax2.set_title('温度玫瑰图 - 艺术化可视化', fontsize=14, fontweight='bold')
    ax2.grid(True)
    ax2.set_theta_zero_location('N')
    ax2.set_theta_direction(-1)
    
    # 添加颜色条
    plt.colorbar(scatter, ax=ax2, label='温度 (°C)')
    
    plt.tight_layout()
    plt.savefig('weather_art.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_simple_art():
    """创建更简单的艺术化点状图"""
    dates, temperatures = generate_weather_data()
    
    plt.figure(figsize=(12, 8))
    
    # 将日期转换为数值用于散点图
    date_nums = [i for i in range(len(dates))]
    
    # 创建散点图，大小和颜色基于温度
    sizes = [(temp - min(temperatures)) * 5 + 10 for temp in temperatures]  # 大小映射
    colors = plt.cm.viridis((np.array(temperatures) - min(temperatures)) / 
                           (max(temperatures) - min(temperatures)))
    
    plt.scatter(date_nums, temperatures, s=sizes, c=colors, alpha=0.6, 
               edgecolors='black', linewidth=0.5)
    
    plt.title('气温数据艺术化表示', fontsize=16, fontweight='bold')
    plt.xlabel('时间 (天)')
    plt.ylabel('温度 (°C)')
    plt.grid(True, alpha=0.3)
    
    # 添加颜色条
    sm = plt.cm.ScalarMappable(cmap='viridis', 
                              norm=plt.Normalize(min(temperatures), max(temperatures)))
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label('温度 (°C)')
    
    plt.savefig('simple_weather_art.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("生成天气数据中...")
    dates, temperatures = generate_weather_data()
    
    print("创建艺术化可视化...")
    create_artistic_visualization(dates, temperatures)
    
    print("创建简单艺术化图表...")
    create_simple_art()
    
    print("完成！检查生成的图片文件。")
# 自然数据艺术化可视化项目

## 项目描述
这个项目将天气数据（气温）转换为艺术化的可视化效果，探索数据可视化和艺术表达之间的界限。

## 数据来源
- 使用模拟生成的年度气温数据
- 数据代表一个完整年份的每日温度变化

## 可视化内容
1. **传统折线图**：显示气温的年度变化趋势
2. **温度玫瑰图**：极坐标下的艺术化温度表示
3. **散点艺术图**：使用大小和颜色编码的温度可视化

## 如何运行
### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行程序
```bash
python weather_art.py
```

## 文件结构
```
项目文件夹/
├── weather_art.py       # 主程序文件
├── requirements.txt     # 依赖包列表
├── README.md           # 说明文档
├── weather_art.png     # 生成的可视化图片1
└── simple_weather_art.png # 生成的可视化图片2
```

## 技术栈
- **Python 3.x**
- **matplotlib**: 数据可视化
- **numpy**: 数值计算
- **pandas**: 数据处理

## 代码示例
```python
# 生成模拟天气数据
def generate_weather_data():
    dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(365)]
    temperatures = []
    # 模拟季节性温度变化...
```

## 生成的可视化效果
运行程序后将生成两张图片：
- `weather_art.png`: 包含传统折线图和极坐标艺术图
- `simple_weather_art.png`: 简化的艺术化散点图

## 作者
[WANG Leru]

## 课程信息
- **课程名称**: [SD5913 Creative Programming for Designers and Artists]
- **提交日期**: [28/09/2025]

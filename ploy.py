import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 設置字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# # 人數資料
# time_slots = ['時間一', '時間二', '時間三']
# counts = [9, 5, 3]  # 根據表格中實際的人數

# # 繪製條形圖
# plt.figure(figsize=(10, 6))
# plt.bar(time_slots, counts, color=['blue', 'orange', 'green'])
# plt.xlabel('時間段')
# plt.ylabel('人數')
# plt.title('不同時間段的參加人數')
# plt.ylim(0, 10)

# # 添加數值標籤
# for i, count in enumerate(counts):
#     plt.text(i, count + 0.2, f'{count}人', ha='center', va='bottom')

# # 顯示圖表
# plt.grid(True, axis='y', linestyle='--', alpha=0.7)
# plt.show()

# 時間段和對應的人數
time_slots = ['時間一', '時間二', '時間三']
counts = [9, 5, 3]

# 設置圖表樣式
sns.set(style="whitegrid")

# 繪製條形圖
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x=time_slots, y=counts, palette="viridis")

# 添加數值標籤
for i, count in enumerate(counts):
    bar_plot.text(i, count + 0.1, f'{count}', ha='center', va='bottom', color='black', fontsize=12)

# 設置標題和標籤
plt.xlabel('時間段')
plt.ylabel('人數')
plt.title('不同時間段的參加人數')

# 顯示圖表
plt.show()
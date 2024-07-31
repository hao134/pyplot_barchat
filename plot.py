import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

# 設置 Matplotlib 使用 Microsoft JhengHei 字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 設置 Seaborn 主題
sns.set_theme(style="whitegrid")
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

# 時間段和對應的人數
time_slots = ['時間一\nfafa', '時間二', '時間三']
counts = [10, 9, 4]

# 繪製條形圖
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x=time_slots, y=counts, palette="viridis")

# 添加數值標籤
for i, count in enumerate(counts):
    bar_plot.text(i, count + 0.2, f'{count}', ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# 設置標籤和標題
plt.xlabel('時間段', fontsize=14, fontweight='bold')
plt.ylabel('人數', fontsize=14, fontweight='bold')
plt.title('不同時間段的參加人數', fontsize=16, fontweight='bold')

# 設置 y 軸範圍和網格
plt.ylim(0, 10)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# 移除上和右邊框
sns.despine()

# 顯示圖表
plt.show()


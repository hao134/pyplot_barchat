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

# 繪製橫條圖
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(y=time_slots, x=counts, palette="viridis")

# 添加數值標籤
for i, count in enumerate(counts):
    bar_plot.text(count + 0.2, i, f'{count}', ha='center', va='center', fontsize=12, fontweight='bold', color='black')

# 設置標籤和標題
plt.ylabel('時間段', fontsize=14, fontweight='bold')
plt.xlabel('人數', fontsize=14, fontweight='bold')
plt.title('不同時間段的參加人數', fontsize=16, fontweight='bold')

# 設置 x 軸範圍和網格
plt.xlim(0, 12)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# 移除上和右邊框
sns.despine()

# 顯示圖表
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 數據
data = {
    '時間段': ['時間一\n10/14(一)~\n10/15(二)', '時間一\n10/14(一)~\n10/15(二)', '時間二\n10/17(四)~\n10/18(五)', '時間二\n10/17(四)~\n10/18(五)', '時間三\n10/21(一)~\n10/22(二)', '時間三\n10/21(一)~\n10/22(二)'],
    '處': ['國勢普查處', '綜合統計處', '國勢普查處', '綜合統計處', '國勢普查處', '綜合統計處'],
    '人數': [9, 1, 5, 4, 3, 1]
}

# 創建 DataFrame
df = pd.DataFrame(data)

# 設置 Seaborn 主題
sns.set_theme(style="whitegrid")
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

# 確保時間段按照順序排列
df['時間段'] = pd.Categorical(df['時間段'], categories=['時間一\n10/14(一)~\n10/15(二)', '時間二\n10/17(四)~\n10/18(五)', '時間三\n10/21(一)~\n10/22(二)'], ordered=True)


# 創建數據透視表以便於堆積
df_pivot = df.pivot_table(index='時間段', columns='處', values='人數', aggfunc='sum', fill_value=0)
df_pivot = df_pivot[['國勢普查處', '綜合統計處']]

# 繪製堆積橫條圖
ax = df_pivot.plot(kind='barh', stacked=True, figsize=(10, 6), color=sns.color_palette("viridis", n_colors=2))

# 添加數值標籤
for p in ax.patches:
    width = p.get_width()
    plt.text(p.get_x() + width / 2, p.get_y() + p.get_height() / 2, f'{int(width)}', ha='center', va='center', fontsize=12, fontweight='bold', color='black')

# 設置標籤和標題
#plt.ylabel('時間段', fontsize=14, fontweight='bold')
plt.xlabel('人數', fontsize=14, fontweight='bold')
plt.title('不同時間段的參加人數', fontsize=16, fontweight='bold')

# 設置 x 軸範圍和網格
plt.xlim(0, 12)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# 隱藏 Y 軸標題
ax.set_ylabel('')


# 顯示圖表和圖例
plt.legend(title='處')
plt.show()

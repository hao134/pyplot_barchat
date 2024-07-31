import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 數據
data = {
    '時間段': ['時間一\n10/14(一)~\n10/15(二)', '時間一\n10/14(一)~\n10/15(二)', '時間二\n10/17(四)~\n10/18(五)', '時間二\n10/17(四)~\n10/18(五)', '時間三\n10/21(一)~\n10/22(二)', '時間三\n10/21(一)~\n10/22(二)'],
    '處': ['國勢普查處', '綜合統計處', '國勢普查處', '綜合統計處', '國勢普查處', '綜合統計處'],
    '人數': [9, 4, 5, 0, 3, 0]
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
    if width > 0:
        ax.annotate(f'{int(width)}',
                    (p.get_x() + width / 2, p.get_y() + p.get_height() / 2),
                    ha='center', va='center', fontsize=12, fontweight='bold', color='black')

# 設置標籤和標題
plt.xlabel('人數', fontsize=14, fontweight='bold')
plt.title('課程 使用T-SQL查詢資料 開課時間詢問', fontsize=16, fontweight='bold')

# 設置 x 軸範圍和網格
plt.xlim(0, 14)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# 移除 Y 軸標籤
ax.set_yticklabels([])

# 隱藏 Y 軸標題
ax.set_ylabel('')

# 自定義 Y 軸刻度標籤
labels = ['時間三\n10/21(一)~\n10/22(二)', '時間二\n10/17(四)~\n10/18(五)', '時間一\n10/14(一)~\n10/15(二)']
for i, label in enumerate(labels):
    lines = label.split('\n')
    y = len(labels) - i - 1
    ax.text(-1, y, lines[0],  ha='center',color='#000000', fontweight='bold',fontsize=12)
    ax.text(-1, y - 0.2, '\n'.join(lines[1:]), ha='center',color='black', fontsize=11)
    if i == 2:
        ax.text(-1, y, lines[0],  ha='center',color='#FF0080', fontweight='bold',fontsize=12)
        ax.text(-1, y - 0.2, '\n'.join(lines[1:]), ha='center',color='black', fontsize=11)

# 添加箭頭和註記
ax.annotate('13', xy=(13, 0), xytext=(14, 0),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, fontweight='bold', color='black', ha='center', va='center')

# 顯示圖表和圖例
plt.legend(title='處')
plt.show()

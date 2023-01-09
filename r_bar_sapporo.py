import matplotlib.pyplot as plt
import r_sapporo as rs

# 設定中文字型
plt.rcParams["font.family"] = "Microsoft JhengHei"
# plt.rcParams["font.size"] = 16

#設定畫布
plt.figure(figsize=(5,10))
color=["#A88460","#BCF5C3","#F5CCA3","#AB8CF5","#6883A8","#1EA89B","#2DAD46","#A83281"]
# # 繪圖 
# plt.subplot(1,2,1,facecolor="#FFE4C9")
# plt.pie(r_v,colors = color)
# plt.title("札幌車站附近美食評分比例表(圓餅圖)",fontsize=18)
# plt.legend(rating,loc=4)

# plt.subplot(1,2,2,facecolor="#CBEBF6")
plt.bar(rs.rating,rs.r_v,color = color)
plt.title("札幌車站附近美食評分比例表(長條圖)",fontsize=18)
plt.xticks(rotation=45)
for a,b in zip(rs.rating,rs.r_v):
    plt.text(a,b+1,b, ha='center', va= 'bottom',fontsize=13)
plt.xlabel("分數",fontsize=15)
plt.ylabel("店家數量",fontsize=15)
plt.ylim(0,120)
plt.savefig("r_bar.png")
plt.show()
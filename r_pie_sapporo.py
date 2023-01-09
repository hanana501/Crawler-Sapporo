import matplotlib.pyplot as plt
import r_sapporo as rs

# 設定中文字型
plt.rcParams["font.family"] = "Microsoft JhengHei"

#設定畫布
plt.figure(figsize=(10,10))
color=["#A88460","#BCF5C3","#F5CCA3","#AB8CF5","#6883A8","#1EA89B","#2DAD46","#A83281"]
# 繪圖 
plt.pie(rs.r_v,colors = color)
plt.title("札幌車站附近美食評分比例表(圓餅圖)",fontsize=25)
plt.legend(rs.rating,loc=4,fontsize=11)

plt.savefig("r_pie.png")
plt.show()
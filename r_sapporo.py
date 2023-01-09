import pandas as pd

data = "r_sapporo.csv"
file = pd.read_csv(data,encoding="utf-8")

#==================================================================
# 整理cuisine
file["cuisine"] = file["cuisine"].str.split('・').str.get(0)
file["cuisine"] = file["cuisine"].str.split('/').str.get(0)
file["cuisine"] = file["cuisine"].str.split('、').str.get(0)
c_o = ["咖哩","中國","炸","壽司","啤酒","咖啡","淇淋","聖代","鍋","甜","義","蕎麥","蛋糕","西式料理","飲茶","鬆餅","小酒館","丼","和式","日式料理","日式點心"]
c_n = ["咖哩飯","中國菜","炸物","壽司","酒吧","咖啡店","冰品","冰品","鍋物","甜點","義式料理","蕎麥麵","甜點","甜點","甜點","甜點","小酒館","丼飯","日式料理","日式料理","甜點"]
# print(file["cuisine"])
# for i in file["cuisine"]:
#     if "咖哩" in i :
#         file[["cuisine"]] = file[["cuisine"]].replace(i,"咖哩飯",regex = True)

for i in file["cuisine"]:
    for j in c_o:
        if j in i :
            file[["cuisine"]] = file[["cuisine"]].replace(i,c_n[c_o.index(j)],regex = True)
# 分類並設定值
C_g = file.groupby("cuisine")
C_g.size()
print(C_g.groups)
#==================================================================
# 整理rating
R_g = file.groupby("rating")
print(R_g.size())

rating = ["3.0~3.09","3.10~3.19","3.20~3.29","3.30~3.39","3.40~3.49","3.50~3.59","3.60~3.69","3.7(含)以上"]
r_v = [0 for i in range(8)]

for i in file["rating"]:
    if i < 3.10:
        r_v[0] += 1
    elif i < 3.20:
        r_v[1] += 1
    elif i < 3.30:
        r_v[2] += 1
    elif i < 3.40:
        r_v[3] += 1
    elif i < 3.50:
        r_v[4] += 1
    elif i < 3.60:
        r_v[5] += 1
    elif i < 3.70:
        r_v[6] += 1
    else:
        r_v[7] += 1
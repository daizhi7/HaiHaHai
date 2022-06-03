
import fsedafdfasfdsafg as fg
from matplotlib import pyplot as plt
# import numpy as np


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

content = fg.xlsxToHaiHaHai("./data/content2.xlsx", "Sheet1")


playerNames = fg.getInfo_(content, "姓名")
players = []


for i in range(len(playerNames)):
    _score = content[i]
    _player = fg.Player(playerNames[i], _score)
    players.append(_player)

# 1

literature = ["语文", "英语", "政治", "历史"]
science = ["数学", "物理", "化学"]

literatureFullScore = 120 + 90 + 60 * 2
scienceFullScore = 120 + 100 + 80

info_1 = []    # l
info_2 = []    # s

for p in players:


    literatureScore = 0

    for ls in literature:
        literatureScore += p.getScore(ls)

    literatureScoreRatio = float(literatureScore / literatureFullScore)
    info_1.append(literatureScoreRatio)

    scienceScore = 0

    for ss in science:
        scienceScore += p.getScore(ss)

    scienceScoreRatio = float(scienceScore / scienceFullScore)
    info_2.append(scienceScoreRatio)

colours = [0 + i*(int(100 / len(players))) for i in range(len(players))]

plt.scatter(info_1, info_2, s=60, alpha=0.5, c=colours, cmap='coolwarm_r')

# linear_model = np.polyfit(info_1, info_2, 1)
# linear_model_fn = np.poly1d(linear_model)
# x_s = np.arange(0, 0.9)
# plt.plot(x_s, linear_model_fn(x_s), color="green")


plt.title("得分率示意图")
plt.xlabel("文科得分率")
plt.ylabel("理科得分率")

plt.colorbar()




if __name__ == '__main__':
    plt.show()

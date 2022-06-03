
import numpy as np
import pandas as pd


pd.set_option('display.width', None)
np.set_printoptions(threshold=1145141919810)


def xlsxToHaiHaHai(xlsx, sheetName, writeDown=False):

    haiHaHai = pd.read_excel(xlsx, sheet_name=sheetName)

    taiTou = np.array(haiHaHai.columns)
    lie = np.array(haiHaHai.values)
    contentOutput = []

    for i in lie:
        playerInfo = dict(zip(taiTou, i))
        contentOutput.append(playerInfo)

    if writeDown:
        f = open("haiHaHai", 'w')
        f.write(str(contentOutput))
        f.close()

    return contentOutput


def getInfo_(haiHaHai, taiTouName):

    contentOutput = []

    for i in range(len(haiHaHai)):
        contentOutput.append(haiHaHai[i][taiTouName])

    return contentOutput


class Player:

    playerNumber = 0

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        Player.playerNumber += 1


    def __repr__(self):
        return self.name


    def getScore(self, subject):
        return self.scores[subject]




if __name__ == '__main__':
    # print(xlsxToHaiHaHai(xlsx="./data/content2.xlsx", sheetName="Sheet1", writeDown=False))
    print(getInfo_(xlsxToHaiHaHai("./data/content2.xlsx", "Sheet1"), "姓名"))



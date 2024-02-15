# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QListWidget,QWidget, QFileDialog,QListWidgetItem, QListView,QItemDelegate,QGridLayout,QSizePolicy
import sys
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import QByteArray, QSortFilterProxyModel,Qt,QSize
from ui_gui import Ui_MainWindow
from LoadData import read_json_file, pharse_json_file, cal_score


setname_chinesename = {
    "PasserbyofWanderingCloud": "云无留迹的过客",
    "MusketeerofWildWheat": "野穗伴行的快枪手",
    "KnightofPurityPalace": "净庭教宗的圣骑士",
    "HunterofGlacialForest": "密林卧雪的猎人",
    "ChampionofStreetwiseBoxing": "街头出身的拳王",
    "GuardofWutheringSnow": "戍卫风雪的铁卫",
    "FiresmithofLavaForging": "熔岩锻铸的火匠",
    "GeniusofBrilliantStars": "繁星璀璨的天才",
    "BandofSizzlingThunder": "激奏雷电的乐队",
    "EagleofTwilightLine": "晨昏交界的翔鹰",
    "ThiefofShootingMeteor": "流星追迹的怪盗",
    "WastelanderofBanditryDesert": "盗匪荒漠的废土客",
    "SpaceSealingStation": "太空封印站",
    "FleetoftheAgeless": "不老者的仙舟",
    "SprightlyVonwacq": "生命的翁瓦克",
    "PanGalacticCommercialEnterprise": "泛银河商业公司",
    "BelobogoftheArchitects": "筑城者的贝洛伯格",
    "TaliaKingdomofBanditry": "盗贼公国塔利亚",
    "CelestialDifferentiator": "星体差分机",
    "InertSalsotto": "停转的萨尔索图",
    "RutilantArena": "繁星竞技场",
    "BrokenKeel": "折断的龙骨",
    "LongevousDisciple": "宝命长存的莳者",
    "MessengerTraversingHackerspace": "骇域漫游的信使"
}

class LoginGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.relicdata = []
        self.relicdata_filtered = []

        super(LoginGui, self).__init__()   # 调用父类的初始化方法
        self.setupUi(self)                 #  调用Ui_MainWindow的setupUi方法布置界面
        self.pushButton_import.clicked.connect(self.import_json)
        self.comboBox_setname.currentTextChanged.connect(self.filter_text_changed)
        self.comboBox_position.currentTextChanged.connect(self.filter_text_changed)
        self.pushButton_calscore.clicked.connect(self.update_cal_config)
        self.pushButton_calscore.clicked.connect(self.filter_text_changed)
    def update_list_view(self):


        items_per_row = 3

        # 设置每个项目的宽度
        item_width = 200

        # 设置项目的大小
        item_size = QSize(item_width, self.listWidget.sizeHintForRow(0))

        # 设置每个项目的大小
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setSizeHint(item_size)

        # 设置列表视图的布局模式
        self.listWidget.setFlow(QListWidget.LeftToRight)
        self.listWidget.setWrapping(True)
        self.listWidget.setResizeMode(QListWidget.Adjust)

        # 创建布局并设置列表视图
        layout = QVBoxLayout(self)
        layout.addWidget(self.listWidget)
    def filter_text_changed(self):
        # 遍历列表项，根据筛选条件显示或隐藏项
        self.listWidget.clear()
        self.relicdata_filtered = []
        position_dict = {"head": "头", "hands": "手", "body": "衣服", "feet": "鞋", "planarSphere": "球", "linkRope": "绳"}
        setfilter = self.comboBox_setname.currentText()
        positionfilter = self.comboBox_position.currentText()
        for relic in self.relicdata:
            if setname_chinesename[relic.setname] == setfilter or setfilter == "不限":
                if position_dict[relic.position] == positionfilter or positionfilter == "不限":
                    self.relicdata_filtered.append(relic)
        self.add_images_to_list(self.relicdata_filtered)
    def import_json(self):
        fname, _ = QFileDialog.getOpenFileNames(self, '打开遗器数据文件', './', '(*.json)')
        json_data =read_json_file(fname[0])
        self.relicdata = pharse_json_file(json_data, self.load_config(self.comboBox_config.currentText()))
        self.add_images_to_list(self.relicdata)
        self.add_setname_to_list(self.relicdata)
    def update_cal_config(self):
        relic_list_new = []
        for relic in self.relicdata:
            relic_with_score =cal_score(relic, self.load_config(self.comboBox_config.currentText()))
            relic_list_new.append(relic_with_score)
        self.relicdata = relic_list_new
        self.add_images_to_list(self.relicdata)
    def sort_key(self,relic):
        return round(sum(relic.score), 2)
    def add_images_to_list(self, relic_list):
        # 添加图片到列表中
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.clear()
        position_dict = {"head": 0, "hands": 1, "body": 2, "feet": 3, "planarSphere": 0, "linkRope": 1}
        sorted_relic_list = sorted(relic_list, key=self.sort_key, reverse=True)
        for relic in sorted_relic_list:
            if relic.maintag['name'] == "生命值" or relic.maintag['name'] == "攻击力" or relic.maintag['name'] == "速度":
                maintag = f"{relic.maintag['name']}-{relic.maintag['value']}({relic.score[0]})分\n"
            else:
                maintag = f"{relic.maintag['name']}-{relic.maintag['value']*100:.2f}%({relic.score[0]})分\n"
            normaltags = relic.normaltags
            normaltag = ""
            length = 1
            for tag in normaltags:
                if tag["name"] == "攻击力" or tag["name"] == "防御力" or tag["name"] == "生命值" or tag["name"] == "速度":
                    normaltag += f"{tag['name']} > {tag['value']}({relic.score[length]})分\n"
                else:
                    normaltag += f"{tag['name']} > {tag['value']*100:.2f}%({relic.score[length]})分\n"
                length += 1
            # print(maintag,normaltags)
            image = QImage(f'./icon/{relic.setname}-{position_dict[relic.position]}.png')
            pixmap = QPixmap(image).scaledToWidth(200)
            # isEquipped = relic.equip
            # if isEquipped:
            #     isEquipped = "已装备"
            # else:
            #     isEquipped = "未装备"
            # item = QListWidgetItem(QIcon(pixmap), f'{relic.chinesename}({round(sum(relic.score),2)}分)|{relic.level}级|{maintag}{normaltag}')
            item = QListWidgetItem(QIcon(pixmap),
                                   f'{relic.chinesename}\n{round(sum(relic.score),2)}分\n{relic.level}级\n{maintag}{normaltag}')
            item.setToolTip(f"{maintag}{normaltag}")
            item.setTextAlignment(Qt.AlignCenter)
            self.listWidget.addItem(item)
            self.update_list_view()

    def add_setname_to_list(self,relic_list):
        setname_list = [relic.setname for relic in relic_list]
        unique_setname_list = list(set(setname_list))
        for unique_setname in unique_setname_list:
            self.comboBox_setname.addItem(setname_chinesename[unique_setname])
    def load_config(self, name):
        config_all = {
            "银狼": [0.5, 0, 0.5, 0.75, 0, 0, 0, 1, 0.75, 1, 1, 0,"量子"],
            "黑塔": [0, 0.75, 0, 0.75, 1, 1, 0, 0, 0, 1, 0.5, 0,"冰"],
            "布洛妮娅": [0.75, 0.5, 0.5, 1, 0, 1, 0, 0, 0.5, 1, 1, 0,"风"],
            "停云": [0.75, 1, 0.5, 1, 0, 0, 0, 0, 0.5, 1, 1, 0, "雷"],
            "符玄": [1, 0, 0.75, 1, 0, 0, 0, 0, 0.75, 0, 1, 1, "量子"],
            "镜流": [0, 0.75, 0, 0.75, 0.85, 1, 0, 0, 0, 1, 1, 0, "冰"],
            "饮月": [0, 0.75, 0, 0.5, 1, 1, 0, 0, 0, 1, 1, 0, "量子"],
            "阮梅": [0.75, 0, 0.5, 1, 0, 0, 1, 0, 0.5, 1, 1, 0, "冰"],
        }
        # 物理, 火, 冰, 雷, 风, 量子,虚数
        config = {'生命值': config_all[name][0],
                        '生命值百分比': config_all[name][0],
                        '攻击力': config_all[name][1],
                        '攻击力百分比': config_all[name][1],
                        '防御力': config_all[name][2],
                        '防御力百分比': config_all[name][2],
                        '速度': config_all[name][3],
                        '暴击率': config_all[name][4],
                        '暴击伤害': config_all[name][5],
                        '击破特攻': config_all[name][6],
                        '效果命中': config_all[name][7],
                        '效果抵抗': config_all[name][8],
                        "能量恢复效率": config_all[name][10],
                        "治疗量加成": config_all[name][11],
                        "虚数属性伤害提高": 0,
                        "量子属性伤害提高": 0,
                        "风属性伤害提高": 0,
                        "雷属性伤害提高": 0,
                        "冰属性伤害提高": 0,
                        "火属性伤害提高": 0,
                        "物理属性伤害提高": 0,
                        }
        config[f"{config_all[name][12]}属性伤害提高"] = config_all[name][9]
        return config
if __name__ == '__main__':
    app = QApplication([])
    gui = LoginGui()
    gui.show()
    app.exec_()
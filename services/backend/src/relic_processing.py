import json


class Coefficient:
    def __init__(self, hp, hp_, atk, atk_, def_value, def_, spd, crit_rate, crit_dmg, break_, eff, eff_res,heal, ener_regen,
                 imaginary_dmg=0, quantum_dmg=0, wind_dmg=0, lightning_dmg=0, ice_dmg=0, fire_dmg=0, physical_dmg=0):
        """
        用于存储计算系数
        :param hp: 生命值
        :param hp_: 生命值百分比
        :param atk: 攻击力
        :param atk_: 攻击力百分比
        :param def_value: 防御力
        :param def_: 防御力百分比
        :param spd: 速度
        :param crit_rate: 暴击率
        :param crit_dmg: 暴击伤害
        :param break_: 击破特攻
        :param eff: 效果命中
        :param eff_res: 效果抵抗
        :param heal: 治疗量加成
        :param ener_regen: 能量恢复率
        :param imaginary_dmg: 虚数属性伤害提高
        :param quantum_dmg: 量子属性伤害提高
        :param wind_dmg: 风属性伤害提高
        :param lightning_dmg: 雷属性伤害提高
        :param ice_dmg: 冰属性伤害提高
        :param fire_dmg: 火属性伤害提高
        :param physical_dmg: 物理属性伤害提高
        """
        self.attributes = {
            "hp": hp,
            "hp_": hp_,
            "atk": atk,
            "atk_": atk_,
            "def": def_value,
            "def_": def_,
            "spd": spd,
            "critRate": crit_rate,
            "critDMG": crit_dmg,
            "break": break_,
            "eff": eff,
            "eff_res": eff_res,
            "imaginaryDmg": imaginary_dmg,
            "quantumDmg": quantum_dmg,
            "windDmg": wind_dmg,
            "lightningDmg": lightning_dmg,
            "iceDmg": ice_dmg,
            "fireDmg": fire_dmg,
            "physicalDmg": physical_dmg,
            "heal": heal,
            "enerRegen": ener_regen
        }

class Relic:
    def __init__(self, set_name, position, main_tag, normal_tags, omit, level, star, equip):
        """
        用于存储遗器数据
        :param set_name: 套装名称
        :param position: 遗器位置
        :param main_tag: 主词条
        :param normal_tags: 副词条
        :param omit: 待定
        :param level: 遗器等级
        :param star: 遗器星级
        :param equip: 待定
        """
        self.set_name = set_name
        self.position = position
        self.main_tag = Tag(name=main_tag["name"], value=main_tag["value"])
        self.normal_tags = [Tag(name=normal_tag["name"], value=normal_tag["value"]) for normal_tag in normal_tags]
        self.omit = omit
        self.level = level
        self.star = star
        self.equip = equip
    def to_dict(self):
        return {
            "set_name": self.set_name,
            "position": self.position,
            "main_tag": self.main_tag.to_dict(),
            "normal_tags": [tag.to_dict() for tag in self.normal_tags],
            "omit": self.omit,
            "level": self.level,
            "star": self.star,
            "equip": self.equip,
        }
class Tag:
    def __init__(self, name, value, score=0, powerup=0, entries=0):
        """
        用于存储词条数据
        :param name: 词条名称
        :param value: 词条属性
        :param score: 词条评分
        :param powerup: 词条强化等级
        :param entries: 有效词条数
        """
        self.name = name
        self.value = value
        self.score = score
        self.powerup = powerup
        self.entries = entries
    def to_dict(self):
        return {"name": self.name, "value": self.value, "score": self.score, "powerup": self.powerup, "entries": self.entries}


def loadJsonFile(file_path):
    """
    测试时用于读取json文件
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到.")
    except json.JSONDecodeError:
        print(f"无法解码文件 '{file_path}' 中的 JSON 数据.")
    except Exception as e:
        print(f"发生了一个错误: {str(e)}")
def loadScoreConfig(name):
    """
    用于读取角色遗器评分系数
    :param name:
    :return:
    """
    config_all = {
        "银狼": [0.5, 0, 0.5, 0.75, 0, 0, 0, 1, 0.75, 1, 1, 0,"quantum"],
        "黑塔": [0, 0.75, 0, 0.75, 1, 1, 0, 0, 0, 1, 0.5, 0,"ice"],
        "布洛妮娅": [0.75, 0.5, 0.5, 1, 0, 1, 0, 0, 0.5, 1, 1, 0,"wind"],
        "停云": [0.75, 1, 0.5, 1, 0, 0, 0, 0, 0.5, 1, 1, 0, "lightning"],
        "符玄": [1, 0, 0.75, 1, 0, 0, 0, 0, 0.75, 0, 1, 1, "quantum"],
        "镜流": [0, 0.75, 0, 0.75, 0.85, 1, 0, 0, 0, 1, 1, 0, "ice"],
        "饮月": [0, 0.75, 0, 0.5, 1, 1, 0, 0, 0, 1, 1, 0, "quantum"],
        "阮梅": [0.75, 0, 0.5, 1, 0, 0, 1, 0, 0.5, 1, 1, 0, "ice"],
    }
    return Coefficient(hp=config_all[name][0], hp_=config_all[name][0], atk=config_all[name][1], atk_=config_all[name][1],
                       def_value=config_all[name][2], def_=config_all[name][2], spd=config_all[name][3], crit_rate=config_all[name][4],
                       crit_dmg=config_all[name][5], break_=config_all[name][6], eff=config_all[name][7], eff_res=config_all[name][8],
                       ener_regen=config_all[name][10], heal=config_all[name][11],**{f"{config_all[name][12]}_dmg": config_all[name][9]})

def calculateRelicScore(relic_data: Relic, score_config=loadScoreConfig("黑塔")):
    """
    计算遗器分数
    :param relic_data: 遗器数据
    :param score_config: 角色评分系数
    :return:
    """
    # 平均单词条数值
    average = {'hp': 37.93,
               'hp_': 0.0389,
               'atk': 18.96,
               'atk_': 0.0389,
               'def_': 0.0486,
               'spd': 2.3,
               'critRate': 0.02916,
               'critDMG': 0.0583,
               'break': 0.0583,
               'eff': 0.0389,
               'def': 18.96,
               'effRes': 0.0389}
    # 基础词条系数
    coefficient = Coefficient(hp=0.153 * 0.5, hp_=1.5, atk=0.3 * 0.5, atk_=1.5 * 100, def_value=0.3*0.5, def_=1.19 * 100,spd=2.53, crit_rate=2*100,crit_dmg=1*100,
                break_=1*100, eff=1.49*100, eff_res=1.49*100, imaginary_dmg=1, quantum_dmg=1,wind_dmg=1,lightning_dmg=1,ice_dmg=1,fire_dmg=1,
                physical_dmg=1,heal=1,ener_regen=1)

    # 计算主词条分数
    position = relic_data.position
    level = relic_data.level
    entriesSum = 0

    # 计算主词条评分
    if position in ["head", "hands"]:
        score_main = 0
    elif position in ["body", "planarSphere"]:
        score_main = 0.66 * level + 5.83 * score_config.attributes.get(relic_data.main_tag.name)
    else:
        score_main = 5.83 * score_config.attributes.get(relic_data.main_tag.name)
    relic_data.main_tag.score = score_main

    # 计算副词条评分
    for tag in relic_data.normal_tags:
        name = tag.name
        value = tag.value
        try:
            score = round(value * coefficient.attributes.get(name) * score_config.attributes.get(name), 1)
            powerup = round(value / average[name]) - 1
        except:
            score = 0
            powerup = 0
        # 计算有效词条数
        if score_config.attributes.get(name) != None and score_config.attributes.get(name) > 0:
            entries = value / average[name]
            entriesSum += entries
        tag.score = score
        tag.powerup = powerup
        tag.entry = entriesSum
    return relic_data


def processRelicFromJson(relic_data):
    # 解析 JSON 数据
    # relic_data = loadJsonFile("C:\\Users\LEGION\Documents\GitHub\FireflyHelper\\tests\\march7th.min.json")
    relic_data_new = []
    print(type(relic_data))
    del(relic_data["version"])
    # 调用 calculateRelicScore 函数，传递遗器数据
    for relic_position in relic_data.values():
        print(relic_position)
        for relic in relic_position:
            raw_relic = Relic(set_name=relic["setName"], position=relic["position"], main_tag=relic["mainTag"], normal_tags=relic["normalTags"], omit=relic["omit"], level=relic["level"], star=relic["star"], equip=relic["equip"])
            relic_data_new.append(calculateRelicScore(raw_relic).to_dict())
    return relic_data_new
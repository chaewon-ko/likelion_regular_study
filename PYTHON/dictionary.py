from distutils.log import info


information = {"고향":"서울","취미":"유튜브","좋아하는 음식":"양꼬치"}
print(information)

information = {"특기":"피아노", "사는 곳":"분당"}
print(information.get("특기"))
print(information.get("사는 곳"))

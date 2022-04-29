information = {"고향":"서울", "취미":"유튜브","좋아하는 음식":"양꼬치"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))

information["특기"] = "피아노"
information["사는곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information))
information.clear()
print(information)
print(foods[-2])
foods.append("김밥")
print(foods)
del foods[1]
print(foods)
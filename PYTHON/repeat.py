import random
import time

for x in range(30):
    print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))

while True:    
    print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))
    break
    print("이 문장도 반복되나")
    time.sleep(1)
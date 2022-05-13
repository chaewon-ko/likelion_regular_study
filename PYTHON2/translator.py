from googletrans import Translator

translator = Translator()

#sentence = "안녕하세요 고채원입니다."
sentence = input("문장을 입력하세요: ") # 사용자에게 감지할 문장 받기
dest = input("어떤 언어로 번역을 원하시나요? ") # 사용자에게 번역될 언어 받기(지정된 것만 사용 가능)

# print(detected.lang)

result = translator.translate(sentence, dest) #사용자가 원하는 언어로 번역하기
detected = translator.detect(sentence) # 감지결과 detected 안에 넣어주기. detect는 translator안의 언어감지 함수

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("================================")
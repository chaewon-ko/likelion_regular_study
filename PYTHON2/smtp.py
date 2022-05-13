import smtplib
from email.message import EmailMessage 
import imghdr
import re
# smtplib의 SMTP 함수 사용해서 gmail의 smtp 서버에 연결하기
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

#이메일 주소가 유효할 경우에만 메일 전송하는 함수
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage() # EmailMessage 기능으로 mime 타입의 message 변수(통) 만들기
message.set_content("코드라이언 수업중입니다.") # mime 형태의 통 안에 본문 내용 담기

message["Subject"] = "이것은 제목입니다."
message["From"] = "njs0657@likelion.org"
message["To"] = "njs06577@gmail.com"

#image = open("ryan.png","rb") #이미지 파일 읽기
#print(image.read()) #파일 읽어서 출력하기 read()

# close 없이 안전하게 파일 열고 사용하고 닫기
with open("C:/Users/chaewon/Desktop/regular_study/PYTHON2/ryan.png","rb") as image: # read binary 모드로 읽은 파일을 image라 명명
    image_file = image.read() # image 읽은 내용을 image_file 변수 안에 저장

image_type = imghdr.what('ryan',image_file)

message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) # smtp 서버에 연결하고 그 정보 smtp 변수에 담아 return
smtp.login("njs0657@likelion.org","########")
# 메일을 보내는 sendEmail 함수를 호출, 인수는 유효성 검사할 메일주소
sendEmail("njs0657@likelionorg")
smtp.quit

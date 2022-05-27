
# pdf2image에서 covert_from_path 함수
from pdf2image import convert_from_path

# convert_from_path를 이용해 pdf파일를 이미지형태로 불러온다.
images = convert_from_path('school.pdf')
# images는 여러 페이지로 구성되어 있어 아래와 같이 각각의 페이지(이미지)를 jpg로 저장한다.
for i, image in enumerate(images):
    image.save("school" + str(i) + ".jpg", "JPEG")
print('conversion complete')

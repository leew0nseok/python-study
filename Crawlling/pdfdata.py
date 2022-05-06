# -*- encoding:utf-8
from tika import parser

print("텍스트 파일을 추출할 PDF파일명을 입력하세요.")

PDFfileName = "school.pdf"

print("텍스트 파일은 다음 폴더에 저장됩니다.")
print("D:\data")

inputpath = PDFfileName

parsed = parser.from_file(PDFfileName)
print(parsed["content"])

fileOut = open('fileOut.txt', 'w', encoding='utf-8')

print(parsed['content'], file=fileOut)

fileOut.close()

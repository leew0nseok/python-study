# step1.관련 모듈 import
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

PdfFilePath = "school.pdf"


# step2.기존 pdf 불러오기
pdfReader = PdfFileReader(PdfFilePath, "rb")

pdfPage = pdfReader.getPage(2)
msg = pdfPage.extractText()

print(msg)


# # step3.새로 만들 pdf 객체 생성
# pdfWriter = PdfFileWriter()

# # step4.기존의 1번 페이지를 가져와서 새로만든 pdf에 붙여넣기
# pdfWriter.addPage(pdfReader.getPage(1))

# print(pdfWriter.getNumPages())

# # step5.1번 페이지가 붙여진 새로운 pdf 파일을 현재 경로('./')에 원하는 이름으로 저장
# pdfWriter.write(open("./추출한 테스트 PDF 파일.pdf", "wb"))


'''
#PyPDF2 pdf 페이지 추출
def extract_pdf_pages(pdf_file_path, pdf_out_file_path, page_list_to_extract):
    with open(pdf_file_path, 'rb') as src_pdf_file:
        pdf_reader = PdfFileReader(src_pdf_file)
        pdf_writer = PdfFileWriter()
        # PDF 첫 번째 페이지를 추출하려면 정수 1이 아닌 0을 전달해야 한다.
        for page_number in page_list_to_extract:
            pdf_writer.addPage(pdf_reader.getPage(page_number))

        # Source PDF 파일의 스트림을 끊기 전에 output PDF 파일을 write해야 한다.
        with open(pdf_out_file_path, 'wb') as out_file:
            pdf_writer.write(out_file)


extract_pdf_pages(PdfFilePath, "./예제.pdf", range(0, 35, 2))

'''

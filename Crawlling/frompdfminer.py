from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer
from PIL import Image
# Open a PDF file.
fp = open('school.pdf', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Create a PDF device object.
device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)


def parse_obj(lt_objs, str):

    # loop over the object list
    for obj in lt_objs:

        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            if str in obj.get_text():
                '''
                print ("%6d %6d %6d %6d %s" % (obj.bbox[0], obj.bbox[3],
                                           obj.bbox[2], obj.bbox[1],
                                           obj.get_text().replace('\n', '_')))
                                           '''
                return obj.bbox[0], obj.bbox[3], obj.bbox[2], obj.bbox[1]
            else:
                continue
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs)


# loop over all pages in the document
pg = input()  # pagenumber
pgint = int(pg)  # 찾을 문자열
str = input()
n = 0
for page in PDFPage.create_pages(document):
    n = n+1
    if n == pgint:
        # read the page :into a layout object
        interpreter.process_page(page)
        layout = device.get_result()

    # extract text from this object
        a, b, c, d = parse_obj(layout._objs, str)
        # print(a,b,c,d)

        img = Image.open(r"school"+pg+".jpg")
    # image size = 590x834
        img = img.resize((590, 834))
    # x start, y start, x length, y length
        crop_area = (a, 834-b, 590, 834)

        cropped_img = img.crop(crop_area)
        cropped_img.show()
        cropped_img.save('test-croped' + '.jpg', 'JPEG')

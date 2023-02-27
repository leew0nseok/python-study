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


def parse_obj2(lt_objs, n):
    title = []
    # loop over the object list
    for obj in lt_objs:

        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            if obj.bbox[0] <= n and not obj.get_text().startswith("  "):
                '''
                print ("%6d %6d %6d %6d %s" % (obj.bbox[0], obj.bbox[3],
                                           obj.bbox[2], obj.bbox[1],
                                           obj.get_text().replace('\n', '_')))
                                           '''
                title.append(obj.bbox[3])  # y 값 리스트에 넣기
                print(obj.get_text())
                print(obj.bbox[0])
            else:
                continue
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs)
    return title


# loop over all pages in the document

def capture_img(pg, strr=None):  # pg = pagenumber, str = 찾을 문자열
    pg = str(pg)
    pgint = int(pg)
    n = 0
    for page in PDFPage.create_pages(document):
        n = n+1
        if n == pgint:
            # read the page :into a layout object
            interpreter.process_page(page)
            layout = device.get_result()

        # extract text from this object
            title = parse_obj2(layout._objs, 56.7)
            print(title)
            a, b, c, d = parse_obj(layout._objs, strr)
            # print(a,b,c,d)

            img = Image.open(r"school"+pg+".jpg")
        # image size = 590x834
            img = img.resize((590, 834))
        # x start, y start, x length, y length
            if len(title) > 0:
                for i in title:
                    if d >= i:
                        d = i
                        crop_area = (a, 834-b, 590, 834-d)
                        break
                    else:
                        crop_area = (a, 834-b, 590, 770)
            else:
                crop_area = (0, 834-b, 590, 770)

            cropped_img = img.crop(crop_area)
            # cropped_img.show()
            cropped_img.save('sendimgfile' + '.jpg', 'JPEG')

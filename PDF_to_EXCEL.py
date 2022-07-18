import tabula

#df = tabula.read_pdf("C:/Users/felip/Downloads/CV.pdf", pages="all", encoding="utf-8", java_options=None, pandas_options=None, multiple_tables=True, user_agent=None)

#tabula.convert_into("C:/Users/felip/Downloads/CV.pdf", "C:/Users/felip/Downloads/aCb.csv", output_format="csv", pages='all', silent=True)

from PyPDF2 import PdfReader
import pandas as pd

reader = PdfReader("C:/Users/felip/Downloads/abril_2022.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[6]
text = page.extract_text()

print(text)
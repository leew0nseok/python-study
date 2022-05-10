from tika import parser  # pip install tika

raw = parser.from_file('school.pdf')
contents = raw['content']
contents = contents.strip()
print(contents)

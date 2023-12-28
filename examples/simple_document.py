import docxcompose as docx


def main():
    doc = docx.Document('Hello world!')
    doc.save('hello.docx')


if __name__ == '__main__':
    main()

import docxcompose as docx


def main():
    doc = docx.Document(docx.Hyperlink('https://google.com', 'Google'))
    doc.save('hyperlink.docx')

if __name__ == '__main__':
    main()

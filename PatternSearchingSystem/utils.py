from docx import Document
import PyPDF2


def read_file(filepath):

    # TXT FILE
    if filepath.endswith(".txt"):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    # DOCX FILE
    elif filepath.endswith(".docx"):

        doc = Document(filepath)

        full_text = []

        for para in doc.paragraphs:

            full_text.append(
                para.text
            )

        return "\n".join(full_text)

    # PDF FILE
    elif filepath.endswith(".pdf"):

        text = ""

        with open(
            filepath,
            "rb"
        ) as file:

            reader = PyPDF2.PdfReader(
                file
            )

            for page in reader.pages:

                text += (
                    page.extract_text()
                )

        return text

    return ""
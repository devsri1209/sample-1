from algorithms import *
from visualization import *
from report_generator import generate_pdf_report

from docx import Document


# ---------- READ TXT OR DOCX ----------
def read_file(file_path):

    if file_path.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        full_text = []

        for para in doc.paragraphs:
            full_text.append(para.text)

        return "\n".join(full_text)

    else:
        print("Unsupported File Format")
        return ""


# ---------- DISPLAY HIGHLIGHTED MATCHES ----------
def highlight_matches(text, pattern):

    highlighted = text.replace(
        pattern,
        f"<<{pattern}>>"
    )

    return highlighted


# ---------- MAIN PROGRAM ----------
print("\n========== PATTERN SEARCHING SYSTEM ==========\n")

file_path = input("Enter file path (.txt or .docx): ")

pattern = input("Enter search pattern: ")

case_choice = input("Case Sensitive Search? (yes/no): ")


# ---------- READ FILE ----------
text = read_file(file_path)

if not text:
    print("No text found")
    exit()


# ---------- CASE HANDLING ----------
if case_choice.lower() == "no":

    original_text = text

    text = text.lower()

    pattern = pattern.lower()

else:
    original_text = text


# ---------- RUN ALGORITHMS ----------
results = {}

print("\nSearching...\n")

results["Naive"] = naive_search(text, pattern)

results["KMP"] = kmp_search(text, pattern)

results["Rabin-Karp"] = rabin_karp_search(text, pattern)


# ---------- DISPLAY RESULTS ----------
for algo in results:

    print("\n===================================")
    print("Algorithm:", algo)

    print("Matches Found:",
          len(results[algo]["positions"]))

    print("Match Positions:",
          results[algo]["positions"])

    print("Execution Time:",
          round(results[algo]["time"], 6),
          "seconds")

    print("Comparisons:",
          results[algo]["comparisons"])


# ---------- HIGHLIGHT MATCHES ----------
print("\n========== HIGHLIGHTED TEXT ==========\n")

highlighted_text = highlight_matches(
    original_text,
    pattern
)

print(highlighted_text)


# ---------- FIND FASTEST ALGORITHM ----------
fastest = min(
    results,
    key=lambda x: results[x]["time"]
)

print("\n===================================")
print("FASTEST ALGORITHM:", fastest)
print("Execution Time:",
      round(results[fastest]["time"], 6),
      "seconds")


# ---------- TOTAL MATCHES ----------
total_matches = len(results["Naive"]["positions"])

print("\nTOTAL MATCHES FOUND:", total_matches)


# ---------- SHOW GRAPHS ----------
plot_execution_time(results)

plot_match_count(results)

plot_comparisons(results)


# ---------- GENERATE PDF REPORT ----------
generate_pdf_report(results, pattern)


# ---------- SUCCESS MESSAGE ----------
print("\n===================================")
print("PDF REPORT GENERATED SUCCESSFULLY")
print("File Name: Pattern_Search_Report.pdf")
print("===================================")
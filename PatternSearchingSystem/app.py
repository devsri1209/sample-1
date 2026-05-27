from flask import Flask, render_template, request
import os
import time
import psutil

from utils import read_file

from algorithms import (
    naive_search,
    kmp_search,
    rabin_karp,
    boyer_moore
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    file = request.files["file"]

    pattern = request.form["pattern"]

    algorithm = request.form["algorithm"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    text = read_file(filepath)

    text = text.lower()

    pattern = pattern.lower()

    start_time = time.time()

    start_memory = (
        psutil.Process().memory_info().rss
    )

    # SELECT ALGORITHM
    if algorithm == "naive":

        matches = naive_search(
            text,
            pattern
        )

    elif algorithm == "kmp":

        matches = kmp_search(
            text,
            pattern
        )

    elif algorithm == "rabin":

        matches = rabin_karp(
            text,
            pattern
        )

    elif algorithm == "boyer":

        matches = boyer_moore(
            text,
            pattern
        )

    end_time = time.time()

    end_memory = (
        psutil.Process().memory_info().rss
    )

    execution_time = (
        end_time - start_time
    )

    memory_used = (
        end_memory - start_memory
    ) / 1024

    plagiarism_percentage = (
        (
            len(matches)
            * len(pattern)
        ) / len(text)
    ) * 100

    return render_template(

        "index.html",

        total_matches=len(matches),

        positions=matches,

        execution_time=round(
            execution_time,
            6
        ),

        memory_used=round(
            memory_used,
            2
        ),

        plagiarism_percentage=round(
            plagiarism_percentage,
            2
        ),

        selected_algorithm=algorithm
    )


if __name__ == "__main__":

    app.run(debug=True)
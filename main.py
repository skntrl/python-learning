def read_data(filepath):
    """Reads a text file and returns a raw string"""
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}.")
        return None


def clean_and_tokenize(raw_text):
    """Sanitize the text and break it into a list of words."""
    clean_text = raw_text.lower()
    clean_text = clean_text.replace(".", "").replace("!", "").replace(",", "")
    return clean_text.split()


def get_top_words(words, limit=3):
    """Count Frequencies and returns the Top 3 words."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:limit]


def save_results(top_words, output_filepath):
    """Writes the formatted results to a text file."""
    with open(output_filepath, "w") as file:
        file.write(f"--- Top {len(top_words)} Words ---\n")
        for word, count in top_words:
            file.write(f"{word}: {count}\n")


def main():
    """The orchestrator: manages the flow of data between functions."""
    # 1. Read the data
    text = read_data("sample.txt")
    if not text:
        return

    # 2. Process
    words = clean_and_tokenize(text)

    # 3. Analyze
    top_3 = get_top_words(words, limit=3)

    # 4. Output
    save_results(top_3, "results.txt")
    print("Analysis Complete. Check results.txt!")


if __name__ == "__main__":
    main()

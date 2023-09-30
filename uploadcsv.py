import csv
import ltsuggest

# Define the URL of the LibreTranslate suggest endpoint
url = "http://localhost:5000"

# Define the CSV file path
csv_file = "suggestions.csv"

# Open the CSV file and read suggestions
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        q = row['Original']  # Original text
        s = row['Suggested']  # Suggested translation
        source = row['Source']  # Language of original text
        target = row['Target']  # Language of suggested translation

        # Call the suggest_translation function
        response = ltsuggest.suggest_translation(url, q, s, source, target)

        print(f"Translation for '{q}' from {source} to {target}:")
        print("Status code: " + str(response.status_code))
        print(response.json())

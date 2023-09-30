import ltsuggest

# Define the URL of the LibreTranslate suggest endpoint
url = "http://localhost:5000/"
# url = "https://libretranslate.com/"

# Define your input parameters
q = "Hello world!"  # Original text
s = "¡Hola mundo!"  # Suggested translation
source = "en"       # Language of original text
target = "es"       # Language of suggested translation

# Call the suggest_translation function
response = ltsuggest.suggest_translation(url, q, s, source, target)

print("Status code: " + str(response.status_code))
print(response.json())
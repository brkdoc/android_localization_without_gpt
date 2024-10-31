import os


def convert_to_dict(multilingual_text):
    # Split the text into lines and initialize an empty dictionary
    lines = multilingual_text.strip().splitlines()
    translations = {}

    # Define language code mappings
    lang_codes = {
        "EN": "en",
        "TR": "tr",
        "PT": "pt-rBR",
        "ES": "es",
        "DE": "de",
        "FR": "fr",
        "JA": "ja"
    }

    # Loop over each line to populate the dictionary
    for line in lines:
        # Ensure line contains ": " to split
        if ": " in line:
            lang, text = line.split(": ", 1)
            # Get the corresponding language code and add to the dictionary
            lang_code = lang_codes.get(lang.strip().upper())
            if lang_code:
                translations[lang_code] = text.strip()
        else:
            print(f"Skipping malformed line: {line}")

    return translations


def create_or_update_language_file(base_path, lang_code, translation_text, string_name):
    # Define the directory and file path based on the language code
    dir_name = f"values-{lang_code}" if lang_code != 'en' else "values"
    dir_path = os.path.join(base_path, dir_name)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, "strings.xml")

    # Define the new <string> line to add
    new_string_line = f'    <string name="{string_name}">{translation_text}</string>\n'

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Find the position of the closing </resources> tag
        for i, line in enumerate(lines):
            if line.strip() == "</resources>":
                # Insert the new <string> line right before the closing tag
                lines.insert(i, new_string_line)
                break

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
    else:
        # If the file doesn't exist, create a new one with <resources> and the <string> entry
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('<?xml version="1.0" encoding="utf-8"?>\n<resources xmlns:tools="http://schemas.android.com/tools">\n')
            file.write(new_string_line)
            file.write('</resources>\n')


# Collect multiline input for multilingual text, end on blank line
print("Enter the multilingual text line by line (e.g., EN: Text TR: Text). Press Double 'Enter' on an empty line to finish input:")
multilingual_text_lines = []
while True:
    line = input()
    if line.strip() == "":  # End input if the line is empty
        break
    multilingual_text_lines.append(line)

# Join all lines into a single string
multilingual_text = "\n".join(multilingual_text_lines)

# Collect the string name
string_name = input("Enter the name for the string (e.g., decline_call_request): ")
base_path = r"C:\Users\BURAK\StudioProjects\Sociable-Android\Forplay\app\src\main\res"  # Enter your custom path

# Convert the text to dictionary format
translations_dict = convert_to_dict(multilingual_text)

# Add translations to each language-specific XML file
for lang_code, translation_text in translations_dict.items():
    create_or_update_language_file(base_path, lang_code, translation_text, string_name)

print("Translations have been added to the respective language files in the Android project structure.")
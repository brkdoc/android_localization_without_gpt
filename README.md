# Android Localization Automation Script

This Python script automates the process of adding multilingual string translations into an Android project. It reads user-inputted multilingual text, identifies language codes, and saves each translation into the respective language-specific `strings.xml` files within the Android project structure.

## Features

- Supports multiple languages, including English, Turkish, Portuguese, Spanish, German, French, and Japanese.
- Automatically creates or updates `strings.xml` files in each language's folder (`values-[language_code]`).
- Appends new translations or updates existing ones without overwriting the entire XML file.

## Prerequisites

- Python 3.x

## Usage

### 1. Clone the repository or copy the script to your local environment.

### 2. Run the script:

   ```bash
   python main.py

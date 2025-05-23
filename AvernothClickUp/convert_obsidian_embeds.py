import os
import re

# Update this to the path of your Obsidian vault
VAULT_DIR = "./"

# Folder for your attachments/images
IMAGE_FOLDER = "Attachments"

# File extensions to consider
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp")

def convert_embeds(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for Obsidian-style embeds
    pattern = r'!\[\[(.*?)\]\]'

    def replacer(match):
        filename = match.group(1)
        # If in a folder like Attachments/, prepend that
        return f'![{os.path.splitext(filename)[0]}]({IMAGE_FOLDER}/{filename.replace(" ", "%20")})'

    converted = re.sub(pattern, replacer, content)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(converted)
    print(f"Converted: {md_file}")

# Walk through all markdown files
for root, _, files in os.walk(VAULT_DIR):
    for file in files:
        if file.endswith(".md"):
            convert_embeds(os.path.join(root, file))

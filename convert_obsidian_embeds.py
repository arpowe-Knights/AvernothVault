import os
import re

# Update this to the path of your Obsidian vault
VAULT_DIR = "./"

# Folder for your attachments/images
IMAGE_FOLDER = "Attachments"

# File extensions to consider
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp")
VIDEO_EXTENSIONS = (".mp4", ".mov", ".webm")

def convert_embeds(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for Obsidian-style embeds
    pattern = r'!\[\[(.*?)\]\]'

    def replacer(match):
        filename = match.group(1)
        ext = os.path.splitext(filename)[1].lower()
        file_url = f"{IMAGE_FOLDER}/{filename.replace(' ', '%20')}"
        name = os.path.splitext(filename)[0]

        if ext in IMAGE_EXTENSIONS:
            return f"![{name}]({file_url})"
        elif ext in VIDEO_EXTENSIONS:
            # Use HTML for video embed
            return f'<video src="{file_url}" controls></video>'
        else:
            # Default: just a link
            return f"[{name}]({file_url})"

    converted = re.sub(pattern, replacer, content)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(converted)
    print(f"Converted: {md_file}")

# Walk through all markdown files
for root, _, files in os.walk(VAULT_DIR):
    for file in files:
        if file.endswith(".md"):
            convert_embeds(os.path.join(root, file))

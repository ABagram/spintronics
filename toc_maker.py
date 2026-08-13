# create a table of contents in markdown format for a given markdown file by extracting headings and converting them into a list with links to the corresponding sections.

import re

def markdown_anchor(text):
    """
    Convert a Markdown heading into a GitHub-style anchor.
    """

    # Remove inline Markdown formatting
    text = re.sub(r'[`*_~]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)

    # Remove characters that are generally not included in anchors
    text = re.sub(r'[^\w\-]', '', text)

    # Remove repeated hyphens
    text = re.sub(r'-+', '-', text)

    # Remove hyphens at the beginning/end
    text = text.strip('-')

    return text


def generate_toc(filename):
    toc = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Match headings from # to ####
            match = re.match(r'^(#{1,3})\s+(.+?)\s*$', line)

            if not match:
                continue

            hashes = match.group(1)
            heading = match.group(2)

            # Heading level: # = 1, ## = 2, etc.
            level = len(hashes)

            # Create Markdown anchor
            anchor = markdown_anchor(heading)

            # Indent based on heading level
            indentation = "  " * (level - 1)

            toc.append(
                f"{indentation}- [{heading}](#{anchor})"
            )

    return "\n".join(toc)

filename = "Act_One.md"

toc = generate_toc(filename)

print(toc)
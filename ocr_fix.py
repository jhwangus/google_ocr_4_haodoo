import pyperclip

def search_replace_multiple(search_replace_pairs):
    """Search and replace multiple terms in the clipboard content.

    Args:
        search_replace_pairs (list of tuples): A list of tuples, where each tuple contains a search term and a replacement term.
    """

    # Get the current clipboard content
    clipboard_content = pyperclip.paste()

    # Iterate through each search-replace pair and perform the replacement
    for search_term, replace_term in search_replace_pairs:
        clipboard_content = clipboard_content.replace(search_term, replace_term)

    # Put the new content back to the clipboard
    pyperclip.copy(clipboard_content)

# Example usage
search_replace_pairs = [
    (" ", ""),
    ("...", "…"),
    ("・・・", "…"),
    ("・・・", "…"),
    (",", "，"),
    (";", "；"),
    (":", "："),
    ("?", "？"),
    ("!", "！"),
    ("(", "（"),
    (")", "）"),
    ("·", "・")
]

search_replace_multiple(search_replace_pairs)

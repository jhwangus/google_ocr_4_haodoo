import pyperclip, re

def replace_spaces_with_full_space(text):
    """Replaces spaces between alphanumeric characters with '　'.

    Args:
        text: The input string.

    Returns:
        The modified string with spaces replaced by '　'.
    """

    pattern = r"([a-zA-Z0-9])\s+([a-zA-Z0-9])"
    return re.sub(pattern, r"\1　\2", text)

def search_replace_multiple(search_replace_pairs):
    """Search and replace multiple terms in the clipboard content.

    Args:
        search_replace_pairs (list of tuples): A list of tuples, where each tuple contains a search term and a replacement term.
    """

    # Get the current clipboard content
    clipboard_content = pyperclip.paste()

    clipboard_content = replace_spaces_with_full_space(clipboard_content)

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
    ("・・・", "…"),
    ("——", "──"),
    (",", "，"),
    (";", "；"),
    (":", "："),
    ("?", "？"),
    ("!", "！"),
    ("(", "（"),
    (")", "）"),
    ("·", "・"),
    ("a", "ａ"),
    ("b", "ｂ"),
    ("c", "ｃ"),
    ("d", "ｄ"),
    ("e", "ｅ"),
    ("f", "ｆ"),
    ("g", "ｇ"),
    ("h", "ｈ"),
    ("i", "ｉ"),
    ("j", "ｊ"),
    ("k", "ｋ"),
    ("l", "ｌ"),
    ("m", "ｍ"),
    ("n", "ｎ"),
    ("o", "ｏ"),
    ("p", "ｐ"),
    ("q", "ｑ"),
    ("r", "ｒ"),
    ("s", "ｓ"),
    ("t", "ｔ"),
    ("u", "ｕ"),
    ("v", "ｖ"),
    ("w", "ｗ"),
    ("x", "ｘ"),
    ("y", "ｙ"),
    ("z", "ｚ"),
    ("A", "Ａ"),
    ("B", "Ｂ"),
    ("C", "Ｃ"),
    ("D", "Ｄ"),
    ("E", "Ｅ"),
    ("F", "Ｆ"),
    ("G", "Ｇ"),
    ("H", "Ｈ"),
    ("I", "Ｉ"),
    ("J", "Ｊ"),
    ("K", "Ｋ"),
    ("L", "Ｌ"),
    ("M", "Ｍ"),
    ("N", "Ｎ"),
    ("O", "Ｏ"),
    ("P", "Ｐ"),
    ("Q", "Ｑ"),
    ("R", "Ｒ"),
    ("S", "Ｓ"),
    ("T", "Ｔ"),
    ("U", "Ｕ"),
    ("V", "Ｖ"),
    ("W", "Ｗ"),
    ("X", "Ｘ"),
    ("Y", "Ｙ"),
    ("Z", "Ｚ"), 
#    ("0", "０"),
#    ("1", "１"),
#    ("2", "２"),
#    ("3", "３"),
#    ("4", "４"),
#    ("5", "５"),
#    ("6", "６"),
#    ("7", "７"),
#    ("8", "８"),
#    ("9", "９"),
 ]

search_replace_multiple(search_replace_pairs)

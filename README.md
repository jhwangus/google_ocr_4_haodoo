# ocr_4_haodoo
如何使用 Google Doc 批次 OCR 多份掃描檔；快速批次轉換英文標點符號成中文標點符號。

## 使用 Google Doc 批次 OCR

## 快速批次搜尋及替換標點符號
Google Doc 的 OCR 預設標點符號為英文標點符號，所以OCR產生的文檔內夾雜英文標點符號，而非我們想要的中文標點符號。例如，逗號、問號、驚嘆號、冒號、分號、左括號、右括號等等，都是以英文半形而非中文全型呈現（例如，逗號用英文","，而非中文"，" ）。

這裡是快速批次解決辦法。

搜索和替換剪貼板內容（快捷方式方法）
這個腳本允許您在剪貼板內容中搜索和替換多個術語。您可以通過創建桌面快捷方式來觸發腳本。

特點：

同時替換多個術語。
使用元組列表進行搜索和替換對。
將修改後的內容保留在剪貼板中。
要求：

Python 3（從 https://www.python.org/downloads/ 下載）
pyperclip 模組（使用 pip install pyperclip 安裝）
說明：

安裝 pyperclip： 在命令提示符或終端中運行 pip install pyperclip。

保存腳本： 將以下代碼另存為 Python 文件（例如，search_replace_multiple.py）。

Python
import pyperclip

def search_replace_multiple(search_replace_pairs):
  """
  在剪貼板內容中搜索和替換多個術語。

  Args:
      search_replace_pairs (元組列表): 元組列表，其中每個元組包含搜索術語和替換術語。
  """

  clipboard_content = pyperclip.paste()

  for search_term, replace_term in search_replace_pairs:
    clipboard_content = clipboard_content.replace(search_term, replace_term)

  pyperclip.copy(clipboard_content)

# 示例用法
search_replace_pairs = [
    ("old_word1", "new_word1"),
    ("old_word2", "new_word2")
]
search_replace_multiple(search_replace_pairs)
Use code with caution.

創建桌面快捷方式：

右鍵單擊桌面，選擇「新增」->「捷徑」。
在「位置」欄中輸入 Python 解釋器的完整路徑（例如，C:\Python310\python.exe）。
單擊「下一步」。
在「輸入項目的位置」欄中添加一個空格，然後添加 Python 腳本的路徑（例如，"C:\path\to\your\script.py"）。
例如，完整的目標欄可能如下所示：
C:\Python310\python.exe "C:\path\to\your\script.py"
單擊「下一步」並為快捷方式命名（例如，「搜索替換剪貼板」）。
單擊「完成」。
用法：

將文本複製到剪貼板： 複製要修改的文本，並確保它在剪貼板中。
雙擊快捷方式： 雙擊您在桌面上創建的快捷方式。
腳本將自動運行，在您的剪貼板內容中搜索指定的術語，並將它們替換為相應的替換項。然後，修改後的內容將被複製回剪貼板。

自定義搜索替換對：

在腳本中編輯 search_replace_pairs 列表以指定您所需的搜索和替換術語。每個元組代表一個單個替換：

Python
search_replace_pairs = [
    ("old_word1", "new_word1"),
    ("old_word2", "new_word2")
]
Use code with caution.

其他注意事項：

確保快捷方式目標欄中的 Python 解釋器路徑和腳本路徑正確。
您可以根據需要修改腳本以包含更多功能或自定義行為。
此腳本提供了一種方便的方法，可以使用桌面快捷方式在剪貼板中搜索和替換文本。

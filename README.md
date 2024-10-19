# ocr_4_haodoo
如何使用 Google Doc 批次 OCR 多份掃描檔；快速批次轉換英文標點符號成中文標點符號。

## 用 Google Docs 執行多張圖片 OCR
Google Doc 有一隱藏功能。當其第一次打開某個 PDF 檔案時，將會自動執行 OCR，唯一限制是檔案不能太大，約40MB以下沒有問題，再大一些的話，Google Doc 會不執行 OCR，而是將每頁圖像直接貼上。

本法利用此功能，先將多份掃描圖像檔製成 PDF 檔，再上載 Google Drive 後打開，進行批次 OCR。

### 安裝

	1. 安裝 ImageMagick
     從 https://imagemagick.org/script/download.php 下載並安裝 ImageMagick。

### 轉換圖像檔成 pdf 檔

	1. 打開一個命令列（command prompt）
	2. 將圖片轉換為 PDF
      convert image_000*.jpg image_001*.jpg image_002*.jpg image_003*.jpg image_004*.jpg book1.pdf
	3. 檢查 PDF 大小，確認小於40MB。如果 PDF 大小超過 40 MB，可能需要減少轉換的圖像檔案數量。

### 用 Google Docs 進行 OCR

	1. 將 book1.pdf 檔上傳至 Google Drive
	2. 在 Google Driver 的 book1.pdf 上按滑鼠右鍵，選擇 Open with Google Doc，將會自動轉換成 book1 的文字檔。
	3. 若未能轉換，應該是 book1.pdf 太大（超過40MB），請減少圖像檔數量。

### OCR 後處理

1. OCR後，會產生很大的文字，頁數可能有數千頁。這是 Google Docs 自動格式化的問題。
2. 此時 Google Docs 中對 book1 選擇整個文檔（CTRL-A）。
3. 用滑鼠點上面 MENU 的格式 -> 清除格式，即可恢復正常大小，進行編輯、校對。

## 快速批次搜尋及替換標點符號

Google Doc 的 OCR 預設標點符號為英文標點符號，所以OCR產生的文檔內夾雜英文標點符號，而非我們想要的中文標點符號。例如，逗號、問號、驚嘆號、冒號、分號、左括號、右括號等等，都是以英文半形而非中文全型呈現（例如，逗號用英文","，而非中文"，" ）。

下面提供一個 Python 程式讓你在剪貼板內容中搜索和替換多個標點符號。你可以通過創建桌面捷徑的方式來執行此程式。

### 特點

1. 同時替換多個標點符號。
2. 可客製化。
3. 將修改後的內容保留在剪貼板中。

### 安裝

	1. 安裝 Python 3（從 https://www.python.org/downloads/ 下載）
	2. 安裝pyperclip 模組
		 在命令提示符或終端中運行 pip install pyperclip。
	3. 將ocr_fix.py 存在電腦上，如：D:\py\ocr_fix.py。
	4. 創建桌面捷徑
		 a. 右鍵單擊桌面，選擇「新增」->「捷徑」。
		 b. 在「位置」欄中輸入 python D:\py\ocr_fix.py
		 c. 單擊「下一步」。
		 d. 為桌面捷徑命名（例如，「OCR_FIX」）。
		 e. 單擊「完成」。

### 用法

	1. 將文本複製到剪貼板，如 CTRAL-A，然後 CTRL-C。
	2. 雙擊桌面捷徑。
     a. 程式將自動運行，在您的剪貼板內容中搜索指定標點符號，並將它們替換為相應的符號。
		 b. 修改後的內容將被保留於剪貼板。
	3. 在編輯的檔案內適當位置，按 CTRL-V。

### 客製化

可修改 ocr_fix.py 內列表，增加搜尋取代符號。

```
# Example usage
search_replace_pairs = [
    (" ", ""),
    ("...", "…"),
    (",", "，"),
    (";", "；"),
    (":", "："),
    ("?", "？"),
    ("!", "！"),
    ("(", "（"),
    (")", "）"),
    ("·", "・")
]
```

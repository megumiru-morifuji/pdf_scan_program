import os
from PyPDF2 import PdfReader

# 対象フォルダ（PDFを入れたフォルダ）
TARGET_FOLDER = "pdf_folder"  # ←ここを自分のフォルダ名に

total_pages = 0
total_files = 0

for root, dirs, files in os.walk(TARGET_FOLDER):
    for file in files:
        if file.lower().endswith(".pdf"):
            path = os.path.join(root, file)
            try:
                reader = PdfReader(path)
                pages = len(reader.pages)

                print(f"{file}: {pages}ページ")

                total_pages += pages
                total_files += 1

            except Exception as e:
                print(f"エラー: {file} ({e})")

print("\n====================")
print(f"PDFファイル数: {total_files}")
print(f"合計ページ数: {total_pages}")
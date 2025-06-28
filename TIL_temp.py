import datetime
date = datetime.date.today()

str_date = date.strftime('%Y-%m-%d')
dir_name = date.strftime('%Y-%m/')

with open(f"{dir_name}{str_date}.md", "x", encoding='UTF-8') as f:
    f.writelines([f"# {str_date}\n\n",
                  "## 学んだこと\n\n",
                  "## メモ\n\n",
                  "## 所感\n\n",
                  "## 参考リンク\n"])
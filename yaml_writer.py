import os
import os.path
import yaml
from book import Book


def str_or_empty(str):
	if str is None:
		return ''
	else:
		return str

def format_book(book):
	return "%s;%s;%s;%s;%s\n" % (book.id, str_or_empty(book.name), str_or_empty(book.ISBN), book.rating, book.date)

# Write books content to csv file
class YamlWriter():
	def save(this, books, file_name):
			if not os.path.exists('LiveLibExport'):
				os.makedirs('LiveLibExport')

			for book in books:
				save_to_path = "LiveLibExport//"
				invalid = '<>:"/\|?*'

				fname = book.name
				for char in invalid:
					fname = fname.replace(char, '')
				if book.name != None:
					fname = os.path.join(save_to_path, fname + ".md")
				else:
					fname = os.path.join(save_to_path, book.id + ".md")
				with open(fname, 'w', encoding="utf-8") as f:
					data = yaml.dump(book, f, sort_keys=True, default_flow_style=False)

				with open(fname, "r", encoding="utf-8") as f:
					contents = f.readlines()

				contents.insert(0, "---\n")
				contents.append("---")

				with open(fname, "w", encoding="utf-8") as f:
					contents = "".join(contents)
					f.write(contents)

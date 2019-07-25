import sys, os
from util.Timer import Timer
from util.FileOpener import FileOpener
from model.StopWordModel import StopWordModel

RAW_WIKI_LINES = 4672758

def print_status(num_articles: int):
	percent = round(100 / RAW_WIKI_LINES * num_articles, 3)
	print(f"\r... Saved {percent}% {str(num_articles)} articles", end="")

def remove_stopwords(file_path: str):
	stop_words = StopWordModel().get_stop_words()
	output_file = FileOpener().get_new_file("wiki.en.filtered.txt", "a")
	with open(file_path, "r") as file:
		i = 0
		for line in file:
			split_line = line.split(" ")
			filtered_list = [word for word in split_line if word not in stop_words]
			filtered_line = " ".join(filtered_list)
			output_file.write(filtered_line)
			i = i + 1
			if (i % 10 == 0):
				print_status(i)
	print_status(i)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <wiki.en.raw.txt>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use raw text "{file_path}"')
		print("[+] Starting to remove stopwords")
		timer = Timer()
		remove_stopwords(file_path)
		print(f"\n[+] Finished: {timer.get_duration()}s")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()




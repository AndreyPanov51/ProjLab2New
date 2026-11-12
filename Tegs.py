import csv


def main():
    unique_tags = set()

    with open("books.csv", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            genres = row.get("Жанр книги", "")
            if genres != "":
                tags = genres.split("#")
                for tag in tags:
                    clean_tag = tag.strip()
                    if clean_tag != "":
                        unique_tags.add(clean_tag)

    for tag in sorted(unique_tags):
        print(tag)


if __name__ == "__main__":
    main()
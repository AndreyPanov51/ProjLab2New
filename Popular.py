import csv


def main():
    book_popularity = {}

    with open("books.csv", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            title = row.get("Название", "").strip()
            checkouts_str = row.get("Кол-во выдач", "0").strip()
            checkouts = int(checkouts_str)
            if title != "":
                book_popularity[title] = book_popularity.get(title, 0) + checkouts

    sorted_books = sorted(book_popularity.items(), key=lambda x: -x[1])
    top_20 = sorted_books[:20]

    for title, check in top_20:
        print("Книга", title, "Выдали:", check)


if __name__ == "__main__":
    main()
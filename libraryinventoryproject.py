class LibraryInventory:
    def __init__(self, filename="library_inventory.txt"):
        self.filename = filename
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.filename, 'r') as file:
                self.books = [line.strip().split(',') for line in file.readlines()]
        except FileNotFoundError:
            self.books = []

    def save_inventory(self):
        with open(self.filename, 'w') as file:
            for book in self.books:
                file.write(','.join(book) + '\n')

    def add_book(self, title, author, genre):
        book = f"{title},{author},{genre}"
        self.books.append(book.split(','))
        print(f"Buku '{title}' oleh {author} telah ditambahkan ke perpustakaan.")
        self.save_inventory()

    def view_inventory(self):
        if not self.books:
            print("Perpustakaan Kosong.")
        else:
            print("Daftar Buku dalam Perpustakaan:")
            for book in self.books:
                print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

    def search_book(self, book_title):
        found_books = [book for book in self.books if book_title.lower() in book[0].lower()]
        if found_books:
            print(f"Buku dengan judul '{book_title}' ditemukan dalam perpustakaan:")
            for book in found_books:
                print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
        else:
            print(f"Tidak ada buku dengan judul '{book_title}' dalam perpustakaan.")

    def remove_book(self, book_title):
        removed_books = [book for book in self.books if book_title.lower() not in book[0].lower()]
        if removed_books != self.books:
            print(f"Buku dengan judul '{book_title}' telah dihapus dari perpustakaan.")
            self.books = removed_books
            self.save_inventory()
        else:
            print(f"Tidak ada buku dengan judul '{book_title}' dalam perpustakaan.")

def main():
    library = LibraryInventory()

    while True:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == "1":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama penulis: ")
            genre = input("Masukkan genre buku: ")
            library.add_book(title, author, genre)
        elif choice == "2":
            library.view_inventory()
        elif choice == "3":
            search_title = input("Masukkan judul buku yang dicari: ")
            library.search_book(search_title)
        elif choice == "4":
            remove_title = input("Masukkan judul buku yang akan dihapus: ")
            library.remove_book(remove_title)
        elif choice == "5":
            print("Program dihentikan.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()

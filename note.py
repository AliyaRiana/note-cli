import os

FILE = "todo.txt"

def load_todo():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_todo(todo_list):
    with open(FILE, "w") as f:
        for item in todo_list:
            f.write(item + "\n")

def show(todo_list):
    if not todo_list:
        print("Daftar kosong.")
    for i, item in enumerate(todo_list, 1):
        print(f"{i}. {item}")

def add(todo_list, item):
    todo_list.append(item)
    save_todo(todo_list)
    print(f"'{item}' ditambahkan.")

def remove(todo_list, index):
    try:
        removed = todo_list.pop(index - 1)
        save_todo(todo_list)
        print(f"'{removed}' dihapus.")
    except IndexError:
        print("Nomor tidak valid.")

def main():
    todo_list = load_todo()
    while True:
        print("\nTo-Do List:")
        show(todo_list)
        cmd = cmd = input("\n[tambah/hapus/clear/keluar]: ").strip().lower()
        if cmd == "tambah":
            item = input("Apa yang ingin ditambahkan? ")
            add(todo_list, item)
        elif cmd == "hapus":
            try:
                num = int(input("Nomor yang ingin dihapus? "))
                remove(todo_list, num)
            except ValueError:
                print("Masukkan angka.")
        elif cmd == "clear":
             todo_list = []
             save_todo(todo_list)
             print("Semua tugas dihapus.")
        elif cmd == "keluar":
            break
        else:
            print("Perintah tidak dikenali.")

if __name__ == "__main__":
    main()

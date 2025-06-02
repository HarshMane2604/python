import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor ()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos(videos):
    cursor.execute("SELECT * FROM videos")
    for row in 
def add_video():
    pass

def update_vedio():
    pass

def delete_vedio():
    pass


def main():
    while True:
        print("\nWelcome to youtube manager app.")
        print("1. List all vedios")
        print("2. Add a youtube vedio")
        print("3. Update a youtube vedio details")
        print("4. Delete a youtube vedio")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == "3":
            vedio_id = input("Enter the vedio id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_vedio(vedio_id, name, time)

        elif choice == "4":
            vedio_id = input("Enter the vedio id: ")
            delete_vedio(vedio_id)

        elif choice == "5":
            break
        else:
            print("Invalid choice")
    conn.close()


if __name__ == "__main__":
    main()
import sqlite3
con=sqlite3.connect("youtube_videos.db")
cursor=con.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name VARCHAR(100) NOT NULL,
                   time VARCHAR(100) NOT NULL
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    # print(cursor.fetchall())
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\nYoutube Manager | choose an option")
        print("\n1. List all youtube video")
        print("\n2. Add a youtube video")
        print("\n3. Update a youtube video details")
        print("\n4. Delete a youtube video")
        print("\n5. Exit the app")
        choice=input("Enter you choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

    con.close()

if __name__ == "__main__":
    main()
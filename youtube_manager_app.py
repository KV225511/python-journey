import json


def load_data():
    try:
        with open("youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print("\n")
        print("*"*70)
        print(f"{index}. {video['name']}, Duration:{video['time']} ")
    print("\n")
    print("*"*70)

def add_video(videos):
    name=input("ENter video name:")
    time=input("Enter video time:")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=input("Enter the video number to update: ")
    if(1<=index<=len(videos)):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print('Invalid video selected')

def delete_video(videos):
    list_all_videos(videos)
    index=input("Enter the video number to delete: ")
    if(1<=index<=len(videos)):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Invalid video selected')
    

def main():
    videos=load_data()
    while True:
        print("\nYoutube Manager | choose an option")
        print("\n1. List all youtube video")
        print("\n2. Add a youtube video")
        print("\n3. Update a youtube video details")
        print("\n4. Delete a youtube video")
        print("\n5. Exit the app")
        choice=input("Enter you choice: ")
        match(choice):
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(video)
            case '3':
                update_video(video)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Please enter a correct option")
    
if __name__=="__main__":
    main()
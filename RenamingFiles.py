import os

path = r"R:\MOVIES\DAIMA"

episodes = os.listdir(path)

for episode in episodes:
    print(episode)

# print()
# i = 1
# for episode in episodes:
#     oldpath = os.path.join(path, episode)
#     newname = f"E0{i}.mkv"
#     newpath = os.path.join(path, newname)
#     os.rename(oldpath, newpath)
#     print(episode, "->", newname)
#     i += 1

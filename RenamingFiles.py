import os

path = r"R:/MOVIES/test"

episodes = os.listdir(path)

for episode in episodes:
    print("=" * 34)
    print(len(episode))
    print(episode.index("."))
    print(episode[episode.index("."):])

print()
# i = 1
# for episode in episodes:
#     oldpath = os.path.join(path, episode)
#     if i <= 9:
#         newname = f"E0{i}.mkv"
#     else:
#         newname = f"E{i}.mkv"
#     newpath = os.path.join(path, newname)
#     os.rename(oldpath, newpath)
#     print(episode, "->", newname)
#     i += 1

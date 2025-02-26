# MultiProcessing in Python

import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor


def download(url, name):
    print(f"Downloading IMG{name}......")
    response = requests.get(url)
    open(f"OS Example\\Tutorial4\\IMG{name}.jpg", "wb").write(response.content)
    print(f"Downloaded IMG{name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(15):
        # Takes 7 business days to complete
        # download(url, i)

        # Way faster
        mp = multiprocessing.Process(target=download, args=[url, i])
        mp.start()
        pros.append(mp)

    for pro in pros:
        pro.join()

    with ProcessPoolExecutor() as executor:
        l1 = [url for i in range(15)]
        l2 = [i for i in range(15)]
        results = executor.map(download, l1, l2)
        for result in results:
            print(result)

"""
1. Have a input loop that gets a URL from the user
2. Fetch the data at the URL and display it
"""
import urllib.request

cache = {}


def get_data(url):
    if url not in cache:
        print("Cache miss!")

        resp = urllib.request.urlopen(url)

        data = resp.read()

        resp.close()

        data = data.decode()  # turns bytes into string

        cache[url] = data

    return cache[url]


if __name__ == "__main__":
    while True:
        url = input("Enter a URL: ")
        print(get_data(url)[:100])

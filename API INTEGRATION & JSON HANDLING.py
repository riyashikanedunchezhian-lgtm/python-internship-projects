import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)

    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet")

    except requests.exceptions.Timeout:
        print("Timeout Error")

    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

    return None


def search_posts(posts, keyword):
    results = []

    for post in posts:
        if keyword.lower() in post["title"].lower() or keyword.lower() in post["body"].lower():
            results.append(post)

    return results


def display_posts(posts):
    if not posts:
        print("No matching posts found.")
        return

    print("\nMatching Posts\n")

    for post in posts:
        print("=" * 50)
        print("User ID :", post["userId"])
        print("Post ID :", post["id"])
        print("Title   :", post["title"])
        print("Body    :", post["body"])
        print("=" * 50)


def main():
    print("Fetching posts from API...\n")

    posts = fetch_posts()

    if posts:
        keyword = input("Enter keyword to search in posts: ")
        filtered_posts = search_posts(posts, keyword)
        display_posts(filtered_posts)


if __name__ == "__main__":
    main()
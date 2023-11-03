import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    api_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(api_url, params=parameters)

    if response.status_code != 200:
        raise RuntimeError(
            "An error occurred and status code was", response.status_code)
    if response.status_code == 403:
        raise RuntimeError(
            "An error occurred. HTTP status code was", response.status_code)
    else:
        response_json = response.json()["items"]
        return response_json


if __name__ == "__main__":

    languages = ["Python", "JavaScript", "Ruby"]
    results = repos_with_most_stars(languages=languages)

    query = create_query(languages)
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} with {stars} stars.")

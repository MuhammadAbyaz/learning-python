class GitHubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached."
        else:
            message = f"Status code was: {status_code}"
        super().__init__(message)


class GitHubRepo:

    def __init__(self, name, language, num_stars) -> None:
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self) -> str:
        return f"-> {self.name} is a {self.language} repo with stars {self.num_stars}."

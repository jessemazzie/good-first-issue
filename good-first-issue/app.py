import urllib.request
import json
import os
import logging
from flask import Flask, render_template

app = Flask(__name__)


def get_access_token():
    """Get the access token from the environment variable or from the .token file"""
    if os.environ.get("GITHUB_ACCESS_TOKEN"):
        return os.environ.get("GITHUB_ACCESS_TOKEN")
    with open("./.token") as f:
        return f.read()


def generate_language_list():
    """Generate a list of programming languages for the search filter"""
    # TODO: Implement this function
    raise NotImplementedError


def build_search_query(
    language: str = None, sort_by: str = "stars", order: str = "desc"
):
    """Build the search query for the GitHub API"""
    query = "good-first-issue+is:issue+is:open"
    if language:
        query = f"{query}+language:{language}"

    if sort_by:
        query = f"{query}&sort={sort_by}"

    if order:
        query = f"{query}&order={order}"

    return query


def search_github_repositories(access_token):
    """Search for repositories with good first issues"""
    github_search_query = build_search_query()
    github_api_version = "2022-11-28"
    url = f"https://api.github.com/search/repositories?q={github_search_query}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": f"application/vnd.github.{github_api_version}+json",
        "2022-11-28": github_api_version,
    }
    req = urllib.request.Request(url, headers=headers)
    response = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    logging.info(f"Total count: {response['total_count']}")
    logging.info(f"Response keys: {response.keys()}")
    # print(response["items"][0].keys())

    return response["items"]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("gfi.log", mode="a"), logging.StreamHandler()],
)

access_token = get_access_token()


@app.route("/")
def index():
    viable_repositories = search_github_repositories(access_token)

    for repo in viable_repositories:
        logging.info(f"Repo name: {repo['name']}")
        logging.info(f"Issue count: {repo['open_issues_count']}")
        logging.info(f"Repository url: {repo['html_url']}")

    return render_template("index.html", repositories=viable_repositories)


if __name__ == "__main__":
    logging.info("Starting the Flask app")
    app.run(debug=True, host="0.0.0.0")

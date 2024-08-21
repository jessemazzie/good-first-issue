import urllib.request
import json
import logging
from flask import Flask, render_template

app = Flask(__name__)

def get_access_token():
    with open("../.token") as f:
        return f.read()


def search_github_repositories(access_token):
    github_search_query = "good-first-issue+is:issue+language:python"
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
    print(response["items"][0].keys())

    return response["items"]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("gfi.log", mode="a"), logging.StreamHandler()],
)

access_token = get_access_token()

print(access_token)


viable_repositories = search_github_repositories(access_token)

@app.route("/")
def hello_world():
    return render_template("index.html", repositories=viable_repositories)

# for repo in viable_repositories:
#     logging.info(f"Repo name: {repo['name']}")
#     logging.info(f"Issue count: {repo['open_issues_count']}")
#     logging.info(f"Repository url: {repo['html_url']}")


"""
Format and send a message indicating the git commits listed in hashes are not verified.

Each sender method should have the same signature as `send_to_console`.
"""

from typing import List


def send_to_console(*, author: str, repo: str, commits: List[dict]):
    """
    Print a message to std::out describing the unverified commits.

    `send_to_console` is the demonstration send method, the parameters have the same
    meaning in all other send methods.

    `author` the name of the GitHub user who authored the `commits`.

    `repo` is the name of the GitHub repo these commits can be found in, in
    `{owner}/{name}` format.

    `commits` is the list of commits that were unverified.
    """
    msg = (
        f"GitHub User {author} pushed the following {len(commits)} unverified "
        f"commits to {repo}:\n\n"
    )

    for commit in commits:
        url = commit["url"]
        msg += f"\t* {url}\n"

    print(msg)

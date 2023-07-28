from scrapper.urls import *
def get_dept_url(branch: str = "cse_csit"):
    """SENDS DEPARTMENT'S HOME PAGE URL """
    if branch is None:
        return None

    branch = branch.strip()

    try:
        url = dept_links[branch]
    except KeyError:
        print("Department not found.")
        return None

    return f"{branch}: {url}"


if __name__ == '__main__':
    url = get_dept_url("mechanical")
    print(url)

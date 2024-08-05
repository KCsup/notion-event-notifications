import requests as req


def query_database(
    notion_token: str,
    database_id: str,
    filter: dict
):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    params = {
        "filter": filter
    }

    return make_notion_request(notion_token, url, "post", params)


def make_notion_request(
    notion_token: str,
    url: str,
    method: str,
    params: dict,
    isJSON: bool = True
):
    response, status_code = None, 0
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    match method.lower():
        case "get":
            response = req.get(url, params=params, headers=headers)
        case "post":
            response = req.post(url, params=params, headers=headers)
        case "patch":
            response = req.patch(url, params=params, headers=headers)
        case _:
            raise InvalidHTTPMethod(f"HTTP method '{method}' is invalid.")

    status_code = response.status_code
    
    if isJSON: response = response.json()

    return response, status_code


class InvalidHTTPMethod(Exception):
    pass

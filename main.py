import requests as req
import notion
import json


notion_token = json.load(open("token.json"))["notion"]

def main():
    filter = {
        "and" : [
            {
                "property": "Status",
                "status": {
                    "does_not_equal": "Done"
                }
            },
            {
                "property": "Tags",
                "multi_select": {
                    "contains": "Event"
                }
            }
        ]
    }
    db, status = notion.query_database(
                               notion_token,
                               "c60a72f32a8f4445a412e11d8389285b",
                               filter,
                           )
    print(db)
    pass


if __name__ == "__main__":
    main()

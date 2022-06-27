import os
import copy
import sys
import json
import requests

from constants import *


def create_payloads(languages=None):
    """
    Create payloads for all languages and all releases.

    Returns:
        List: List of payloads, language and release.
    """
    payloads = []
    if not languages:
        languages = LANGUAGES
    for language in languages:
        for release in RELEASES:
            payload = copy.deepcopy(
                TRANSLATIONS_PAYLOAD if language != "en_US" else STRING_PAYLOAD
            )
            payload["data"]["relationships"]["resource"]["data"][
                "id"
            ] = f"o:{ORGANIZATION}:p:{PROJECT}:r:{release}"

            if language != "en_US":
                payload["data"]["relationships"]["language"]["data"][
                    "id"
                ] = f"l:{language}"
            payloads.append(
                {
                    "payload": json.dumps(payload),
                    "language": language,
                    "release": release,
                    "url": TRANSLATION_URL if language != "en_US" else STRING_URL,
                }
            )

    return payloads


def create_request(payload, url):

    response = requests.post(url=url, headers=HEADERS, data=payload)
    if response.status_code != 202:
        print(f"Error: {response.status_code}")
        sys.exit(1)
    return response.json()["data"]["id"]


def collect_task_ids(languages=None):
    payloads = create_payloads(languages)

    for payload in payloads:
        task_id = create_request(payload.get("payload"), payload.get("url"))
        payload.update({"task_id": task_id})

    return payloads


def check_for_task_id(url):
    flag = True
    while flag:
        response = requests.get(
            url=url,
            headers=HEADERS,
        )
        if response.headers["Content-Type"] == "application/octet-stream":
            flag = False
    return response.content


def main(languages):
    payloads = collect_task_ids(languages)
    for payload in payloads:
        content = check_for_task_id(f'{payload.get("url")}/{payload.get("task_id")}')
        file_name = f"{payload.get('release')}.po"
        save_to_path(payload.get("language"), file_name, content)


def save_to_path(language, file_name, content):
    """
    Save content to path.

        Args:
            language (str): Language.
            file_name (str): File name.
            content (str): Content.
    """
    path = os.path.join(os.getcwd(), "translations", language, "LC_MESSAGES")
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = "djangojs.po" if "-js" in file_name else "django.po"
    with open(f"{path}/{file_name}", "wb") as f:
        print(f"Saving {path} - {file_name}")
        f.write(content)


def check_for_input():
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments provided")
        sys.exit(1)
    elif len(args) == 1 and args[0] == "--help":
        print("Usage:")
        print("  python transifex.py <language>")
        print("  python transifex.py <language> <language> <language> ...")
        print("  python transifex.py --help")
        sys.exit(0)
    elif len(args) == 1 and args[0] == "all":
        return LANGUAGES 
    else:
        for language in args:
            if language not in LANGUAGES:
                print(
                    f"Language {language} is not supported. Supported languages: {' ,'.join(LANGUAGES)}"
                )
                args.remove(language)
        return args

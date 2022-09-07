import os
from dotenv import load_dotenv

load_dotenv("api_key.env")

TOKEN = os.getenv("TRANSIFEX_API_KEY")

BASE_URL = "https://rest.api.transifex.com/"
STRING_URL = BASE_URL + "resource_strings_async_downloads"
TRANSLATION_URL = BASE_URL + "resource_translations_async_downloads"

ORGANIZATION = "open-edx"
PROJECT = "open-edx-releases"
RELEASES = ["release-nutmeg", "release-nutmeg-js"]
LANGUAGES = [
    "ar",
    "de_DE",
    "en_US",
    "es_419",
    "fa_IR",
    "fr",
    "ja_JP",
    "ru",
    "tr_TR",
    "uk",
]
STATUS = ["failed", "pending", "processing"]

TRANSLATIONS_PAYLOAD = {
    "data": {
        "attributes": {
            "content_encoding": "text",
            "file_type": "default",
            "mode": "translator",
        },
        "relationships": {
            "language": {"data": {"id": "LANGUAGE", "type": "languages"}},
            "resource": {
                "data": {
                    "id": "o:ORGANIZATION:p:PROJECT:r:RELEASE",
                    "type": "resources",
                }
            },
        },
        "type": "resource_translations_async_downloads",
    }
}


STRING_PAYLOAD = {
    "data": {
        "attributes": {
            "callback_url": None,
            "content_encoding": "text",
            "file_type": "default",
            "pseudo": False,
            "pseudo_length_increase": 1,
        },
        "relationships": {
            "resource": {
                "data": {
                    "id": "o:organization_slug:p:project_slug:r:resource_slug",
                    "type": "resources",
                }
            }
        },
        "type": "resource_strings_async_downloads",
    }
}

HEADERS = {
    "Content-Type": "application/vnd.api+json",
    "Authorization": f"Bearer {TOKEN}",
}

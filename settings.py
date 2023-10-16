from functools import lru_cache
from typing import List

from pydantic import BaseSettings

_DEFAULT_SITES_HOSTS = [
    "https://gist.githubusercontent.com/V3u3/df11c014b70f0ab53985f833f2b1dfcb/raw/1f96d7efee2eea3250be04703ada9fa525fc288a/uk.json"
]
_DEFAULT_PROXIES_HOSTS = [
    "https://raw.githubusercontent.com/opengs/uashieldtargets/v2/proxy.json"
]

_DEFAULT_TARGETS = [
#     There ypu can put your own targets
]


class Settings(BaseSettings):
    VERSION: int = 20
    MAX_THREADS: int = 500
    SITES_HOSTS: List[str] = _DEFAULT_SITES_HOSTS
    PROXIES_HOSTS: List[str] = _DEFAULT_PROXIES_HOSTS
    DEFAULT_TARGETS: List[str] = _DEFAULT_TARGETS
    MAX_REQUESTS_TO_SITE: int = 500
    TARGET_UPDATE_RATE: int = 120
    READ_TIMEOUT: int = 10
    BROWSER: dict = {"browser": "firefox", "platform": "android", "mobile": True}
    HEADERS_TEMPLATE: dict = {
        "Content-Type": "application/json",
        "cf-visitor": "https",
        "User-Agent": None,
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru",
        "x-forwarded-proto": "https",
        "Accept-Encoding": "gzip, deflate, br",
    }


@lru_cache()
def get_settings():
    return Settings()

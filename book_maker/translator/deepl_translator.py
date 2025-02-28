import json
import time
import deepl
import requests
import re

from book_maker.utils import LANGUAGES, TO_LANGUAGE_CODE

from .base_translator import Base
from rich import print


class DeepL(Base):
    """
    DeepL translator
    """

    def __init__(self, key, language, **kwargs) -> None:
        super().__init__(key, language)
        l = None
        l = language if language in LANGUAGES else TO_LANGUAGE_CODE.get(language)
        if l not in [
            "bg",
            "zh",
            "zh-hant",
            "zh-hans",
            "cs",
            "da",
            "nl",
            "en-US",
            "en-GB",
            "et",
            "fi",
            "fr",
            "de",
            "el",
            "hu",
            "id",
            "it",
            "ja",
            "lv",
            "lt",
            "pl",
            "pt-PT",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "es",
            "sv",
            "tr",
            "uk",
            "ko",
            "nb",
        ]:
            raise Exception(f"DeepL do not support {l}")
        self.language = l

    def rotate_key(self):
        pass

    def translate(self, text):
        self.rotate_key()
        translator = deepl.Translator(f"{next(self.keys)}")
        print(text)
        try:
            result = translator.translate_text(text, target_lang=self.language)
        except Exception as e:
            print(e)
            time.sleep(30)
            result = translator.translate_text(text, target_lang=self.language)
        t_text = result.text
        print("[bold green]" + re.sub("\n{3,}", "\n\n", t_text) + "[/bold green]")
        return t_text

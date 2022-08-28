import json
from ipapy import UNICODE_TO_IPA
from wiktionary_rus.wiktionary import find_item_from_wiki, wikiout


def test_find_item_from_wiki():
    assert "xərɐˈʂo" == find_item_from_wiki("хорошо'")[0].sounds


def test_wikiout():
    with open("tests/test_wikiout.json", "r", encoding="UTF-8") as f:
        saved_str = json.load(f)
        generated_str = str(wikiout("клю'ч"))
    assert saved_str == generated_str


def test_equality_of_id_in_wiki_and_ipapy():
    assert find_item_from_wiki("а'кр")[0].ipa[0] == UNICODE_TO_IPA["a"]

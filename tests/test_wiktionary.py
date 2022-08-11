import pytest
import json
from wiktionary_rus.wiktionary import find_item_from_wiki, wikiout

def test_find_item_from_wiki():
    assert 'xərɐˈʂo' == find_item_from_wiki("хорошо")[0].sounds
    
def test_wikiout():
    with open("tests/test_wikiout.json", "r") as f:
        saved_str = json.load(f)
        generated_str = str(wikiout("ключ")) 
    assert saved_str == generated_str
    
from wiktionary_rus.ipa_processing import IpaProcessing
import json
import pytest

def test_get_unique_ipa():
    with open("tests/test_get_unique_ipa.json", "r") as f:
        list_unique_unicodes = json.load(f)
    assert list_unique_unicodes == str(IpaProcessing.get_unique_ipa())
    
def test_get_sign2number():
    with open("tests/test_get_sign2number.json", "r") as f:
        sign2number = json.load(f)
    assert sign2number == str(IpaProcessing.get_sign2number())
    

def test_get_number2sign():
    with open("tests/test_get_number2sign.json", "r") as f:
        number2sign = json.load(f)
    assert number2sign == str(IpaProcessing.get_number2sign())

    
from wiktionary_rus.wiktionary import *
from wiktionary_rus.npipa_processing import *
from ipapy import UNICODE_TO_IPA


def test_ipa_string_to_numbers():
    ipa_string = find_item_from_wiki("а'кр")[0].ipa
    assert (all(np.array([1,18,39], dtype = "float32")) 
            == all(NpIpaProcessing.ipa_string_to_numbers(ipa_string)))
    

def test_uni_string_to_int():
    ipa_string = find_item_from_wiki("а'кр")[0].ipa
    assert [1, 18, 39] == NpIpaProcessing.uni_string_to_int(ipa_string)
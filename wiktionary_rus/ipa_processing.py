from ipapy import UNICODE_TO_IPA
from memoization import cached
from wiktionary_rus.wiktionary import wiki_instances


class IpaProcessing:

    @classmethod
    @cached
    def get_unique_ipa(cls):
        all_signs = set()
        for item in wiki_instances:
            if item.ipa:
                value = item.ipa
                for ch in value:
                    all_signs.add(ch)
        list_unique_ipas = [ipa_ch for ipa_ch in list(all_signs)]
        list_unique_unicodes = [str(ip) for ip in list_unique_ipas]
        list_unique_unicodes.sort()
        return list_unique_unicodes

    @classmethod
    def get_sign2number(cls):
        list_unique_unicodes = cls.get_unique_ipa()
        sign2number = dict(
            (UNICODE_TO_IPA[l], i)
            for i, l in enumerate(list_unique_unicodes, start=1))
        return sign2number

    @classmethod
    def get_number2sign(cls):
        list_unique_unicodes = cls.get_unique_ipa()
        number2sign = dict(
            (i, UNICODE_TO_IPA[l])
            for i, l in enumerate(list_unique_unicodes, start=1))
        return number2sign

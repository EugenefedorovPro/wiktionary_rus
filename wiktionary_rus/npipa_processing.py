import numpy as np
from wiktionary_rus.ipa_processing import IpaProcessing


class NpIpaProcessing:
    @classmethod
    def ipa_string_to_numbers(cls, ipa_string):
        ipa_as_numbers = []
        sign2number = IpaProcessing.get_sign2number()
        for ch in ipa_string:
            n = sign2number[ch]
            ipa_as_numbers.append(n)
        ipa_as_numbers = np.array(ipa_as_numbers, dtype="float32")
        return ipa_as_numbers

    @classmethod
    def uni_string_to_int(cls, ipa_string):
        ipa_as_int = []
        sign2number = IpaProcessing.get_sign2number()
        for ch in ipa_string:
            n = sign2number[ch]
            ipa_as_int.append(n)
        return ipa_as_int

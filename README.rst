##############################
wiktionary_rus
##############################

Python package with Russian wiktionary preprocessed for neural networks

* Version 0.0.1
* Date: 2022, August, 11
* Developer: Eugene Proskulikov
* License: MIT
* Contact: `LinkedIn <https://www.linkedin.com/in/eugene-proskulikov-168050a4/>`_.
* Home: https://github.com/EugenefedorovPro/wiktionary_rus

``wiktionary_rus`` includes:

*  database *wiki_parsed.pkl* of 422821 items, which goes back to original `russian wiktionary <https://kaikki.org/dictionary/Russian/index.html>`_
*  attributes wrapped in Dictionary Class to operate with database: word, lowcase, accent, stem, part of speech, meanings, unicode transcription according to `International Phonetic Alphabet <https://en.wikipedia.org/wiki/Help:IPA/Russian>`_, digital representations of a word for rhyming
*  stand-alone functions to get unique ipa signs; generating dicts: number_to_ipa, ipa_to_number; to convert IPA string to np.array and to list of integers

-------------
Install
-------------    

::

    $ pip install git+https://github.com/EugenefedorovPro/wiktionary_rus.git

 
The database embraces instances and the Dictionary class, which they belong to.
I serialized it with `dill` module, which means that one can unpickle everything one needs 
in any environment without previous uploading of the Dictionary Class, as standard
`pickle` module demands.

-------------------------
Dependencies 
-------------------------

``wiktionary_rus`` depends on `a special branch <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of my fork of 
`ipapy <https://github.com/pettarin/ipapy>`_ module. On installation
the branch is cloned from GitHub to the defined virtual environment. 
``ipapy`` is a Python module to work with International Phonetic Alphabet (IPA) strings

*requirements.txt* embraces a full-fledged list of all other dependencies, including 
those demanded for comfortable work in Jupyter within Visual Studio Code.


------------
Quick start
------------

::  

    from wiktionary_rus.wiktionary import wiki_instances, find_item_from_wiki, wikiout

This import will upload database. 
To lookup all data available on the word::
    
        wikiout("пешко'м")

Note, the input word has to be stressed, with the accent after the stressed vowel  

Output is a list of dicts::

> [{'word': 'пешком', 'word_lowcase': 'пешком', 'stem': None, 'pos': 'adv',
> 'grammeme': None, 'meanings': [['on foot, afoot']], 
> 'accent': "пешко'м", 'sounds': > 'pʲɪʂˈkom', 'status': True, 
> 'ipa': consonant plosive velar voiceless back close-mid rounded vowel bilabial consonant nasal voiced, 
> 'npipa': array([18., 34., 26.], dtype=float32), > 'intipa': [18, 34, 26]}]


To find all items on the word available in the database::

     find_item_from_wiki("клю'ч")

Output will provide a list of objects, which have *word* attribute equal to
an input, in this case *ключ*::

> [<__main__.Dictionary object at 0x000002288EFCFC70>, <__main__.Dictionary object at 0x000002288EFCFD90>]

-------------------
General attributes
-------------------


Each object has 12 attributes. Nine of them are of generale usage, the other three are preprocessed for my other project::
    
    find_item_from_wiki("клю'ч")[0].word # ключ, original form of word
    find_item_from_wiki("клю'ч")[0].word_lowcase #ключ, the same form with low case
    find_item_from_wiki("клю'ч")[0].stem # "клю'ч" stem of the word with an accent
    find_item_from_wiki("клю'ч")[0].pos # noun, part of speech
    find_item_from_wiki("клю'ч")[0].grammeme # ['accusative', 'nominative', 'singular'], basic grammatical forms
    find_item_from_wiki("ключ")[0].meanings # [['key'], ['wrench, spanner, screw wrench'], ['clue, key'], ['clef, key'], ['radical (in Chinese characters)']], meanings of the word
    find_item_from_wiki("клю'ч")[0].accent # "клю'ч", the word with an accent
    find_item_from_wiki("клю'ч")[0].sounds # 'klʲʉt͡ɕ', the unicode transcription of the word in IPA
    find_item_from_wiki("клю'ч")[0].status # True, boolean, may be False or True

395692 of 422821 items have True status, and were used in my other projects for 
training neural networks. The words standing behind them satisfy the following conditions:

* consist of simple alphabetic signs: ``re.compile("[^а-я|А-Я|ё|Ё|'|-]")``
* belong to most frequent parts of speech: "noun", "verb", "adj", "name", "adv", "num", "pron", "intj", "prep", "conj", "particle", "det", "ambiposition"
* some other conditions of minor importance

-------------------
Special attributes
-------------------
    
The next three attributes (.ipa, .npipa, .intipa) are specially designed for my project `rhyme_rus <https://github.com/EugenefedorovPro/rhyme_rus>`_. It is a python
library to find rhymes to a russian word. While rhyming only part of a word matters: the stressed vowel, all sounds after it, and the previous consonant if available.
These presuppositions made me chop the word accordingly::

    find_item_from_wiki("клю'ч")[0].ipa # alveolar consonant lateral-approximant palatalized // voiced central close rounded vowel // alveolo-palatal consonant sibilant-affricate voiceless  

That's a transcription of the word in ipapy objects representing International 
Phonetic Alphabet. `ipapy <https://github.com/pettarin/ipapy>`_ 
is a python library to work with IPA. `My fork <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of it is used in the project. I represent a word's
transcription as IPA, in accordance with insight that these are sounds we rhyme, not characters::

    find_item_from_wiki("клю'ч")[0].npipa # array([22., 82., 54.], dtype=float32) 

Here we have a part of a word, demanded by rhyme algorithm, which is represented as float32 numpy array::

    find_item_from_wiki("клю'ч")[0].intipa # [22, 82, 54]

Here goes the chopped word presented as a list of integers.

------------------
All items of wiki
------------------
::

    from wiktionary_rus.wiktionary import wiki_instances
    len(wiki_instances)

::

> 422821


``wiki_instances`` contains a list of all instances of the Dictionary class.
If you want to get access to class itself::

    from wiktionary_rus.dictionary import Dictionary



-----------------
Special functions
-----------------

::
 
    from wiktionary_rus.ipa_processing import IpaProcessing
    
    IpaProcessing.get_unique_ipa() 

::

> ['a', 'b', 'bʲ', 'bʲː', 'bː', 'd', 'dʲ', 'dʲː', 'dː', 'd͡z', 'd͡zʲ', 'e', 'f',
>  'fʲ', 'i', 'j', 'jː', 'k', 'kʲ', 'kʲː', 'kː', 'lʲ', 'lʲː', 'lˠ', 'lˠː', 'm',
>  'mʲ', 'mʲː', 'mː', 'n', 'nʲ', 'nʲː', 'nː', 'o', 'p', 'pʲ', 'pʲː', 'pː', 'r','rʲ',
> 'rʲː', 'rː', 's', 'sʲ', 'sʲː', 'sː', 't', 'tʲ', 'tʲː', 'tː', 't͡s', 't͡sʲ',
> 't͡sː', 't͡ɕ', 't͡ɕː', 'u', 'v', 'vʲ', 'vʲː', 'vː', 'x', 'xʲ', 'z', 'zʲ', 'zʲː',
> 'zː', 'æ', 'ɐ', 'ɕ', 'ɕː', 'ə', 'ɛ', 'ɡ', 'ɡʲ', 'ɡː', 'ɨ', 'ɪ', 'ɵ', 'ʂ', 'ʂː',
> 'ʈ͡ʂ', 'ʉ', 'ʊ', 'ʐ', 'ʐː']


produces a list of all 85 unique ipa signs in wiki_instances

::

    from wiktionary_rus.ipa_processing import IpaProcessing
    
    IpaProcessing.get_number2sign()

::

> {1: front open unrounded vowel, 
> 2: bilabial consonant plosive voiced, 
> 3: bilabial consonant palatalized plosive voiced, 
> 4: bilabial consonant palatalized plosive voiced... }

produces a dict: key - number starting from 1 to 85, value - ipa object


::

    from wiktionary_rus.ipa_processing import IpaProcessing
    
    IpaProcessing.get_sign2number()


::

> {front open unrounded vowel: 1,
> bilabial consonant plosive voiced: 2,
> bilabial consonant palatalized plosive voiced: 3,
> bilabial consonant palatalized plosive voiced: 4... }

produces a reversed dict: key - ipa object, value - number starting from 1 to 85

::

    from wiktionary_rus.npipa_processing import NpIpaProcessing
    from wiktionary_rus.wiktionary import find_item_from_wiki

    ipa_string = find_item_from_wiki("до'м")[0].ipa
    NpIpaProcessing.ipa_string_to_numbers(ipa_string)

::

> array([ 6., 34., 26.], dtype=float32)

returns np array of float32 type representation of an ipa string

::

    from wiktionary_rus.npipa_processing import NpIpaProcessing
    from wiktionary_rus.wiktionary import find_item_from_wiki

    ipa_string = find_item_from_wiki("до'м")[0].ipa
    NpIpaProcessing.uni_string_to_int(ipa_string)

::

> [6, 34, 26]

returns a list of integers representing ipa string

---------------
Raw Data
---------------
All data for ``wiktionary_rus`` is stored in `source <https://github.com/EugenefedorovPro/rhyme_rus/tree/main/rhyme_rus/data>`_ directory

*kaikki.org-dictionary-Russian_2022_01_01.json* is the original `russian wiktionary <https://kaikki.org/dictionary/Russian/index.html>`_

*kaikki_parsing_to_Class.ipynb* is a Jupyter notebook with code processing raw data to structured *wiktionary_rus*. You can reproduce the whole process of parsing, changing the code where you need

*grammemes_statistics.xlsx* is a file, which *kaikki_parsing_to_Class.ipynb* demands for correct processing of *grammeme* attribute. The latter should be placed in the same directory as the former one

 

import dill 
from pathlib import Path
from memoization import cached
from ipapy import UNICODE_TO_IPA
from ipapy.ipastring import IPAString



# loading wiki_parsed
@cached
def upload_wiki_parsed(path):
    with open(path_wiki_parsed, "rb") as f:
        wiki_parsed_instances = dill.load(f)
        print("Parsed wiktionary uploaded successfully")
        return wiki_parsed_instances



# the critical issue is that UNICODE_TO_IPA dict and ipa transcription in wiki_parsed
# belong to different classed and having the same name, refer to different objects
# with different ids.
# ite may invoke many issues while working with ipapy.
# the following two functions solve the problem 
# by rewriting .ipa attribute in all instances of Dictionary class
 
   
def create_dict_name_ipa(UNICODE_TO_IPA):
    dict_name_ipa = {ip.name:ip for ip in UNICODE_TO_IPA.values()}
    return dict_name_ipa



def equal_ipa_in_wiki_and_ipapy(dict_name_ipa):
    for item in wiki_instances:
        if item.ipa:
            list_new_ip = []
            for ip in item.ipa:
                new_ip = dict_name_ipa[ip.name]
                list_new_ip.append(new_ip)
            item.ipa = IPAString(ipa_chars=list_new_ip)


# uploading wiki_parsed instances
path_wiki_parsed = Path(__file__).parent / "wiki_parsed.pkl"
wiki_instances = upload_wiki_parsed(path_wiki_parsed)


# rewriting .ipa attribute with UNICODE_TO_IPA
# corresponding objects

dict_name_ipa = create_dict_name_ipa(UNICODE_TO_IPA)
equal_ipa_in_wiki_and_ipapy(dict_name_ipa)



# main functions for end-users
    
def find_item_from_wiki(word_with_accent):
    wiki_instances = upload_wiki_parsed(path_wiki_parsed)
    list_items = [item for item in wiki_instances if item.accent == word_with_accent]
    return list_items


def wikiout(word_with_accent):
    list_items = find_item_from_wiki(word_with_accent)
    list_vars = []
    for item in list_items:
        list_vars.append(vars(item))
    return list_vars
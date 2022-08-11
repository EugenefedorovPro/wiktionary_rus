import dill 
from pathlib import Path 
import ipapy
from memoization import cached

# loading wiki_parsed
@cached
def upload_wiki_parsed(path):
    with open(path_wiki_parsed, "rb") as f:
        wiki_parsed_instances = dill.load(f)
        print("Parsed wiktionary uploaded successfully")
        return wiki_parsed_instances

path_wiki_parsed = Path(__file__).parent / "wiki_parsed.pkl"
wiki_instances = upload_wiki_parsed(path_wiki_parsed)
    
def find_item_from_wiki(word):
    wiki_instances = upload_wiki_parsed(path_wiki_parsed)
    list_items = [item for item in wiki_instances if item.word == word]
    return list_items

def wikiout(word):
    list_items = find_item_from_wiki(word)
    list_vars = []
    for item in list_items:
        list_vars.append(vars(item))
    return list_vars
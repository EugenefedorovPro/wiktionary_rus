from pathlib import Path
import dill


def test_upload_wiki_parsed():
    path_wiki_parsed = Path(__file__).parent.parent / "wiktionary_rus/wiki_parsed.pkl"
    with open(path_wiki_parsed, "rb") as f:
        wiki_parsed_instances = dill.load(f)
    assert 422821 == len(wiki_parsed_instances)
    assert [48, 12, 48] == wiki_parsed_instances[100].intipa

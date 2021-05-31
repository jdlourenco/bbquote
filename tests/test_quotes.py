from bbquote.quotes import get_quote

def test_get_quote():
    v = get_quote()
    assert type(v) == dict
    
    for k in ["role", "quote", "show"]:
        assert k in v.keys()
    
    assert type(v["role"]) == str
    assert len(v["role"]) > 0
    
    assert type(v["quote"]) == str
    assert len(v["quote"]) > 0
    
    assert type(v["show"]) == str
    assert len(v["show"]) > 0

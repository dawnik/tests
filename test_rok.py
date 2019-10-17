import czy_rok_przystepny

def test_czyPrzystepny_2000():
    data = czy_rok_przystepny.czyPrzestepny(2000)
    assert data == True

def test_czyPrzystepny_2004():
    data = czy_rok_przystepny.czyPrzestepny(2004)
    assert data == True

def test_czyPrzystepny_2028():
    data = czy_rok_przystepny.czyPrzestepny(2028)
    assert data == True

def test_czyPrzystepny_2001():
    data = czy_rok_przystepny.czyPrzestepny(2001)
    assert data == False

def test_czyPrzystepny_1997():
    data = czy_rok_przystepny.czyPrzestepny(1997)
    assert data == False

def test_czyPrzystepny_2007():
    data = czy_rok_przystepny.czyPrzestepny(2007)
    assert data == False
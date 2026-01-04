from code import verifier_reponse, score_final, table_valide

def test_verifier_reponse():
    
    # Réponses correctes
    assert verifier_reponse(5, 3, 15) == True
    assert verifier_reponse(7, 8, 56) == True
    assert verifier_reponse(10, 10, 100) == True
    assert verifier_reponse(2, 5, 10) == True
    
    # Réponses incorrectes
    assert verifier_reponse(5, 3, 10) == False
    assert verifier_reponse(7, 8, 50) == False
    assert verifier_reponse(3, 4, 0) == False

def test_score_final():
   
    # Score parfait (10/10)
    resultat = score_final(10, 5)
    assert "Félicitations" in resultat
    assert "parfaitement" in resultat
    
    # Bon score (8-9/10)
    resultat = score_final(9, 7)
    assert "pas loin" in resultat
    
    resultat = score_final(8, 3)
    assert "pas loin" in resultat
    
    # Score faible (0-7/10)
    resultat = score_final(7, 4)
    assert "travailler" in resultat
    
    resultat = score_final(0, 2)
    assert "travailler" in resultat

def test_table_valide():
    
    # Tables valides (1-10)
    assert table_valide(1) == True
    assert table_valide(5) == True
    assert table_valide(10) == True
    assert table_valide(7) == True
    
    # Tables invalides
    assert table_valide(0) == False
    assert table_valide(11) == False
    assert table_valide(15) == False
    assert table_valide(-5) == False
    assert table_valide(-1) == False
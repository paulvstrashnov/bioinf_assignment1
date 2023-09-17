import src.nw as align

def test_nw_1():
    """Identical sequences, match=5, mismatch=-4, gap=-10
    """
    seq1 = 'ACGT'
    seq2 = 'ACGT'
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(seq1, 
                                                 seq2, 
                                                 score_fun=lambda x, y: 5 if x == y else -4, 
                                                 gap_penalty=-10)
    assert score == 20
    assert aligned_seq1 == 'ACGT'
    assert aligned_seq2 == 'ACGT'

def test_nw_2():
    pass
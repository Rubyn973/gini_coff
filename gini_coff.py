def ginicoff(poor: float, midleclass: float, rich: float, poor_income: float, midleclass_income: float, rich_income: float) :
    S1 = (poor * poor_income) / 2
    S1 = round(S1, 3)
    S2 = ((poor_income + poor_income + midleclass_income)/2) * midleclass
    S2 = round(S2, 3)
    S3 = ((1 + poor_income + midleclass_income) / 2) * rich
    S3 = round(S3, 2)
    Sgeneral = S1 + S2 + S3
    Sgeneral = round(Sgeneral,3)
    gini_coff= 1 - (2 * Sgeneral)
    return gini_coff 

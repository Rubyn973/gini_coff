class Calculator:
    def ginicoff(self, poor: float, midleclass: float, rich: float, poor_income: float, midleclass_income: float, rich_income: float) :
        S1 = (self.poor * self.poor_income) / 2
        S1 = round(S1, 3)
        S2 = ((self.poor_income + self.poor_income + self.midleclass_income)/2) * self.midleclass
        S2 = round(S2, 3)
        S3 = ((1 + self.poor_income + self.midleclass_income) / 2) * self.rich
        S3 = round(S3, 2)
        Sgeneral = S1 + S2 + S3
        Sgeneral = round(Sgeneral,3)
        gini_coff= 1 - (2 * Sgeneral)
        return gini_coff 

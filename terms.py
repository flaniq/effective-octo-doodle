import json
value_ids = [389832,379361,387323,445594,429610,492511,379364,446674]
"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Creation of container with attribute id and value. Usage of name 
Imput Example:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""
def createAttributeTerm(attr_id, attr_val):
newterm1 = createAttributeTerm(5471, value_ids)
"""
Input Example:
"""
def createManufacturerTerm(manufact_val):
newmanterm = createManufacturerTerm("Lenovo")
"""
"""
def composeTerms(logic, man_term, term1 = 0, term2 = 0, term3 = 0, term4 =0):
query = composeTerms("must", newmanterm, newterm1, newterm1, newterm1, newterm1)
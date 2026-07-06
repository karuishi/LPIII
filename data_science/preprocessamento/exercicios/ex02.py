"""

Considere a situação onde empresas podem solicitar serviços diversos de sua empresa após terem realizado um cadastro. Infelizmente o cadastro
das empresas é feito online e sem validação e muitos dados estão incorretos.

Os dados cadastrados para cada empresa são:
CNPJ
Razão Social
Situação (Ativo ou não):
Ano de fundação

O único dado que foi validado durante o cadastro foi o formato do CPNJ. Discuta maneiras possíveis de resolver esse problema de 
inconsistência na base de dados (com ou sem código).
Dica: Não pense apenas nos algoritmos apresentados, durante o pré-processamento muitas vezes é necessário adaptar-se ao ambiente.

R: A partir do CNPJ é possível pesquisar todos os dados restantes para assim tomar uma decisão final.
"""

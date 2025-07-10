import re

def email_valido(email):
    """
    Verifica se o email é válido (formato e domínios permitidos).
    """
    email = email.strip()
    if ' ' in email:
        return False
    padrao = r'^[\w\.-]+@(gmail\.com|hotmail\.com)$'
    return re.match(padrao, email)



def senha_valida(senha):
    """
    Verifica se a senha é válida (mínimo 8 caracteres, letras, números, sem espaços).
    """
    if senha != senha.strip():
        return False
    if ' ' in senha:
        return False
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Za-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    return True



def telefone_valido(telefone):
    """
    Verifica se o telefone é válido (11 dígitos numéricos).
    """
    return telefone.isdigit() and len(telefone) == 11
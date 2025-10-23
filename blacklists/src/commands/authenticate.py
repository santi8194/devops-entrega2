from blacklists.src.commands.base_command import BaseCommand
from blacklists.src.errors.errors import NotToken, TokenInvalid

def verify_token(token):
    
    token_valid = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5MTA3NTAyNyIsImV4cCI6MTcyOTE4MDc3N30.2mGqEH_n7AeFHCfGBR9XPv2prxqBCVVlpC-9TRQ8ouA'
    
    if token_valid == token:
        id = token_valid
        return id
    else:
        return None

class Authenticate(BaseCommand):
    def __init__(self, headers):
        self.headers = headers

    def execute(self):
        if 'Authorization' not in self.headers:
            raise NotToken()  # El token no está presente en los encabezados
            
        token = self.headers['Authorization'].split('Bearer ')[-1]        
        id = verify_token(token)
        
        if not id:
            raise TokenInvalid() # El token no es válido o está vencido
        
        return id

import ormar
from pydantic import validator
import re
from config import database,metadata


class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'papeis'
    id:int = ormar.Integer(primary_key=True)
    nome:str = ormar.String(max_length=100)
    sigla:str = ormar.String(max_length=10)
    cnpj:str = ormar.String(max_length=20)

    @validator('sigla')
    def valida_formatacao_sigla(cls,value):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(value):
            raise ValueError('A sigla do papel é invalida!')
        return value
    





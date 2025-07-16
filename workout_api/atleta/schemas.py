from pydantic import BaseModel
from typing import Annotated, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotaded[str, Field(description="Nome do Atleta", examples="Pedro", max_length=50)]
    cpf: Annotaded[str, Field(description="CPF do Atleta", examples="00123456789", max_length=11)]
    idade: Annotaded[int, Field(description="Idade do Atleta", examples=25)]
    peso: Annotaded[PositiveFloat, Field(description="Peso do Atleta", examples=65.5)]
    altura: Annotaded[PositiveFloat, Field(description="Altura do Atleta", examples=1.67)]
    sexo: Annotaded[str, Field(description="Peso do Atleta", examples="M", max_length=1)]


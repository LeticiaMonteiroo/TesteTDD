# test_meu_programa.py
import pytest
from meu_programa import EscolhaUsuario

def test_saida_eh_string_quando_entrada_0():
    obj = EscolhaUsuario(0)
    resultado = obj.processar()
    assert isinstance(resultado, str), "A saída deve ser uma string"

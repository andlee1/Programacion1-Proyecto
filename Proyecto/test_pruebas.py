from validaciones import validar_dni,validar_email,validar_telefono
import re

def test_validar_dni():
	assert(validar_dni("46249731")) == True
	assert(validar_dni("abcdefgh")) == False
	assert(validar_dni("5673")) == False

def test_validar_email():
	assert(validar_email("cliente@ejemplo.com")) == True
	assert(validar_email("@@ejemplo.96")) == False
	assert(validar_email("cliente@ejemplo.com.ar")) == False

def test_validar_telefono():
	assert(validar_telefono("3444-636375")) == True
	assert(validar_telefono("011-636375")) == False
	assert(validar_telefono("344636375")) == False





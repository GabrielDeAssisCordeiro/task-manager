import main
from main import lista

def add_note(lista,nome):
  maior_id = 0
  for notas in lista:
    if notas["ID"] > maior_id:
      maior_id = notas["ID"]
  novo_id = maior_id + 1

  new_tarefa = {"ID":novo_id, "Título":nome, "Concluída":False}
	#open("notas.JSON", "a", encoding="utf-8")
  return lista.append(new_tarefa)

def list_notes():
    ids = []
    for notas in lista:
      ids.append(notas["ID"])
        
    return

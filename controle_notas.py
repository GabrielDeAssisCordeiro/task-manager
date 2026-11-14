lista = []

def add_note(nome):
  maior_id = 0
  for notas in lista:
    if notas["ID"] > maior_id:
      maior_id = notas["ID"]
  novo_id = maior_id + 1

  new_tarefa = {"ID":novo_id, "Titulo":nome, "Concluido":False}
	#open("notas.JSON", "a", encoding="utf-8")
  lista.append(new_tarefa)
  print("Tarefa Adicionada")

def list_notes():
  if not lista:
    print("Nenhuma tarefa cadastrada")
  else:
    for nota in lista:
      if nota["Concluido"]:
        status = "[x]"
      else:
        status = "[ ]"
      print(f"{nota['ID']} - {status} {nota['Titulo']}")

def do_note(id_concluir):
  for nota in lista:
    if nota["ID"] == id_concluir:
        nota["Concluido"] = True
        print(f"Tarefa {nota['Titulo']} concluída")
        return True
  return False

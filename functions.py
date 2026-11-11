from main import lista

def add_note(nome):
	nota = {"ID": 1, "Título":nome, "Concluída":"False"}
	#open("notas.JSON", "a", encoding="utf-8")
	return lista.append(nota)

def list_notes():
    ids = []
    for notas in lista:
      ids.append(notas["ID"])
        
    return

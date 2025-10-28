import json
import os

# Caminho do arquivo onde os dados serão salvos
ARQUIVO_USUARIOS = "data/usuarios.json"

def carregar_usuarios():
    """Lê o arquivo JSON e retorna a lista de usuários."""
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    """Salva a lista de usuários no arquivo JSON."""
    os.makedirs(os.path.dirname(ARQUIVO_USUARIOS), exist_ok=True)
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

def adicionar_usuario(nome, email):
    """Adiciona um novo usuário à lista e salva no arquivo."""
    usuarios = carregar_usuarios()
    
    # Verifica se o email já existe
    if any(u["email"] == email for u in usuarios):
        print("❌ Usuário com este e-mail já existe!")
        return
    
    novo_usuario = {"nome": nome, "email": email}
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("✅ Usuário adicionado com sucesso!")

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return
    
    print("\n=== Lista de Usuários ===")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nome']} - {u['email']}")

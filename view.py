from biblioteca_db import BibliotecaDB

# Instanciar a classe BibliotecaDB com o nome do banco de dados
db = BibliotecaDB('biblioteca.db')

# Criar tabelas (caso não existam)
db.criar_tabela_livros()
db.criar_tabela_usuarios()
db.criar_tabela_emprestimos()

# Inserir alguns livros (apenas para exemplo)
db.inserir_livro(
    titulo="O Senhor dos Anéis",
    autor="J.R.R. Tolkien",
    editora="HarperCollins",
    ano_publicacao=1954,
    isbn="978-0261102385"
)

db.inserir_livro(
    titulo="1984",
    autor="George Orwell",
    editora="Secker & Warburg",
    ano_publicacao=1949,
    isbn="978-0451524935"
)

# Exibir todos os livros
livros = db.exibir_livros()

# Mostrar os livros na saída
print("Livros na biblioteca:")
for livro in livros:
    print(f"Título: {livro[1]}")
    print(f"Autor: {livro[2]}")
    print(f"Editora: {livro[3]}")
    print(f"Ano de Publicação: {livro[4]}")
    print(f"ISBN: {livro[5]}")
    print("-" * 20)

# Inserir alguns usuários
db.inserir_usuario(
    nome="João",
    sobrenome= "da Silva",
    email="joao.silva@example.com",
    telefone="123456789"
)

db.inserir_usuario(
    nome="Maria",
    sobrenome="Oliveira",
    email="maria.oliveira@example.com",
    telefone="987654321"
)

# Exibir todos os livros
usuarios = db.exibir_usuario()

for usuario in usuarios:
    print(f'Usuario:')
    print(f"Nome: {usuario[1]}")
    print(f"Sobrenome: {usuario[2]}")
    print(f"Email: {usuario[3]}")
    print(f"Telefone: {usuario[4]}")
    print("-" * 20)

# Inserir alguns empréstimos
db.inserir_emprestimo(
    id_usuario=1,
    id_livro=1,
    data_emprestimo="2024-06-27",
    data_devolucao=None  # Simulando um empréstimo em aberto
)

db.inserir_emprestimo(
    id_usuario=2,
    id_livro=2,
    data_emprestimo="2024-06-28",
    data_devolucao=None  # Simulando um empréstimo em aberto
)

# Exibir todos os empréstimos em aberto
emprestimos_abertos = db.exibir_emprestimos()

print("Empréstimos em aberto:")
for emprestimo in emprestimos_abertos:
    print(f"Título do Livro: {emprestimo[0]}")
    print(f"Nome do Usuário: {emprestimo[1]}")
    print(f"E-mail do Usuário: {emprestimo[2]}")
    print(f"Data de Empréstimo: {emprestimo[3]}")
    print("-" * 20)

# Fechar a conexão
db.fechar_conexao()

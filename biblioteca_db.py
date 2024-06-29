import sqlite3

class BibliotecaDB:
    def __init__(self, db_name):
        """Inicializa a conexão com o banco de dados."""
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def criar_tabela_livros(self):
        """Cria a tabela de livros se não existir."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                autor TEXT,
                editora TEXT,
                ano_publicacao INTEGER,
                isbn TEXT
            )
        ''')
        self.con.commit()

    def criar_tabela_usuarios(self):
        """Cria a tabela de usuários se não existir."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                sobrenome TEXT,
                email TEXT,
                telefone TEXT
            )
        ''')
        self.con.commit()

    def criar_tabela_emprestimos(self):
        """Cria a tabela de empréstimos se não existir."""
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos(
                id INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                id_livro INTEGER,
                data_emprestimo TEXT,
                data_devolucao TEXT,
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
                FOREIGN KEY(id_livro) REFERENCES livros(id)
            )
        ''')
        self.con.commit()

    def inserir_livro(self, titulo, autor, editora, ano_publicacao, isbn):
        """Insere um novo livro na tabela de livros."""
        self.cur.execute('''
            INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn)
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo, autor, editora, ano_publicacao, isbn))
        self.con.commit()

    def inserir_usuario(self, nome, sobrenome, email, telefone):
        """Insere um novo usuário na tabela de usuários."""
        self.cur.execute('''
            INSERT INTO usuarios (nome, sobrenome, email, telefone)
            VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, email, telefone))
        self.con.commit()

    def inserir_emprestimo(self, id_usuario, id_livro, data_emprestimo, data_devolucao):
        """Insere um novo empréstimo na tabela de empréstimos."""
        self.cur.execute('''
            INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao)
            VALUES (?, ?, ?, ?)
        ''', (id_usuario, id_livro, data_emprestimo, data_devolucao))
        self.con.commit()

    def exibir_livros(self):
        """Exibe todos os livros da tabela de livros."""
        self.cur.execute('SELECT * FROM livros')
        livros = self.cur.fetchall()
        return livros

    def exibir_usuario(self):
        """Exibe todos os usuarios da tabela usuarios."""
        self.cur.execute('SELECT * FROM usuarios')
        usuarios = self.cur.fetchall()
        return usuarios

    def exibir_emprestimos(self):
        """Exibe todos os empréstimos da tabela de empréstimos."""
        self.cur.execute('''SELECT livros.titulo, usuarios.nome, usuarios.sobrenome,
                            emprestimos.data_emprestimo, emprestimos.data_devolucao
                            FROM livros
                            INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
                            INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
                            WHERE emprestimos.data_devolucao IS NULL''')
        emprestimos = self.cur.fetchall()
        return emprestimos

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.con.close()

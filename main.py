from database import Database
from play_database import PlayDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.210.122.52:7687", "neo4j", "injection-helicopters-taxes")
db.drop_all()

# Criando uma instância da classe PlayDatabase para interagir com o banco de dados
play_db = PlayDatabase(db)

# Criando alguns jogadores
play_db.create_player("Falcao")
play_db.create_player("Lionel Messi")
play_db.create_player("Ronaldo")
play_db.create_player("Bruno Rodrigues")

# Criando algumas partidas e relação entre jogadores
play_db.create_plays("Lionel Messi", "Ronaldo")
play_db.create_plays("Lionel Messi", "Bruno Rodrigues")
play_db.create_plays("Lionel Messi", "Falcao")

# Atualizando o nome de um jogador
play_db.update_professor("Lionel Messi", "Cristiano Ronaldo")

play_db.insert_player_plays("Bruno Rodrigues", "Falcao")
play_db.insert_player_plays("Ronaldo", "Falcao")

# Deletando um jogador
play_db.delete_player("Cristiano Ronaldo")
play_db.delete_player("Falcao")

# Print de todas as informações do banco de dados
print("Players:")
print(play_db.get_player())
print("Plays:")
print(play_db.get_plays())

# Fechando a conexão
db.close()
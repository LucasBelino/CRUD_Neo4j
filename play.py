class SchoolDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_plays(self, name, player_name):
        query = "MATCH (p:Player {name: $player_name}) CREATE (:Plays {name: $name})<-[:PLAY]-(p)"
        parameters = {"name": name, "player_name": player_name}
        self.db.execute_query(query, parameters)

    def get_player(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_plays(self):
        query = "MATCH (a:Plays)<-[:PLAY]-(p:Player) RETURN a.name AS name, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["player_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_player_plays(self, player_name, play_name):
        query = "MATCH (a:Player {name: $player_name}) MATCH (b:Plays {name: $plays_name}) CREATE (a)-[:PLAY]->(b)"
        parameters = {"player_name": player_name, "plays_name": plays_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

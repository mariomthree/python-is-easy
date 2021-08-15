from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt+routing://localhost:7687", auth=("neo4j", "password"))
driver.close()
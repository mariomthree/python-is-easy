from neo4j import GraphDatabase, basic_auth

# Database Credentials
uri             = "bolt://localhost:7687"
userName        = "neo4j"
password        = "password"

# Connect to the neo4j database server
graphDB_Driver  = GraphDatabase.driver("neo4j://127.0.0.1:7687", auth=("neo4j", "password"))

# CQL to query all the cities present in the graph
cqlNodeQuery = "MATCH (m:City) RETURN m"

# CQL to query the distances from Nairobi to some of the other African capital cities
cqlEdgeQuery  = "MATCH (m:city {name:'Nairobi City'})-[r]->(n:city) RETURN n.name,r.miles"

# CQL to create a graph containing some of the African capital cities
cqlCreate = """CREATE (Addis:city { name: "Addis"}),
(Nairobi:city { name: "Nairobi City"}),
(Lago:city { name: "Lago City"}),
(Johannesburg:city { name: "Johannesburg City"}),
(Addis)-[:connects_in {miles: 2259}]->(Nairobi),
(Addis)-[:connects_in {miles: 2210}]->(Lagos),
(Addis)-[:connects_in {miles: 3227}]->(Johannesburg),
(Nairobi)-[:connects_in {miles: 2259}]->(Addis),
(Nairobi)-[:connects_in {miles: 1233}]->(Lagos),
(Nairobi)-[:connects_in {miles: 1233}]->(Johannesburg),
(Johannesburg)-[:connects_in {miles: 3227}]->(Addis),
(Johannesburg)-[:connects_in {miles: 1233}]->(Nairobi),
(Johannesburg)-[:connects_in {miles: 2260}]->(Lagos),
(Lagos)-[:connects_in {miles: 2210}]->(Addis),
(Lagos)-[:connects_in {miles: 1233}]->(Nairobi),
(Lagos)-[:connects_in {miles: 2260}]->(Johannesburg)"""


# Execute the CQL query
with graphDB_Driver.session() as graphDB_Session:

    # Create nodes
    graphDB_Session.run(cqlCreate)

    # Query the graph    
    nodes = graphDB_Session.run(cqlNodeQuery)

    print("List of African Capital cities present in the graph:")
    for node in nodes:
        print(node)

    # Query the relationships present in the graph
    nodes = graphDB_Session.run(cqlEdgeQuery)

    print("Distance from Nairob City to the other African Cities present in the graph:")
    for node in nodes:
        print(node)
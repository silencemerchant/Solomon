from neo4j import GraphDatabase
from datetime import datetime

class IntelligenceGraph:
    """Neo4j-based Intelligence Graph (STIX-inspired)"""
    
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", 
                                         auth=("neo4j", "solomon2026"))
    
    def close(self):
        self.driver.close()
    
    def add_entity(self, entity_type: str, name: str, properties: dict = None):
        """Add entity to graph (Person, Company, Device, etc.)"""
        with self.driver.session() as session:
            session.run("""
                MERGE (e:Entity {name: $name, type: $type})
                SET e += $props,
                    e.updated_at = $timestamp
            """, name=name, type=entity_type, 
                props=properties or {}, 
                timestamp=datetime.utcnow().isoformat())
    
    def add_relationship(self, from_name: str, to_name: str, rel_type: str):
        """Create relationship between entities"""
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Entity {name: $from}), (b:Entity {name: $to})
                MERGE (a)-[r:RELATIONSHIP {type: $rel}]->(b)
                SET r.updated_at = $timestamp
            """, from=from_name, to=to_name, rel=rel_type, 
                timestamp=datetime.utcnow().isoformat())

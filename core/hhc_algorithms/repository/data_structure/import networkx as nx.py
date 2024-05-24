import networkx as nx
from models.patient_model import Patient

class Graph:
    def __init__(self) -> None:
        
        self.G = nx.Graph()

    def add_node(self, patient: Patient):
        self.G.add_node(patient.to_object())


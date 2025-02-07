from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
from typing import List
import matplotlib
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import networkx as nx
import chinese_whispers
import json

matplotlib.use('Agg')  # Usar backend no interactivo
app = FastAPI()

# Definir el modelo para el vector
class VectorF(BaseModel):
    vector: List[float]

def generate_graph(num_nodes=20, connection_prob=0.2):
    G = nx.erdos_renyi_graph(num_nodes, connection_prob)
    edges = [(u, v, np.random.rand()) for u, v in G.edges()]
    return G, edges

def plot_clusters(G, labels, output_file:str):
    pos = nx.spring_layout(G)
    unique_labels = list(set(labels))
    plt.title("Chinese Whispers")
    colors = plt.cm.jet(np.linspace(0, 1, len(unique_labels)))
    color_map = {label: colors[i] for i, label in enumerate(unique_labels)}
    
    node_colors = [color_map[labels[i]] for i in range(len(labels))]
    nx.draw(G, pos, node_color=node_colors, with_labels=True, edge_color='gray')
    
    #plt.show()
    plt.savefig(output_file)
    plt.close()
    
@app.post("/chinese-whispers")
def calculo(num_nodes: int, iterations: int):
    output_file = 'chinese_whispers.png'
    # Generar un grafo aleatorio
    G, edges = generate_graph(num_nodes)

    # Ejecutar el algoritmo Chinese Whispers
    labels = chinese_whispers.chinese_whispers(edges, num_nodes, iterations)

    # Visualizar los clusters
    plot_clusters(G, labels, output_file)
    
    j1 = {
        "Grafica": output_file
    }
    jj = json.dumps(str(j1))

    return jj

@app.get("/chinese-whispers-graph")
def getGraph(output_file: str):
    return FileResponse(output_file, media_type="image/png", filename=output_file)
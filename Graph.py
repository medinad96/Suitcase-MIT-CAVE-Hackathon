from Vertex import Vertex
import networkx as nx
import pandas as pd

cerealnodes = []

def creategraph():
    #Get the data from the Excel files
    cerealxlsx = pd.ExcelFile('CAVE_Hackathon_Data.xlsx')
    cereal_sd = pd.read_excel(cerealxlsx, 'Cereal_SD')
    cereal_ll = pd.read_excel(cerealxlsx, 'Cereal_LL')
    
    #Create the nodes for the graph
    for index, row in cereal_sd.iterrows():
        tempvertex = Vertex(row[0], row[1], row[6], row[4])
        cerealnodes.append(tempvertex)
        
    #Create the graph using NetworkX
    cerealG = nx.DiGraph()
    cerealG.add_nodes_from(cerealnodes)
    
    for index, row in cereal_ll.iterrows():
        cerealG.add_edges_from([(row[0], row[1])])

def main():
    creategraph()

main() 

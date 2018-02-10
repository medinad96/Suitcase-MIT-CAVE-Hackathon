class Vertex: 
    
    def __init__(self, node, stageCost, stageTime, demand):
        self.id = node
        self.stageCost = stageCost
        self.stageTime = stageTime
        self.demand = demand
        
    def __str__(self):
        return str(self.id)
    
    def get_id(self):
        return self.id
    
    def get_cost(self):
        return self.stageCost
    
    def get_stageTime(self):
        return self.stageTime
    
    def get_demand(self):
        return self.demand
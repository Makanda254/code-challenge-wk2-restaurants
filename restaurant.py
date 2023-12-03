class Restaurant:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
 
 #Test to return name name of restaurant   
restaurant1 = Restaurant('CJs')
print(restaurant1.get_name()) # output: CJs
        
        
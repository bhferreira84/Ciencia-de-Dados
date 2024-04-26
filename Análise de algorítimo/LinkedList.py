class Node:

    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
     

class LinkedList:
    def __init__(self):
        self.root = None
        self._size = 0


    def append(self, elem):
        #Insersão quando a lista não está vazia
        if self.root:
            ponteiro = self.root
            while(ponteiro.next):
                ponteiro = ponteiro.next
            ponteiro.next = Node(elem)
        else:
            # primeira insersão
            self.root = Node(elem)
        self._size+=1
  
    def __len__(self):
        # retorna o tamanho da lista
        return self._size
    
    def get(self, index):
        # retorna o elemento associado ao index
        pass
    
    def set(self,index, elemento):
        pass
    
    def __getitem__(self, index):
        ponteiro= self.root
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError(" List index out of range ")
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError(" List index out of range ")
    
    def __setitem__(self,index, elem):
        ponteiro= self.root
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError(" List index out of range ")
        if ponteiro:
            ponteiro.data = elem
        else:
            raise IndexError(" List index out of range ")
    
    
    def index(self, elem):
        # encontra o index do elemento
        ponteiro = self.root
        i = 0
        while(ponteiro):
            if ponteiro.data == elem:
                return i
            ponteiro = ponteiro.next
            i += 1
            
            
        raise ValueError(f'{elem} is not in list')    
            
            
      
    
    
    
    
    
    
    
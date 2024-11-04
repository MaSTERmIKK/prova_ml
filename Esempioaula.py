class Punto():

    x = 0
    y = 0


    def muovipunto(self, nuovax, nuovay):
        self.x = nuovax
        self.y = nuovay
    

    def distanza_or(self):
        if self.x > 0 and self.y > 0:
            print("la distanza da zero è-->")
            print(self.x, self.y)
        
        if self.x > 0:
            print("la distanza da zero è-->")
            print(self.x)
    
        if self.y > 0:
            print("la distanza da zero è-->")
            print(self.y)


        
oggettPunto = Punto()
oggettPunto.muovipunto(6, 11)
oggettPunto.distanza_or()
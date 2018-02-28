class LightTester(object):
     
    lights = None
    def __init__(self,N):
        self.size = N
        self.lights = [[False]*N for _ in range(N)]
              
    def apply(self,cmd):
        if cmd is 'switch on':
            self.lights[0][1] = True
        elif cmd is 'switch off':
            self.lights[0][1] = False
        elif cmd is 'toggle':
            if self.lights[0][1] == True:
                self.lights[0][1] = False
            else:
                self.lights[0][1] = True
    
    def count(self):
        count = 0
        for i in self.lights:
            for j in i:
                if j == True:
                    count+=1
        return count

    def coordinates(self,x,y,x1,y1):
        for i in range(y,y1+1):
            for j in range(x,x1+1):
                self.lights[i][j] = True
        for i in self.lights:
            print(i)
        return(self.count())


if __name__ == "__main__":
    LightTester().__init__
PI = 3.141592

class Math:
    def solve(self, r):
        return PI * (r**2)
    

def sum(a, b):
    return a+b

if __name__ == '__main__':
    print(PI)
    ma = Math()
    print(ma.solve(2))
    print(sum(PI, 4.4) )
    
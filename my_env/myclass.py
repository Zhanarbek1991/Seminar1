class Point
    x = 2
    y = 3
    c = 4

    def print_xyc(self):
        print("x = ", self.x)
        print("y = ", self.y)
        print("c = ", self.c)

if __name__ == "__main__":
    p = Point()
    p.print_xyc()
    print(p.y,p.x,p.c)
    print(p.x,p.y,p.c)
    print(p.c,p.x,p.y)

class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        
    def informace(self):
        return f"Jmeno: {self.jmeno}, Vek: {self.vek}"
    

class Student(Osoba):
    def __init__(self, jmeno, vek, obor):
        super().__init__(jmeno, vek)
        self.obor = obor
        
    def informace(self):
        return f"Jmeno: {self.jmeno}, Vek: {self.vek}, Obor: {self.obor}"
    
    
osoba1 = Osoba("Petr", 57)
student1 = Student("Honza", 18, "IT")

print(osoba1.informace())
print(student1.informace())
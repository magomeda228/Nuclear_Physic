mn = 939.55
mae = 931.49
mp = mae * 1.007825
ma = mae * 4.0026432

class Nuclear:
    """
    Initialize a Nuclear object with given properties."""
    def __init__(self, Name, Z, A, Ma, M10=0, M11=0, M42=0):
        self.Name = Name
        self.Z = Z
        self.A = A
        self.Ma = Ma
        self.M10 = M10
        self.M11 = M11
        self.M42 = M42
        print(f"\n name = {self.Name}")
    def E_nucleon(self):
        print(f"e = {(self.Z * mp + (self.A - self.Z) * mn - mae* self.Ma) / self.Ma:.2f}, Mev; ", 
              f"W = {(self.Z * mp + (self.Ma - self.Z) * mn-mae * self.Ma):.2f}, Mev")
        return 0
    
    def E_neitron(self):
        print(f"e_n = {mn + mae * self.M10 - self.Ma * mae:.2f}, Mev")
        return 0
    def E_proton(self):
        print(f"e_p = {mp + mae * self.M11 - self.Ma * mae:.2f}, Mev")
        return 0
    def E_alpha(self):
        print(f"e_a = {ma + self.M42 * mae - self.Ma * mae :.2f}, Mev")
        return 0

    
Al = Nuclear('_Al', 13, 27, 26.981532, 25.986892)
Al.E_nucleon()
_4He = Nuclear('_4He', 13, 27, 4.0026, 3.0160, 3.016049)
_4He.E_neitron()
_4He.E_proton()
_5He = Nuclear('_5He', 2, 5, 5.012, 4.0026, 4.026432)
_5He.E_neitron()
_5He.E_proton()
_9B = Nuclear('_9B', 5, 9, 9.01330, 8.024067, 8.005305)
_9B.E_neitron()
_9B.E_proton()
_12C = Nuclear('_12C', 6, 12, 12.00, 11.011433, 11.009305, 8.005305)
_12C.E_neitron()
_12C.E_proton()
_12C.E_alpha()
_27Al = Nuclear('_27Al', 13, 27, 26.981538, 25.986892, 25.985837, 22.989769)
_27Al.E_neitron()
_27Al.E_proton()
_27Al.E_alpha()
_56Fe = Nuclear('_56Fe', 26, 56, 55.934936, 54.938121, 54.938043, 51.940505)
_56Fe.E_neitron()
_56Fe.E_proton()
_56Fe.E_alpha()
_107Ag = Nuclear('_107Ag', 47, 107, 106.905092, 105.90664, 105.903480, 102.905494)
_107Ag.E_neitron()
_107Ag.E_proton()
_107Ag.E_alpha()
_236U = Nuclear('_236U', 92, 236, 236.045566, 235.043928, 235.045399, 232.03805)
_236U.E_neitron()
_236U.E_proton()
_236U.E_alpha()
_210P = Nuclear('_210P', 84, 210, 209.982874, 0, 0, 205.974465)
_210P.E_alpha()
_226Ra = Nuclear('_210P', 88, 226, 226.025408, 0, 0, 222.017576)
_226Ra.E_alpha()

#     ρ a test sűrűsége, kg/m³
#
#     m a test teljes tömege, kg
#
#     V a test teljes térfogata, m³,
def suruseg(m: float, V: float):
    ρ: float
    ρ = m / V
    return ρ

def soros(R1: float, R2: float):
    Re: float
    Re = R1+R2
    return Re


def parhuzamos(R1: float, R2: float):
    Re: float
    Re = (R1 * R2) / (R1 + R2)
    return Re


a = suruseg(m = 5, V = 0.02)

b = suruseg(4, 0.2)

print(a)
print(b)

print(parhuzamos(100, 100))
print(soros(100, 100))

Re = parhuzamos(
    soros(
        parhuzamos(50, 50),
        parhuzamos(
            parhuzamos(50, 50),
            50)
    ),
    50
)

print(Re)
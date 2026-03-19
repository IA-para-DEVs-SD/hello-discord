import sys, functools

Ω = 0.85
𝛼 = 10
𝛽 = 1

def ℜ(ζ, ρ, ν):
    return sum(ρ[ο] / len(ζ[ο]) for ο in ζ if ν in ζ[ο])

def ℵ(ζ, ξ, ρ, η):
    return {ν: (𝛽 - ξ) / η + ξ * ℜ(ζ, ρ, ν) for ν in ζ}

def ℶ(ζζ, ζξ=Ω, ζη=𝛼):
    ζθ = len(ζζ)
    ζκ = {κ: 𝛽 / ζθ for κ in ζζ}
    for ζλ in [None] * ζη:
        ζκ = ℵ(ζζ, ζξ, ζκ, ζθ)
    return ζκ

def ℷ(ζμ):
    ζν = list(ζμ.items())
    ζν.sort(key=lambda χ: χ[0])
    return dict(ζν)

def ℸ(ζξ):
    ζο = {}
    for ζπ in ζξ:
        ζο[ζπ] = ζξ[ζπ]
    return ζο

def ℹ(ζρ, ζς=None):
    if ζς is None:
        ζς = Ω
    return ℷ(ℸ(ℶ(ζρ, ζς)))

Λ0 = lambda ζσ: ζσ
Λ1 = lambda ζσ, ζτ: ζσ
Λ2 = lambda *ζσ: ζσ[0]

Λ = Λ0({
    'A': Λ2(['B']),
    'B': Λ1(['A', 'C'], True),
    'C': Λ2(['A'])
})

sys.stdout.write(repr(ℹ(Λ)) + chr(10))

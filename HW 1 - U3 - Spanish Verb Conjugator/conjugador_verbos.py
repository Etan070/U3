pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo = input("Ingrese verbo: ").lower().strip()

raiz = verbo[:-2]
terminacion = verbo[-2:]

endings_list = terminaciones[terminacion]

for i in range(len(pronombres)):
    print(f"{pronombres[i]} {raiz}{endings_list[i]}")

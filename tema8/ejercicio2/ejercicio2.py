import pickle

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Crear un objeto de la clase Vehiculo
vehiculo = Vehiculo("Toyota", "Camry", 2020)

# Guardar el objeto en un archivo
with open("vehiculo.pkl", "wb") as f:
    pickle.dump(vehiculo, f)

# Cargar el objeto desde el archivo
with open("vehiculo.pkl", "rb") as f:
    vehiculo_cargado = pickle.load(f)

print(vehiculo_cargado.marca) # imprimiría "Toyota"
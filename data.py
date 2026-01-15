import pandas as pd
import matplotlib.pyplot as plt

X=13
Y=5

data = pd.read_csv("data.csv")

durata = data["Durata"]
puls = data ["Puls"]
calorii = data["Calorii"]
maxpuls = data["MaxPuls"]

plt.figure()
plt.plot(durata, label = "Durata")
plt.plot(puls, label = "Puls")
plt.plot(calorii, label="Calorii")
plt.plot(maxpuls, label="Maxpuls")
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend()
plt.show()

plt.figure()
plt.plot(durata.head(X), label="Durata")
plt.plot(puls.head(X), label="Puls")
plt.plot(calorii.head(X), label="Calorii")
plt.plot(maxpuls.head(X), label="Maxpuls")
plt.title(f"Primele {X} valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend()
plt.show()

plt.figure()
plt.plot(durata.tail(Y), label="Durata")
plt.plot(puls.tail(Y), label="Puls")
plt.title(f"Ultimele {Y} valori - Durata si puls")
plt.xlabel ("Index")
plt.ylabel ("Valori")
plt.legend()
plt.show()

           

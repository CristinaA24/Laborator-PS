import numpy
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului
amplitudine = 1.0      # Amplitudinea semnalului
frecventa = 5.0        # Frecvența semnalului în Hz
faza = np.pi / 2       # Faza în radiani; np.pi/2 va face cele două semnale identice
timp_total = 2.0       # Durata semnalului în secunde

# Generarea semnalului
timp = np.linspace(0, timp_total, int(250 * timp_total))  # 250 de eșantioane pe secundă
semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)
semnal_cosinus = amplitudine * np.cos(2 * np.pi * frecventa * timp)

# Crearea subplot-urilor
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

# Primul subplot cu semnalul sinus
axs[0].plot(timp, semnal_sinus, 'b-')
axs[0].set_title('Semnal Sinusoidal')
axs[0].set_xlabel('Timp (s)')
axs[0].set_ylabel('Amplitudine')

# Al doilea subplot cu semnalul cosinus
axs[1].plot(timp, semnal_cosinus, 'r-')
axs[1].set_title('Semnal Cosinusoidal')
axs[1].set_xlabel('Timp (s)')
axs[1].set_ylabel('Amplitudine')

# Afișarea graficelor
plt.tight_layout()
plt.show()

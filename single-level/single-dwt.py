from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import pywt

samplerate, data = wavfile.read('sample.wav');  # Reading the audio file
t = np.arange(len(data)) / float(samplerate);  # Getting Time
data = data/max(data);  # Normalize Audio Data

cA, cD = pywt.dwt(data, 'bior6.8', 'per');  # DWT

y = pywt.idwt(cA, cD, 'bior6.8', 'per')  # IDWT

wavfile.write('sampleR.wav', samplerate, y);  # writing y as Audio
wavfile.write('samplecD.wav', samplerate, cD);  # writing cD as Audio
wavfile.write('samplecA.wav', samplerate, cA);  # writing cA as Audio

# Formatting for figure
L = len(data);
y = y[0:L];  # Matching length with input for plotting

plt.figure(figsize=(30, 20));

plt.subplot(4, 1, 1)
plt.plot(t, data, color='k');
plt.xlabel('Time');
plt.ylabel('S');
plt.title('Original Signal');

plt.subplot(4, 1, 2)
plt.plot(cA, color='r');
plt.xlabel('Samples');
plt.ylabel('cA');
plt.title('Approximation Coeff. (cA)');

plt.subplot(4, 1, 3)
plt.plot(cD, color='g');
plt.xlabel('Samples');
plt.ylabel('cD');
plt.title('Detailed Coeff. (cD)');

plt.subplot(4, 1, 4)
plt.plot(t, y, color='b');
plt.xlabel('Time');
plt.ylabel('Value');
plt.title('Reconstructed Signal');

plt.savefig('plot.png', dpi=100)  # Saving plot as PNG image
plt.show()

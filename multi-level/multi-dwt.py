from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import pywt

samplerate, data = wavfile.read('sample.wav');  # Reading the audio file
t = np.arange(len(data)) / float(samplerate);  # Getting Time
data = data/max(data);  # Normalize Audio Data

coeffs = pywt.wavedec(data, 'bior6.8', mode='sym', level=2);  # DWT
cA2, cD2, cD1 = coeffs

y = pywt.waverec(coeffs, 'bior6.8', mode='sym')  # IDWT

wavfile.write('sampleR.wav', samplerate, y);  # writing y as Audio
wavfile.write('samplecA2.wav', samplerate, cA2);  # writing cA2 as Audio
wavfile.write('samplecD2.wav', samplerate, cD2);  # writing cD2 as Audio
wavfile.write('samplecD1.wav', samplerate, cD1);  # writing cD1 as Audio

# Formatting for figure
L = len(data);
y = y[0:L];  # Matching length with input for plotting

plt.figure(figsize=(30, 20));

plt.subplot(5, 1, 1)
plt.plot(t, data, color='k');
plt.xlabel('Time');
plt.ylabel('S');
plt.title('Original Signal');

plt.subplot(5, 1, 2)
plt.plot(cA2, color='r');
plt.xlabel('Samples');
plt.ylabel('cA2');
plt.title('Approximation Coeff. (cA2)');

plt.subplot(5, 1, 3)
plt.plot(cD2, color='g');
plt.xlabel('Samples');
plt.ylabel('cD2');
plt.title('Detailed Coeff. (cD2)');

plt.subplot(5, 1, 4)
plt.plot(cD1, color='m');
plt.xlabel('Samples');
plt.ylabel('cD1');
plt.title('Detailed Coeff. (cD1)');

plt.subplot(5, 1, 5)
plt.plot(t, y, color='b');
plt.xlabel('Time');
plt.ylabel('Value');
plt.title('Reconstructed Signal');

plt.savefig('plot.png', dpi=100)  # Saving plot as PNG image
plt.show()

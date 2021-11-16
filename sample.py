from pywt import wavedec
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import pywt
import copy

def wavelet_reconstructor(signal, wavelet_name, decomposition_level):
    reconstructed_signal = {}

    # row signal
    # reconstructed_signal.append(signal)
    reconstructed_signal['row'] = signal

    coeffs = wavedec(signal, wavelet_name, level=decomposition_level)
    backup = copy.deepcopy(coeffs)
     # reconstructed signal with all sub-bands
     # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))

    reconstructed_signal['all_recon'] = pywt.waverec(coeffs,wavelet_name)
    # with out approximate sub-band
    coeffs[-4] = np.zeros_like(coeffs[-4])

    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['rm_approx'] = pywt.waverec(coeffs,wavelet_name)

    # with out approximate and level - 1 sub-band
    # coeffs[-4] = np.zeros_like(coeffs[-4])
    coeffs[-1] = np.zeros_like(coeffs[-1])
    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['rm_approx_cd1'] = pywt.waverec(coeffs,wavelet_name)

    # single sub-bands
    # only level 3 approximate coefficient
    coeffs = copy.deepcopy(backup)
    coeffs[-1] = np.zeros_like(coeffs[-1])
    coeffs[-2] = np.zeros_like(coeffs[-2])
    coeffs[-3] = np.zeros_like(coeffs[-3])
    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['cA3'] = pywt.waverec(coeffs,wavelet_name)

    # only level 3 detailed coefficient
    coeffs = copy.deepcopy(backup)
    coeffs[-1] = np.zeros_like(coeffs[-1])
    coeffs[-2] = np.zeros_like(coeffs[-2])
    coeffs[-4] = np.zeros_like(coeffs[-4])
    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['cd3'] = pywt.waverec(coeffs,wavelet_name)

    # only level 2 detailed coefficient
    coeffs = copy.deepcopy(backup)
    coeffs[-1] = np.zeros_like(coeffs[-1])
    coeffs[-3] = np.zeros_like(coeffs[-3])
    coeffs[-4] = np.zeros_like(coeffs[-4])
    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['cd2'] = pywt.waverec(coeffs,wavelet_name)

    # only level 1 detailed coefficient
    coeffs = copy.deepcopy(backup)
    coeffs[-2] = np.zeros_like(coeffs[-2])
    coeffs[-3] = np.zeros_like(coeffs[-3])
    coeffs[-4] = np.zeros_like(coeffs[-4])
    # reconstructed_signal.append(pywt.waverec(coeffs,wavelet_name))
    reconstructed_signal['cd1'] = pywt.waverec(coeffs,wavelet_name)
	
    plt.figure(figsize=(30, 20));

    plt.subplot(5, 1, 1)
    plt.plot( reconstructed_signal['cA3'] , color='r');
    plt.xlabel('Samples');
    plt.ylabel('cA3');
    plt.title('cA3');

    plt.subplot(5, 1, 2)
    plt.plot(reconstructed_signal['cd3'], color='g');
    plt.xlabel('Samples');
    plt.ylabel('cd3');
    plt.title('cd3');

    plt.subplot(5, 1, 3)
    plt.plot(reconstructed_signal['cd2'], color='m');
    plt.xlabel('Samples');
    plt.ylabel('cd2');
    plt.title('cd2');

    plt.subplot(5, 1, 4)
    plt.plot(reconstructed_signal['cd1'], color='b');
    plt.xlabel('Time');
    plt.ylabel('cd1');
    plt.title('cd1');

    plt.savefig('plot.png', dpi=100)  # Saving plot as PNG image
    plt.show()

    return reconstructed_signal

samplerate, data = wavfile.read('sample.wav');  # Reading the audio file
t = np.arange(len(data)) / float(samplerate);  # Getting Time
data = data/max(data);  # Normalize Audio Data
y = wavelet_reconstructor(data, 'bior6.8', 3);









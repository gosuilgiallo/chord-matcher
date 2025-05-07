# This script visualizes the results of the chord analysis.
# It generates a plot showing the waveform, chromagram, and chord segments.
# It saves the plot as 'chord_analysis.png'.
# visualization.py

import matplotlib.pyplot as plt
import librosa.display

def visualize_results(chroma, chord_segments, y, sr, hop_length):
    plt.figure(figsize=(12, 10))
    plt.subplot(3, 1, 1)
    librosa.display.waveshow(y, sr=sr, alpha=0.6)
    plt.title('Waveform')
    plt.subplot(3, 1, 2)
    librosa.display.specshow(chroma, x_axis='time', y_axis='chroma', hop_length=hop_length, sr=sr, cmap='coolwarm')
    plt.colorbar()
    plt.title('Chromagram')
    plt.subplot(3, 1, 3)
    for start, end, chord in chord_segments:
        plt.axvspan(start, end, alpha=0.3, label=chord)
    plt.legend()
    plt.tight_layout()
    plt.savefig('assets/chord_analysis.png', dpi=300)
    plt.close()
import librosa
import numpy as np
from scipy.ndimage import median_filter

def extract_chroma_features(audio_path, n_fft=4096, hop_length=512, n_chroma=12):
    """
    Extract features from audio.
    """
    y, sr = librosa.load(audio_path, sr=None)
    y_harmonic, _ = librosa.effects.hpss(y, margin=3.0)
    y_harmonic = librosa.util.normalize(y_harmonic)
    chroma = librosa.feature.chroma_cqt(
        y=y_harmonic, sr=sr, hop_length=hop_length, n_chroma=n_chroma,
        bins_per_octave=36, fmin=librosa.note_to_hz('C2')
    )
    chroma_filtered = median_filter(chroma, size=(1, 5))
    chroma_norm = librosa.util.normalize(chroma_filtered, axis=0)
    return chroma_norm, sr, hop_length, y
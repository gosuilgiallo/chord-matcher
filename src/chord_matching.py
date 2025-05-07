import numpy as np
import json
import librosa

# load data from chords.json
# The JSON file should contain a dictionary where keys are chord names and values are lists of floats representing the chord templates.
with open('data/chords.json', 'r') as f:
    CHORD_TEMPLATES = {k: np.array(v) for k, v in json.load(f).items()}

def chord_template_matching(chroma, min_duration_frames=12):
    num_frames = chroma.shape[1]
    chord_labels = np.zeros(num_frames, dtype=object)
    chord_scores = np.zeros(num_frames)
    for i in range(num_frames):
        frame = chroma[:, i]
        max_correlation = -np.inf
        best_chord = "N.C."
        for chord_name, template in CHORD_TEMPLATES.items():
            correlation = np.dot(frame, template) / (np.linalg.norm(frame) * np.linalg.norm(template))
            if correlation > max_correlation:
                max_correlation = correlation
                best_chord = chord_name
        if max_correlation > 0.4:
            chord_labels[i] = best_chord
            chord_scores[i] = max_correlation
        else:
            chord_labels[i] = "N.C."
            chord_scores[i] = max_correlation
    return chord_labels, chord_scores

def create_chord_segments(chord_labels, sr, hop_length):
    chord_changes = np.where(np.roll(chord_labels, 1) != chord_labels)[0]
    segment_starts = np.concatenate([[0], chord_changes])
    segment_ends = np.concatenate([chord_changes, [len(chord_labels)]])
    segment_times_start = librosa.frames_to_time(segment_starts, sr=sr, hop_length=hop_length)
    segment_times_end = librosa.frames_to_time(segment_ends, sr=sr, hop_length=hop_length)
    chord_segments = [
        (segment_times_start[i], segment_times_end[i], chord_labels[segment_starts[i]])
        for i in range(len(segment_starts))
    ]
    return chord_segments
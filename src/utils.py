# This file contains utility functions for processing chord progressions.

def consolidate_chord_progression(chord_segments, min_duration=0.5):
    filtered_segments = []
    last_chord = None
    last_start = 0
    for start, end, chord in chord_segments:
        duration = end - start
        if chord == "N.C." or duration < min_duration:
            continue
        if chord == last_chord:
            continue
        else:
            if last_chord is not None:
                filtered_segments.append((last_start, start, last_chord))
            last_chord = chord
            last_start = start
    if last_chord is not None:
        filtered_segments.append((last_start, chord_segments[-1][1], last_chord))
    return filtered_segments
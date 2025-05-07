import os
import sys
from features import extract_chroma_features
from chord_matching import chord_template_matching, create_chord_segments
from utils import consolidate_chord_progression
from visualization import visualize_results
from banner import print_banner

def main(audio_path):
    chroma, sr, hop_length, y = extract_chroma_features(audio_path)
    chord_labels, chord_scores = chord_template_matching(chroma)
    chord_segments = create_chord_segments(chord_labels, sr, hop_length)
    consolidated_segments = consolidate_chord_progression(chord_segments)
    visualize_results(chroma, consolidated_segments, y, sr, hop_length)
    print("\nFound chord progression:")
    for start, end, chord in consolidated_segments:
        print(f"{start:.2f}s - {end:.2f}s: {chord}")

if __name__ == "__main__":
    print_banner()
    if len(sys.argv) < 2:
        audio_path = input("Please enter the path to an audio file (type 'chords/Em_C_G_D.wav' for a ready example): ").strip()
    else:
        audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"Error: File '{audio_path}' not found.")
        sys.exit(1)
    main(audio_path)
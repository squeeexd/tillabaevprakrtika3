FREQUENCIES = {
    'C': 261.63,  # До
    'C#': 277.18, # До диез
    'D': 293.66,  # Ре
    'D#': 311.13, # Ре диез
    'E': 329.63,  # Ми
    'F': 349.23,  # Фа
    'F#': 369.99, # Фа диез
    'G': 392.00,  # Соль
    'G#': 415.30, # Соль диез
    'A': 440.00,  # Ля
    'A#': 466.16, # Ля диез
    'B': 493.88   # Си
}


note_with_octave = input("Введите ноту с номером октавы (например, C4, A#3, C8): ")

note = note_with_octave[:-1]
octave = int(note_with_octave[-1])

base_frequency = FREQUENCIES[note]

frequency = base_frequency * (2 ** (octave - 4))

print(f"Частота ноты {note_with_octave}: {frequency:.2f} Гц")
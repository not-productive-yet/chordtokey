print("chord to key")
print("_____________________________________________")
number_input_Chords = int(input("How many chords are you using? "))

input_chords = []
for index in range(number_input_Chords):
    user_input = input("Chord " + str(index + 1) + ": ")
    input_chords.append(user_input)

musical_keys = {
    "C": ["c", "dm", "em", "F", "G", "Am", "Bdim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "E": ["E", "Fm", "Gm", "A", "B", "Cm", "Ddim"]
}
print("_____________________________________________")
numberKeysFound = 0

# loop through every key to find input chords
for key in musical_keys:
    input_chords_found = 0
    for chord in range(7):
        for input_chord in input_chords:
            if musical_keys[key][chord].lower() == input_chord:
                input_chords_found += 1
    if input_chords_found == number_input_Chords:
        print("Key of", key)
        print(musical_keys[key])
        numberKeysFound += 1

if numberKeysFound == 0:
    print("No keys found..")

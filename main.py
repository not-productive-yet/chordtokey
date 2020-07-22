from keys import musical_keys

print("chord to key")
print("_____________________________________________")
number_input_chords = int(input("How many chords are you using? "))

input_chords = []
for index in range(number_input_chords):
    user_input = input("Chord " + str(index + 1) + ": ")
    input_chords.append(user_input)

print("_____________________________________________")
numberKeysFound = 0

# loop through every key to find input chords
for key in musical_keys:
    input_chords_found = 0
    for chord in range(7):
        for input_chord in input_chords:
            if musical_keys[key][chord].lower() == input_chord:
                input_chords_found += 1
    if input_chords_found == number_input_chords:
        print("Key of", key)
        print(musical_keys[key])
        numberKeysFound += 1

if numberKeysFound == 0:
    print("No keys found..")

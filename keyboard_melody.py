import pygame
from pynput.keyboard import Key, Listener

pygame.init()


MELODY_FUR_ELISE = [
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
    'B4', 'C5', 'D5', 'E5',
    'G4', 'F5', 'E5', 'D5',
    'F4', 'E5', 'D5', 'C5',
    'E4', 'D5', 'C5', 'B4',
    'E4', 'E5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'Ab4', 'B4', 'C5',
    'E4', 'E5', 'Eb5', 'E5', 'Eb5', 'E5', 'B4', 'D5', 'C5', 'A4',
    'C4', 'E4', 'A4', 'B4',
    'E4', 'C5', 'B4', 'A4',
]

MELODY_HAPPY_BIRTHDAY_TO_YOU = [
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
]

MELODY_I_LOVE_YOU = [
     'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
     'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
     'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
     'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
     'G3', 'E3', 'G3', 'G3', 'E3', 'G3',
     'A3', 'G3', 'F3', 'E3', 'D3', 'E3', 'F3',
     'E3', 'F3', 'G3', 'C3', 'C3', 'C3', 'C3', 'C3', 'D3', 'E3', 'F3', 'G3',
     'G3', 'D3', 'D3', 'F3', 'E3', 'D3', 'C3',
]

MELODY_PIRATE_OF_THE_CARRIBEAN = ['A3', 'C4', 'D4', 'D4',
                                  'D4', 'E4', 'F4', 'F4',
                                  'F4', 'G4', 'E4', 'E4',
                                  'D4', 'C4', 'C4', 'D4',
                                  'A3', 'C4', 'D4', 'D4',
                                  'D4', 'E4', 'F4', 'F4',
                                  'F4', 'G4', 'E4', 'E4',
                                  'D4', 'C4', 'D4',
                                  'A3', 'C4', 'D4', 'D4',
                                  'D4', 'F4', 'G4', 'G4',
                                  'G4', 'A4', 'A#4', 'A#4',
                                  'A4', 'G4', 'A4', 'D4',
                                  'D4', 'E4', 'F4', 'F4', 'G4', 'A4', 'D4',
                                  'D4', 'F4', 'E4', 'E4', 'F4', 'D4', 'E4',
                                  'A4', 'C5', 'D5', 'D5',
                                  'D5', 'E5', 'F5', 'F5',
                                  'F5', 'G5', 'E5', 'E5',
                                  'D5', 'C5', 'C5', 'D5',
                                  'A4', 'C5', 'D5', 'D5',
                                  'D5', 'E5', 'F5', 'F5',
                                  'F5', 'G5', 'E5', 'E5',
                                  'D5', 'C5', 'D5',
                                  'A4', 'C5', 'D5', 'D5',
                                  'D5', 'F5', 'G5', 'G5',
                                  'G5', 'A5', 'A#5', 'A#5',
                                  'A4', 'G5', 'A5', 'D5',
                                  'D5', 'E5', 'F5', 'F5', 'G5', 'A5', 'D5',
                                  'D5', 'F5', 'E5', 'E5', 'D5', 'C5', 'D5',   
                                  'D5', 'E5', 'F5', 'F5', 'F5', 'G5', 'A5', 'F5', 'D5', 'A4',
                                  'A#5', 'G5', 'D5', 'A#4',
                                  'D5', 'E5','A5'
]

melody = MELODY_PIRATE_OF_THE_CARRIBEAN
sound_file = 'Piano'


def sharp_cvtr(notes):

    notes = notes.replace(notes[0],chr(ord(notes[0])+1).lower())
    notes = notes.replace('#','b')

    return notes


def key_press_event(key):

    for notes in range(len(melody)):
        sound = sound_file+'/'+melody[0].lower()+'.ogg'
        
        if melody[0][1] == '#':
            sound = sound_file+'/'+sharp_cvtr(melody[0]).lower()+'.ogg'
               
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(0)


    melody.append(melody[0])
    melody.pop(0)


obj = Listener(on_press=key_press_event)
obj.start()
obj.join()
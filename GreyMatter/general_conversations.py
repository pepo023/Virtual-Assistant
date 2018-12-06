# This import is not working as SenseCells.tts even though the
# general conversations file is in the folder above SenseCells
from GreyMatter.SenseCells.tts import tts
import random


def who_are_you():
    messages = ['I am Melissa, your lovely personal assistant.',
                'Melissa, didnt I tell you before?',
                'You ask that so many times!, I am Melissa.']
    tts(random.choice(messages))


def how_am_i():
    replies=['You are goddam handsome', 'My knees go weak when I see you.',
             'You are sexy!', 'You look like the kindest person that I have met.',]
    tts(random.choice(replies))


def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad '
             'away.', 'Why was six scared of seven? Because seven ate nine.',
             'No, I always forget the punch line.']
    tts(random.choice(jokes))


def who_am_i(name):
    tts('You are ' + name + ', a brilliant person. I love you!')


def where_born():
    tts('I was created by a magician.')


def how_are_you():
    tts('I am fine, thank you.')


def echamela():
    tts('Echamela toda en la boca.')

def goodbye():
    tts('Goodbye')

def undefined():
    tts("I don't know what that means!")

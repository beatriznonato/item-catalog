#!/usr/bin/env python2.7

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

TEMP_PATH = '/tmp/sqlalchemy-media'
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(id=0, name='Beatriz Nonato',
             email='bia_nonato@icloud.com',
             picture='https://image.flaticon.com/icons/svg/270/270137.svg')
session.add(user1)
session.commit()

category1 = Category(name="Cattributes")
session.add(category1)
session.commit()

category2 = Category(name="Fancy Cats")
session.add(category2)
session.commit()

category3 = Category(name="Exclusive Cats")
session.add(category3)
session.commit()

category4 = Category(name="Special Edition")
session.add(category4)
session.commit()

menuItem1 = Item(user_id=0,
    name="Midnight Bumbear", 
    description="""Oh heyyy! I'm Midnight Bumbear, a lover of all things green.
    I would honestly rather do anything else than trying to swallow ribbons.
    I can tell you like to get into trouble.""",
    category=category1, 
    picture='https://img.cryptokitties.co/0x06012c8cf97bead5deae237070f9587f8e7a266d/1591641.svg', #noqa
    filename=None) 
session.add(menuItem1)
session.commit()

menuItem2 = Item(user_id=0,
    name="Professor Cattypop", 
    description="""*yawn* Sorry, you caught me napping. I'm Professor Cattypop.
    And you are? I was the real world inspiration for Blackarachnia.
    I can tell you like to get into trouble.""",
    category=category1, 
    filename=None)   
session.add(menuItem2)
session.commit()

menuItem3 = Item(user_id=0,
    name="Kitte Catroo", 
    description="""Ooope. They call me Kitte Catroo. Hey, got any ice cream on you?
    I'm always hungry. My college voted me 'most likely to write the next Harry Potter...
    by plagiarizing J. K. Rowling', but I was always more interested in mocking dogs. Holla at me.""",
    category=category1,
    filename=None)
session.add(menuItem3)
session.commit()

menuItem4 = Item(user_id=0,
    name="Pizzazz", 
    description="""I'm Pizzazz, and I'm as hot as melting cheese, 
    as spicy as Italian sausage, and as well-loved as anchovies. 
    (...In Metropurrlis they're the most popular topping.) 
    Don't you dare bring up pineapple, it doesn't belong on pizza. 
    Not to be extra cheesy, but I'll give you a pizza my heart.""",
    category=category2,
    filename=None)
session.add(menuItem4)
session.commit()

menuItem5 = Item(user_id=0,
    name="Miss Purrfect",
    description="""Hello, lover. You know that feeling you get when a 
    Kitty is beautiful, not for their outward Cattributes, but for their 
    inner hash? That's me, Last Miss Purrfect, the original catty cat. 
    Some would say my heart is decentralized, but all I know for sure is 
    the only thing more eternal than the blockchain is my love for you.""",
    category=category2,
    filename=None)
session.add(menuItem5)
session.commit()

menuItem6 = Item(user_id=0,
    name="Hypurrion",
    description="""Once I might have been a lowly Kitty, but in this
    strange new realm I have become Hypurrion, blessed by the power 
    of the Titans and twice the cat I used to be! Behold my awesome magic, 
    my epic armour, and my powerful purr. I am on the frontlines. Will you claim me?""",
    category=category3,
    filename=None)
session.add(menuItem6)
session.commit()

menuItem7 = Item(user_id=0,
    name="NormalCat",
    description="""48 65 6c 6c 6f 20 74 68 65 72 65 2c 20 49 27
    6d 20 47 6c 69 74 63 68 43 61 74 2e 20 53 6f 6d 65 74 68 69
    6e 67 20 69 73 20 61 20 6c""",
    category=category3,
    filename=None)
session.add(menuItem7)
session.commit()

menuItem8 = Item(user_id=0,
    name="The Last Vulcant",
    description="""Hey good looking, what's cooking? I'm The Last Vulcant 
    and I'm sorry to grill you like that. People assume I'm a pessimist 
    who can't get anything done. The fools! This isn't even my final form. 
    Wait until they see my true power! HYAAAAAaaaaaaawwn...""",
    category=category3,
    filename=None)
session.add(menuItem8)
session.commit()

menuItem9 = Item(user_id=0,
    name="KITT-E",
    description="""Greetings, friend! I am KITT-E the RoboKitty, the world's 
    most adorable catputer and most powerful purrcessor! 
    *Yawn* Oh, excuse me! I'm a little drained.""",
    category=category4,
    filename=None)
session.add(menuItem9)
session.commit()

menuItem10 = Item(user_id=0,
    name="Sparkles",
    description="""Hello, darling, it is I, Sparkles, your fairy catmother.
    Like the invisible paw of fate, I reward pure-hearted Kitty collectors with 
    pawsitively magical one-in-a-million breeds. But don't get on my bad side, 
    or I'll wave my magic wand and transform you into a *shudder* dog.""", 
    category=category4, 
    filename=None)
session.add(menuItem10)
session.commit()

menuItem11 = Item(user_id=0, 
    name="Purremy Allaire", 
    description="""Hey there, I'm Purremy Allaire. Some cats are focused on catnip
    and stalking prey; I'm more about using open internet protocols
    to pave the way for value to move as freely in the future as information 
    moves today. Every Kitty needs scratch, and I want to make getting cryptocurrency
    as easy as catching a mouse.""",
    category=category4,
    picture='http://img.cryptokitties.co/0x06012c8cf97bead5deae237070f9587f8e7a266d/1137672.png', #noqa
    filename=None)
session.add(menuItem11)
session.commit()


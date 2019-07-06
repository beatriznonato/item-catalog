# -*- coding: utf-8 -*-

import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

TEMP_PATH = '/tmp/sqlalchemy-media'
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(
    name='Beatriz Nonato',
    email='bia_nonato@icloud.com',
    picture='/img/creator.png')
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

item1 = Item(
    user_id=1,
    name="Nana Bluepants",
    description="""En Taro Adun, please refer to me as Nana Bluepants,
    and only that. This one time, at band camp, I was voted "class heart
    throb". People think it's weird, but sloth is my favourite delicacy.
    Try it with bearnaise, you'll see what I'm saying.""",
    category=category1,
    picture='https://bit.ly/2K8Fgpk',
    )
session.add(item1)
session.commit()

item2 = Item(
    user_id=1,
    name="Katu Vileright",
    description="""Hiya! My name is Katu Vileright. My best friend is a elf
    on the shelf. I think I would have been voted "most likely to end up on
    reality tv" if I had stayed in school. Check me out!""",
    category=category1,
    picture='https://bit.ly/2wJEaYs'
    )
session.add(item2)
session.commit()

item3 = Item(
    user_id=1,
    name="Count Mugpoppins",
    description="""Yo. My real name is unspeakable in the human language,
    so you can call me Count Mugpoppins. If you ever want to try
    bothering my owner just hit me up. I'm a kitty, you're a human, this
    friendship is our destiny.""",
    category=category1,
    picture='https://bit.ly/2wJEaYs'
    )
session.add(item3)
session.commit()

item4 = Item(
    user_id=1,
    name="Pizzazz",
    description="""I'm Pizzazz, and I'm as hot as melting cheese,
    as spicy as Italian sausage, and as well-loved as anchovies.
    (...In Metropurrlis they're the most popular topping.)
    Don't you dare bring up pineapple, it doesn't belong on pizza.
    Not to be extra cheesy, but I'll give you a pizza my heart.""",
    category=category2,
    picture='https://bit.ly/2Wz1wzd'
    )
session.add(item4)
session.commit()

item5 = Item(
    user_id=1,
    name="Miss Purrfect",
    description="""Hello, lover. You know that feeling you get when a
    Kitty is beautiful, not for their outward Cattributes, but for their
    inner hash? That's me, Last Miss Purrfect, the original catty cat.
    Some would say my heart is decentralized, but all I know for sure is
    the only thing more eternal than the blockchain is my love for you.""",
    category=category2,
    picture='https://bit.ly/2EYhgkK'
    )
session.add(item5)
session.commit()

item6 = Item(
    user_id=1,
    name="Hypurrion",
    description="""Once I might have been a lowly Kitty, but in this
    strange new realm I have become Hypurrion, blessed by the power
    of the Titans and twice the cat I used to be! Behold my awesome
    magic, my epic armour, and my powerful purr. I am on the frontlines.
    Will you claim me?""",
    category=category3,
    picture='https://bit.ly/2KBZK9x'
    )
session.add(item6)
session.commit()

item7 = Item(
    user_id=1,
    name="NormalCat",
    description="""48 65 6c 6c 6f 20 74 68 65 72 65 2c 20 49 27 6d 20
    47 6c 69 74 63 68 43 61 74 2e 20 53 6f 6d 65 74 68 69 6e 67 20 69 73
    20 61 20 6c 69 74 74 6c 65 20 6f 66 66 20 68 65 72 65 2e 20 49 20 62
    65 6c 6f 6e 67 20 74 6f 20 40 70 61 75 6c 69 61 78 2c 20 68 61 76 65
    20 79 6f 75 20 73 65 65 6e 20 68 69 6d 20 62 79 20 63 68 61 6e 63 65 3f""",
    category=category3,
    picture='https://bit.ly/2K3piwJ'
    )
session.add(item7)
session.commit()

item8 = Item(
    user_id=1,
    name="Genesis",
    description="""Greetings, human. I am Genesis. The dogs know me as alpha;
    the cats know me as omega. To your kind, I am a riddle wrapped
    in an enigma, first found by a user in Mystery, Alaska. I looked into
    the void and the void looked back. Then I lost interest. I can’t wait
    to be your new owner!""",
    category=category3,
    picture='https://bit.ly/2KtP0Ke'
    )
session.add(item8)
session.commit()

item9 = Item(
    # user_id=1,
    name="Catzy",
    description="""Hi, I'm Catzy. I like a good joke almost as much as a good
    pair of Bermuda shorts, but not nearly as much as fast, reliable exchanges.
    If I can't find it I build it, and if I can't build it, I keep dreaming
    until I can. It’s a crypto gold rush, and I'm inventing the pan.""",
    category=category4,
    picture='https://bit.ly/2WUw5ia'
    )
session.add(item9)
session.commit()

item10 = Item(
    user_id=1,
    name="Sparkles",
    description="""Hello, darling, it is I, Sparkles, your fairy catmother.
    Like the invisible paw of fate, I reward pure-hearted Kitty collectors with
    pawsitively magical one-in-a-million breeds. But don't get on my bad side,
    or I'll wave my magic wand and transform you into a *shudder* dog.""",
    category=category4,
    picture='https://bit.ly/2EX0t1k'
    )
session.add(item10)
session.commit()

item11 = Item(
    user_id=1,
    name="Purremy Allaire",
    description="""Hey there, I'm Purremy Allaire. Some cats are focused on
    catnip and stalking prey; I'm more about using open internet protocols
    to pave the way for value to move as freely in the future as information
    moves today. Every Kitty needs scratch, and I want to make getting
    cryptocurrency as easy as catching a mouse.""",
    category=category4,
    picture='https://bit.ly/2QWFkJj',
    )
session.add(item11)
session.commit()

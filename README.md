# Item Catalog

![pep8](https://img.shields.io/badge/pep8online-compliant-green.svg)

## Description of Project

Create an application that provides a list of items in a variety of categories, 
as well as a system for registering and authenticating users. Registered users will have 
the ability to post, edit and delete their own items.

## Curiosity
> [CryptoKitties](https://www.cryptokitties.co/) is a blockchain game on Ethereum developed by Axiom Zen that allows players to purchase,
collect, breed and sell virtual cats. It is one of the earliest attempts to deploy blockchain 
technology for recreation and leisure.The game's popularity in December 2017 congested the Ethereum network,
causing it to reach an all-time high in number of transactions and slowing it down significantly.
**This catalog contein some these kitties.** :cat:

## How to Install
1. Download or clone from github [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm), instructions on how to install **Vagrant** and **Virtual Box**.
2. Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/)
3. To run the virtual machine we will use the terminal [GitBash](https://git-scm.com/downloads)

## Dependences
For *Ubuntu*
#### Install pip for python 2
1. ``sudo apt update``
2. ``sudo apt install python-pip``
3. ``pip --version``
4. If it worked, the version will be returned.

#### Install Sqlalchemy
- ``sudo pip install SQLAlchemy``

#### Install Flask
- ``sudo pip install Flask``

#### Install Bleach
- ``sudo pip install bleach``

## How to Run
1. Inside the Vagrant directory activate the virtual machine with the **vagrant up** command.
2. After your activation, enter the **vagrant ssh** command to activate your virtual machine.
3. Load the database with the command:
 - ``python create_db_items.py``
 - ``python db_setup.py``
4. In GitBash run the ``python project.py`` command to perform the parsing.
  
### License
MIT © Beatriz Nonato

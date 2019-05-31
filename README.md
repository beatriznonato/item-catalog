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
To install all the dependencies required to run the project:
- ``pip install -r requirements.txt``

## How to Run
1. Inside the Vagrant directory activate the virtual machine with the **vagrant up** command.
2. After your activation, enter the **vagrant ssh** command to activate your virtual machine.
3. Load the database with the command:
 - ``python db_setup.py``
 - ``python create_db_items.py``
4. In GitBash run the ``python project.py`` command to perform the parsing.

## Endpoints to get the JSON.
`` @app.route('/catalog/JSON/')
def showCatalogJSON():
    categories = session.query(Category).all()
   return jsonify(Categories=[c.serialize for c in categories])``
   

``@app.route('/catalog/<string:category_name>/items/JSON')
def showItemsJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category=category)
    return jsonify(Items=[i.serialize for i in items])``
    

``@app.route('/catalog/<string:category_name>/<string:item_name>/JSON')
def showItemJSON(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name,
                                         category=category).one()
    return jsonify(Item=[item.serialize]) ``
    
    
### License
MIT © Beatriz Nonato

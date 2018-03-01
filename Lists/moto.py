# A module with list of bikes

def run():
    moto = [
        'ducati', 'bmw', 'honda', 
        'harley-davidson', 'minsk', 'java'
        ]
    
    # trying append, insert, pop methods, else

    moto.append('suzuki')
    moto.insert(2, 'kawasaki')
    last_deleted = moto.pop(0)
    moto.remove('minsk')
    moto.reverse()

    print("I already sold " + last_deleted.title() + "!")
    del moto[5]
    print("I want to buy " + moto[3].title() + " somewhen!")
    for a in moto:
        print("I like " + a.title() + "!")

if __name__ == "__main__":
    run()


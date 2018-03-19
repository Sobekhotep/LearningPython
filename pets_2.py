def run():

    def describe_pet(anymal_type, pet_name):
        """Output pet information"""
        print("\nI have a " + anymal_type + ".")
        print("My " + anymal_type + "'s name is " + pet_name.title() + ".")

    describe_pet(pet_name=input("Wats your pet's name? "),
                 anymal_type=input("What is your pet? "))
    describe_pet('chinchilla', 'botzman')


if __name__ == "__main__":
    run()


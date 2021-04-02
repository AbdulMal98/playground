def starter():
    # Uncomment 'PokeAppManager.start()' once we have the full flow ready for the PokeApp
    # The 'start()' function will kick off the flow and put our user into the 'Information flow'
    # The 'information flow' is as follows:
    '''
    The user starts 'Main.py'
    -> (PokeAppManager)The user is presented w/ a prompt asking the user to "Choose a pokemon:"
    -> (PokeAppManager) We parse that input and get the information corresponding to that pokemon name.
    IF the input is invalid, tell the user the input is invalid, and prompt "Choose a pokemon:" again.
    -> (PokeClient) Get the Pokemon Information from the 'PokeAPI'
    -> (PokeAppManager) pass the 'PokemonDataDto' to the view
    -> (PokeView) the view will present the Pokemon's information
    -> (PokeAppManager) Prompt the user to pick another
    Pokemon
    '''
    # PokeAppManager.start()


if __name__ == "__main__":
    starter()

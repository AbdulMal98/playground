def showPokemonInfo(pokemon: PokemonDataDto):
    print(
        f'''
        NAME: {pokemon.name}\n
        ID: {pokemon.id}\n
        TYPE: {pokemon.type}\n
        HEIGHT: {pokemon.height}\n
        MOVES: {pokemon.getFormattedMoves()}\n
        ''')

from PokeClient import *

def starter():
    while True:
        infoforpoke=prompt_user()
        if infoforpoke==None:
            continue
        displayinfo(infoforpoke)
        user_input=input('Would you like to find information on another? (yes/no): ')
        if user_input=='no':
            break















if __name__ == "__main__":
    starter()






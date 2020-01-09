

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """update list of old letters.
    :param letter_guessed:leeter guss value
    :param old_letters_guessed: list of all letter guessed
    :type letter_guessed:char
    :type old_letters_guessed:list
    :return:if the update was success?
    :rtype :boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed+=[letter_guessed]
        return True
    else:
        if letter_guessed in old_letters_guessed:
            print("\nX---NOTICE---X:You have already used this character!")
            old_letters_guessed.sort()    
            for char in old_letters_guessed:
                print(char+"->",end = ''),
        else:
            print("X---NOTICE---X:only char!")
        return False
				    
def check_valid_input(letter_guessed, old_letters_guessed):
    """check if the input is valid.
    :param letter_guessed:leeter guss value
    :param old_letters_guessed: list of all letter guessed
    :type letter_guessed:char
    :type old_letters_guessed:list
    :return: if the input is valid?
    :rtype: boolean
    """
    for char in letter_guessed:
        is_alpha=char.isalpha()
        if not is_alpha or len(letter_guessed)>1 or letter_guessed in old_letters_guessed:
            return False
    else:return True
	
def check_win(secret_word, old_letters_guessed):
    """"check if the user gusse all the secret word.
    :param secret_word:the hidden word
    :param old_letters_guessed: list of all letter guessed
    :type secret_word:string
    :type old_letters_guessed:list
    :return True/false if the use gussed all the hidden word
    :rtype :boolean
    """
    if "__" in show_hidden_word(secret_word, old_letters_guessed):
        return False
    else:
        return True
def show_hidden_word(secret_word, old_letters_guessed):
    """show the chars in the hidden word(includ the success gusses).
    :param secret_word:the hidden word
    :param old_letters_guessed: list of all letter guessed
    :type secret_word:string
    :type old_letters_guessed: list
    :return string of the hidden word(includ the success gusses)
    :rtype: string
    """
    
    result=""
    for char in secret_word:
        if char in old_letters_guessed:
            
            result+=char
        else:
            result=result+"__ "
                
    return result
def print_tray(num_of_tries):
    """Keeps Typhoon a dictionary of all the states of the 'hanging man'.
    param num_of_tries: the number of user tries
    param type: int
    return: none
    """
    HANGMAN_PHOTOS=dict()

    HANGMAN_PHOTOS[1]= """   x-------x"""	#firs picture

    HANGMAN_PHOTOS[2]="""    x-------x
    |
    |
    |
    |
    |"""# picture number 2
	
    HANGMAN_PHOTOS[3]="""    x-------x
    |       |
    |       0
    |
    |
    |"""#picture number 3
    HANGMAN_PHOTOS[4]="""    x-------x
    |       |
    |       0
    |       |
    |
    |"""#picture 4
	
    HANGMAN_PHOTOS[5]="""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""#picture 5
	
    HANGMAN_PHOTOS[6]="""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""#pic 6
	
    HANGMAN_PHOTOS[7]="""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""#pic 7 	
    print(HANGMAN_PHOTOS[num_of_tries])
	
		
def new_game_screen():
    """Prints a new game view on the screen
    """
    MAX_TRIES=6
    HANGMAN_ASCII_ART="""        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/"""
    print(HANGMAN_ASCII_ART)
    print("amount of trays:",end = '')
    print(MAX_TRIES)

def choose_word(file_path, index):#C:\Users\maor\Desktop\secret.txt
    """chose the hidden word from fil.
    :param file_path: the location of the file on the device
    :param index: the index of the word in the file
    :type file_path: string
    :type index: int
    :return: hidden word
    :rtype: string
    """
    file_object=open(file_path,"r")
    file_word=file_object.read()
    file_splitted_space=file_word.split(" ")
    space_length=len(file_splitted_space)-1
    if int(index)>space_length:
        round_index=int(index)%space_length
    else: 
        round_index=int(index)
    word_dic=dict()
    i=1
    while len(file_splitted_space)>0:
        temp_word=file_splitted_space[0]
        word_dic[i]=temp_word
        while temp_word in file_splitted_space:
            file_splitted_space.remove(temp_word)
        i=i+1
    file_object.close()
    return i-1, word_dic[round_index]

def main():
    old_letters_guessed=[]
    num_of_tries=1
    new_game_screen()
    print("hello lets start ! ")
    path=input("plese enter the path to the secret word:")
    index=input('plese enter the index of the word on file:')
    num_of_words,secret_word=choose_word(path, index)         
    print_tray(num_of_tries)
    print(show_hidden_word(secret_word,old_letters_guessed))
    while num_of_tries<7:
        tray_char=input("Guess a letter:")
        if try_update_letter_guessed(tray_char, old_letters_guessed):
            num_of_tries+=1
            if tray_char in secret_word:
                num_of_tries-=1
                print("Great guessing")
                print(show_hidden_word(secret_word,old_letters_guessed))
                if check_win(secret_word,old_letters_guessed):
                    print("GAME OVER : _  GREATE YOU WIN !!! ")
                    break
                continue
            else:
                print_tray(num_of_tries)       
        print(" ")
    if not check_win(secret_word,old_letters_guessed):
        print("GAME OVER :you lose tray again")
if __name__ == "__main__": 
    main() 
        


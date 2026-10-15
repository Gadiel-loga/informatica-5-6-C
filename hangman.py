import random

def main():
    start_game("abcd.txt")

def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")

        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            if guess not in incorrect_letters:
                incorrect_letters: {" ".join(incorrect_letters)}
            print(f"Wrong guess! Attempts left:", str(attempts))

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break
    if ateempts == 0 and "_" in hint:
        print("No attempts left, the word was:", word)




#toy en busca d amarte sijn consolidarme ven mi niño q mañana noes importynate pa bonfdad no importa
#LLora llora hasta q tus ojos sean ñmar de cuando eras chiquito de esa delgada linnea que tenes que tragar llora llora que estas lejos de csaas por q el tiepose pasa que estas lejos decasa yo ya me aarepenti ñppor las cosa sque ya hice mal por la sal de mar
#de que nuncame deprima no volveran a pasar ya no quiers desperatar preo yo sit que te quiero masj quea yare llora llora, que pena siente el alma cuando la suerte empia se opone alos deseos sin plvidar tus ojos llora de cuando eras chiquito ser uno con el umbral te ra a piñas y te tenes que tragar llora llora que estas lejos de casa llora llora ´por que elt iempo se apsa llora llora
#llora llora llora llora por que tenes casi 30 y ya te pesan las riendas despuess reviiviste vivri con la panza llena dos tajos en las venas llora llora llora



if __name__ == "__main__":
    main()

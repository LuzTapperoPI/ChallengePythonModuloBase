# Autora: M Luz Tappero
# Descripción del problema: Crear una funcion que reciba un string y devuelva el nombre del ganador y su puntaje. Para cada letra del string se deben formar todas las posibles subcadenas posibles y se suman los puntos correspondientes (1 punto por cada ocurrencia). Si el substring comienza con una vocal se suman los puntos a Kevin, si comienza con una consonante se suman los puntos a Stuart. El juego termina cuando ambos jugadores han formado todas las posibles subcadenas posibles.
# Input: string s
# Output: impresión del ganador y su puntaje. Ademas de la impresión de las posibles subcadenas posibles y los puntos correspondientes.


def minion_game(s): 
    # Definition of variables
    kevin_score = 0
    stuart_score = 0
    UPPERCASE_VOWELS = "AEIOUÁÉÍÓÚÄËÏÖÜ"
    length= len(s)

    # Validate the lenth of the input
    if length > 10**6:
        raise ValueError("The length of the string must not exceed 10^6 characters.")
    # Iterate over the string
    for i in range(length):
        # Calculate the score increment for each iteration
        score_increment = length - i
        current_letter= s[i]
        # A list is created with possible substrings that can be formed. For each number k between index i and the length, a substring is created starting at index i and ending at index k + 1, using slicing notation s[i : k+1].
        possible_substrings= []
        for k in range(i, length):
            possible_substrings.append(s[i : k+1])
        possible_substring= possible_substrings
        
        if current_letter in UPPERCASE_VOWELS:
            #If the letter i is a vowel, add to the score of Kevin.
            kevin_score += score_increment
            print(f" Index {i}: Current string letter {current_letter}, Kevin adds {score_increment} points for the possible combinations {possible_substring} --> Kevin's current score  {kevin_score} - Stuart's current score: {stuart_score}")
        else:
            # If the letter i is a consonant, add to the score of Stuart.
            stuart_score += score_increment
            print(f" Index {i}: Current string letter {current_letter}, Stuart adds {score_increment} points for the possible combinations {possible_substring} --> Stuart's current score: {stuart_score} - Kevin's current score {kevin_score}")
      
    show_results(kevin_score, stuart_score)

# Function to show the results
def show_results(kevin_score, stuart_score):
    print("\nFinal Results:")
    if kevin_score > stuart_score:
        print(f"\nThe winner is Kevin with Score: {kevin_score}")
        print(f"\nStuart loses the game with Score: {stuart_score}")
    elif kevin_score < stuart_score:
        print(f"\nThe winner is Stuart with Score:  {stuart_score}")
        print(f"\nKevin loses the game with Score: {kevin_score}")
    else:
        print("There is no winner. It's a Tie")

# Main program
def main():
    print("Welcome to the Minion Game!")
    while True:
        try:
            s= input("\nInput a string (letters only): ")
            s = s.upper()  # Convert to uppercase
            if not s.isalpha():
                raise ValueError("The input string must contain only alphabetic characters.")
            minion_game(s)
            break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()




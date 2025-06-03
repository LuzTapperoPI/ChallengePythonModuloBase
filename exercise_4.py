# Autora: M Luz Tappero
# Descripción del problema: Crear una clase que reciba un vector de pesos y que tenga métodos para:
# - Sobreescribir los valores de los pesos.
# - Realizar el producto escalar entre el vector de pesos y otro vector de entrada.
# - Realizar una predicción utilizando la función ReLU.
# Crear una clase que herede el comportamiento de la clase anterior y permita agregar el atributo bias y redefinir el método dot para que sume el bias al producto escalar.
# Input: vector de pesos, vector de entrada y bias
# Output: impresión del resultado del producto escalar, predicción y producto escalar con el bias sumado.
# Ya que esta actividad representa el comportamiento de una neurona artificial, nombre a la clase como Perceptron (unidad de cómputo de redes neuronales artificiales).

class Perceptron:
    def __init__(self, weights):
        if not isinstance(weights, list):
            raise TypeError("Weights must be a list")
        self.weights = weights

    # Set_weights method to overwrite the values of the weights attribute
    def set_weights(self, new_weights):
        if not isinstance(new_weights, list):
            raise TypeError("New weights must be a list")
        self.weights = new_weights

    # Dot method that multiplies the weights vector by a vector of input
    def dot(self, input_vector):
        if not isinstance(input_vector, list):
            raise TypeError("Input vector must be a list")
        # Check if the length of the weights vector is equal to the length of the input vector
        if len(self.weights) != len(input_vector):
            raise ValueError("To multiply the input vector by the weights, they must have the same length")
        
        dot_result = 0
        # Multiply each element of the weights vector by the corresponding element of the input vector and sum them to calculate the dot product
        for i in range(len(self.weights)):
            # Accumulate the dot product by multiplying corresponding elements of weights and input_vector
            dot_result += self.weights[i] * input_vector[i]
        return dot_result
    
    # ReLu function that returns the input value x if x is positive, and 0 if x is negative or zero
    def reLu(self, value):
        "Rectified Linear Unit activation function. The ReLu function returns the input value x if x is positive, and 0 if x is negative or zero."
        return max(0, value)
    
    # Predict method that uses the output of the dot method and passes it through the ReLu function
    def predict(self, dot_result):
        prediction = self.reLu(dot_result)
        return prediction

# ExtendedPerceptron class that inherits from Perceptron
class ExtendedPerceptron(Perceptron):
    # Constructor with bias
    def __init__(self, weights, bias):
        super().__init__(weights)
        if not isinstance(bias, int):
            raise TypeError("Bias must be an integer")
        self.bias = bias
    
    # Redefine the dot method to add the bias
    def dot_redefined(self,input_vector):
        dot_product = super().dot(input_vector) + self.bias
        return dot_product


# Function to create perceptron
def perform_perceptron_calculations(weights, input_vector, new_weights, bias):
    perceptron = Perceptron(weights)
    calculate_and_display_results(perceptron, input_vector, "initial")

    perceptron.set_weights(new_weights)
    calculate_and_display_results(perceptron, input_vector, "new")

    perceptron_with_bias = ExtendedPerceptron(new_weights, bias)
    calculate_with_bias(perceptron_with_bias, input_vector)


# Function to calculate and display the results witouth bias
def calculate_and_display_results(perceptron, input_vector, weight_type):
    dot_product = perceptron.dot(input_vector)
    prediction = perceptron.predict(dot_product)
    print(f"\n -> The {weight_type} weights are:", perceptron.weights)
    print(f"\n -> The dot product between the input vector and the {weight_type} weights is: {dot_product:.2f}")
    print(f"\n -> The result of the prediction with the {weight_type} weights of the dot product is: {prediction:.2f}")


# Function to calculate and display the results with bias
def calculate_with_bias(perceptron_with_bias, input_vector):
    dot_product = perceptron_with_bias.dot_redefined(input_vector)
    print("\n -> The bias value is:", perceptron_with_bias.bias)
    print(f"\n -> The dot product between the input vector and the new weights is: {dot_product:.2f}")
    

# Function to ask for weights
def ask_weights(prompt = "\nEnter the weights vector, separated by commas: "):
    while True:
        weights = input(prompt).strip()
        if not weights:
            print("Invalid input. The weights vector cannot be empty.")
            continue
        try:
            weights = [float(x) for x in weights.split(",") if x.strip()]
            if not weights:
                raise ValueError
            return weights
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")


# Function to ask for input vector
def ask_input_vector():
    while True:
        input_vector = input("\nEnter the input vector, separated by commas: ")
        if ',' not in input_vector:
            print("Invalid input. Please enter a list of numbers separated by commas.")
            continue
        try:
            input_vector = [float(x) for x in input_vector.split(",")]
            return input_vector
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")
            continue


# Function to ask for bias
def ask_bias():
    while True:
        try:
            bias = int(input("\nEnter the bias value: "))
            return bias
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Main function
def main():
    while True:
        print("\n**WELCOME TO THE SIMULATION OF THE PERCEPTRON CLASS**")
        input_vector = ask_input_vector()
        # Input vector determines the length of the weights vector
        
        while True:
            weights = ask_weights("\nEnter the weights vector, separated by commas: ")
            if len(weights) == len(input_vector):
                break
            else: 
                print("The length of the weights vector must be equal to the length of the input vector.")

        while True:
            new_weights = ask_weights("\nEnter the new weights vector, separated by commas:")
            if len(new_weights) == len(input_vector):
                break
            else:
                print("The length of the new weights vector must be equal to the length of the input vector.")

        bias = ask_bias()
        print("\n**CALCULUS**")
        perform_perceptron_calculations(weights, input_vector, new_weights, bias)

        ask_to_continue = input("\nDo you want to continue? (yes/no): ")
        if ask_to_continue == "no":
            print("\nExiting the program. Goodbye!\n")
            break
        
if __name__ == "__main__":
    main()









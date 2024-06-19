import random
import matplotlib.pyplot as plt

def Sig_dado_Ant(s, matrizCanal, probPrimerSimbolo):
        symbols = ['B', 'M', 'A']
        if s is None:
            return random.choices(symbols, probPrimerSimbolo)[0]
        else:
            # Obtiene la distribución de probabilidad para el próximo símbolo desde el diccionario
            probabilities = [matrizCanal[s][symbol] for symbol in symbols]
            # Genera el siguiente símbolo basado en las probabilidades
            return random.choices(symbols, probabilities)[0]

def ProbPrimRec(j, N, matrizCanal, tolerance, probPrimerSimbolo):
    prob = 0
    prob_ant = -1
    repeticiones = 0
    m = 0
    probs = []
    
    def converge(prob, prob_ant, m, IT_MIN=10000):
        return abs(prob - prob_ant) < tolerance and m >= IT_MIN
    
    while not converge(prob, prob_ant, m):
        nro_simb = 1
        s = Sig_dado_Ant(None, matrizCanal, probPrimerSimbolo)
        
        while s != j:
            s = Sig_dado_Ant(s, matrizCanal, probPrimerSimbolo)
            nro_simb += 1
            
        if nro_simb <= N:
            repeticiones += 1  
            
        m += 1
        prob_ant = prob
        prob = repeticiones / m
        probs.append(prob)  # Guarda el valor de probabilidad actual para el grafico
        
    return probs, prob

def simulate_and_plot(j, N, matrizCanal, tolerancia, probPrimerSimbolo):
    probs, final_prob = ProbPrimRec(j, N, matrizCanal, tolerancia, probPrimerSimbolo)

    print(f'Probabilidad de que haya {N} simbolos distintos entre apariciones consecutivas del simbolo {j}: {final_prob}')        
    plt.plot(probs)
    plt.xlabel('Iteration')
    plt.ylabel('Probability')
    plt.title(f'Convergence of Probability for j={j} and N={N}')
    plt.grid(True)
    plt.show()

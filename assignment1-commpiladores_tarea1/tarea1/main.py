class DFA():
    def __init__(self, numStates, finalStates, alphabet):
        self.numStates = numStates
        self.finalStates = [int(state) for state in finalStates.split()]
        self.alphabet = alphabet.split()
        self.transitions = {}
        
    def addTransitions(self, line):
        line = line.split(" ")
        value = []
        for i in range(1, len(line)):
            pair = (self.alphabet[i-1], int(line[i]))
            value.append(pair)
        self.transitions[int(line[0])] = value
        
    def delta(self, p, a):
        for val in self.transitions[p]:
            if val[0] == a:
                return val[1]
    
    def minDFA(self):
        matrix = [[False for _ in range(self.numStates)] for _ in range(self.numStates)]
        pairs = []

        # Inicialización de pares distinguibles
        for i in range(self.numStates):
            for j in range(i+1, self.numStates):
                if((i in self.finalStates and j not in self.finalStates) or (j in self.finalStates and i not in self.finalStates)):
                    matrix[i][j] = True
                else:
                    pairs.append((i, j))

        # Iterativamente marcar pares de estados distinguibles
        changed = True
        while changed:
            changed = False
            for (i, j) in pairs:
                if not matrix[i][j]:
                    for char in self.alphabet:
                        state_i = self.delta(i, char)
                        state_j = self.delta(j, char)
                        if state_i > state_j:
                            state_i, state_j = state_j, state_i
                        if matrix[state_i][state_j]:
                            matrix[i][j] = True
                            changed = True
                            break

        # Obtener pares no distinguibles
        not_distinguishable_pairs = []
        for i in range(self.numStates):
            for j in range(i+1, self.numStates):
                if not matrix[i][j]:
                    not_distinguishable_pairs.append((i, j))

        # Imprimir los pares no distinguibles
        for pair in not_distinguishable_pairs:
            print(f"({pair[0]}, {pair[1]})", end=' ')
        print()
    
if __name__ == "__main__":
    c = int(input())
    if c <= 0:
        print("El número de casos debe ser mayor que 0.")
    else:
        for _ in range(c):
            n = int(input())
            if n <= 0:
                print("El número de estados debe ser mayor que 0.")
            else:
                alphabet = input()
                finalStates = input()
                dfa = DFA(n, finalStates, alphabet)
                for i in range(n):
                    line = input()
                    dfa.addTransitions(line)
                dfa.minDFA()

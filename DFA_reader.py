#Função de simulação de um automâto finito determinístico
########################################################################
def simular_dfa(dfa, entrada):
    estado = dfa['initial_state']
    aux = ''.join(entrada)
    aceitar = False
    while len(entrada) > 0:
        c = entrada.pop(0)
        
        if c not in dfa['sigma']:
            print("O símbolo",c,"não pertence ao alfabeto do autômato!")
            break
        elif(estado not in dfa['states']):
            print("O estado", estado,"não pertence ao conjunto de estados do autômato!")
            break
        
        try:
            estado = dfa['delta'][(estado,c)]
            print((estado,c), "->", dfa['delta'][(estado,c)])
        except KeyError:
            print("Não foi possível realizar a transição do estado", estado, "com entrada", c)
            break
        
    if(estado in dfa['final_states'] and len(entrada) == 0):
       aceitar = True

    if(aceitar == True):
       print("A cadeia", aux, "foi aceita pelo autômato!")
    else:
       print("A cadeia", aux, "foi rejeitada pelo autômato!")
########################################################################


while(True):
    #Programa Principal
    entrada = input("Digite a cadeia: ")
    entrada = list(entrada)
    with open('m.dfa.txt') as dfa_file:
            dfa_data = dfa_file.read()
    dfa = eval(dfa_data)
    #Para conferir o conteúdo
    #print(dfa)
    simular_dfa(dfa, entrada)

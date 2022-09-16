#colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#librerías
import time
import random

points = random.randint(1,10)
trivia_start = True
attempt = 0

print(BLUE+"\n¡Bienvenido(a) a mi trivia sobre fútbol!"+RESET)
print(BLUE+"----------------------------------------\n"+RESET)
print(GREEN+"Comenzamos en 5 segundos\n"+RESET)
for chargnum in range(5,-1,-1):
  print(GREEN+"",chargnum,""+RESET)
  time.sleep(1)
player_1 = input(YELLOW+"\nAntes de empezar, ¿cuál es tu nombre?: "+RESET)
print(YELLOW+"\nVeamos que tanto sabes sobre el deporte rey\n"+RESET)
x = input(YELLOW+"Presiona 'enter' para conocer con cuantos puntos comienzas: "+RESET)
print(GREEN+"\n -----------------")
print("|Lanzando dados...|")
print(" -----------------"+RESET)
time.sleep(1)
print(YELLOW+"\nEnhorabuena",player_1,"comienzas con",points,"puntos.\n"+RESET)
print(RED+"*Cada pregunta correcta son 10 puntos adicionales y cada incorrecta son 5 puntos que te descuentan*"+RESET)
while trivia_start == True:
  attempt += 1
  points = points + 0
  print(GREEN+"\nAtento(a), que en 5 segundos se muestran las preguntas!\n"+RESET)
  for numbb in range(5,-1,-1):
    print(GREEN+"",numbb,""+RESET)
    time.sleep(1)
  print(GREEN+"\nIntento número",attempt,":"+RESET)

  questions = {"1) ¿Quién es el único futbolista en ganar 3 veces un mundial?: ": "c","2) ¿En que país se jugó el primer mundial?: ": "a","3) ¿En que mundial ocurrió la controversial jugada 'La mano de Dios'?: ":"b"}
  options = [["a) Diego Armando Maradona 'Maradona'","b) Dinko Dermendzhiev 'Dinko'","c) Edson Arantes do Nascimento 'Pelé'","d) Dimitar Nikolov Yakimov 'Niko'"],["a) Uruguay","b) México","c) Argentina","d) Inglaterra"],["a) Argentina 1978","b) México 1986","c) Italia 1990","d) España 1982"]]
  question_num = 1
  corrects = 0
  respuestas = []
  
  for key in questions:
    print(GREEN+"------------------------------------------\n"+RESET)
    print(GREEN+key+RESET)
    for i in options[question_num-1]:
      print(BLUE+i+RESET)
    question_num +=1
    answer_1 = input(YELLOW+"\nSeleccione (a, b, c, o d): "+RESET).lower()
    while answer_1 not in ("a","b","c","d"):
      answer_1 = input(YELLOW+"Por favor ingrese solo una de las alternativas propuestas: "+RESET).lower()
    if answer_1 == questions.get((key),answer_1):
      points = points +10
    else:
      points = points -5
    print(RED+"Tienes un puntaje acumulado de",points,"puntos."+RESET)
    respuestas.append(answer_1)

  print(GREEN+" \n------------------------------------")
  print("Tus respuestas seleccionadas: ", end=" ")
  for rpta in respuestas:
      print(rpta, end=" ")
  print("\nTu puntaje final es de",points,"puntos!")
  print("------------------------------------\n"+RESET)
  
  new_rand = random.randint(-10,10)
  points = points + new_rand
  var_1 = input("¿Desea arriesgar y aumentar su puntaje final? Escriba 'si' para usar la ruleta y presione cualquier tecla para mantener su puntaje actual: ").lower()
  if var_1 == "si":
    print(RED+"\nTu puntaje final con ruleta fue de",points,"puntos!\n"+RESET)
  else:
    print(YELLOW+"\nGracias por jugar.\n"+RESET)
      
  repeat = input("¿Desea intentarlo de nuevo?. Escriba 'si' para ello y cualquier tecla para 'no': ").lower()
  if repeat != "si":
    print(YELLOW+"\nEspero que te hayas divertido",player_1,"hasta pronto."+RESET)
    trivia_start = False
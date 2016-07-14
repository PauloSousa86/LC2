import os;
dist = int(input("Distancia do comboio para a Gate.(Valor entre 2000 e 5000): "))

if((dist < 2000) or dist > 5000):
	print("Erro, valor abaixo de 2000 ou superior a 5000")

vel = int(input("Velocidade.(Entre 40 e 50: "))
delay = int(input("Delay do lower event: "))

file = open("train.smv", "w")
file.write("MODULE main\n\n")
file.write("VAR\n\t")
file.write("state : {Far, Near, Past};\n\t")
file.write("event : {idle, approach, exit};\n\t")
file.write("x : -200.." + str(dist) + ";\n\t")
file.write("control : controller(event);\n\t")
file.write("\nASSIGN\n")
file.write("\tinit(x) := " + str(dist) + "; init(state) := Far; init(event) := idle;\n")
file.write("\tnext(state) := case\n")
file.write("\t\tstate = Far & x <= 1000 : Near;\n")
file.write("\t\tstate = Near & x <= 0 : Past;\n")
file.write("\t\tstate = Past & x <= -100 : Far;\n")
file.write("\t\tTRUE : state;\n")
file.write("\t\tesac;\n\n")

file.write("\tnext(event) := case\n")
file.write("\t\tstate = Far & x <= 1000 : approach;\n")
file.write("\t\tstate = Past & x <= -100 : exit;\n")
file.write("\t\tTRUE : event;\n")
file.write("\t\tesac;\n\n")

file.write("\tnext(x) := case\n")
file.write("\t\tx <= -100 : " + str(dist-100) + ";\n")
file.write("\t\tstate = Far : x - " + str(vel) + ";\n")
file.write("\t\tstate = Near : x - 30;\n")
file.write("\t\tstate = Past : x - 30;\n")
file.write("\t\tTRUE : x;\n")
file.write("\t\tesac;\n\n")

file.write("SPEC AG (( x = 0) -> (control.gate.state = Closed & control.gate.y =0))\n\n")

file.write("MODULE controller(event)\n")
file.write("VAR\n")
file.write("\taction : {idle, lower, raise};\n")
file.write("\tstate : {idle, raising, lowering};\n")
file.write("\tgate : gate(action);\n")
file.write("\tz : 0.." + str(delay+1) + ";\n")
file.write("\tu : 0.." + str(delay) + ";\n")

file.write("ASSIGN\n")
file.write("\tinit(state) := idle; init(z) := 0; init(u) := 4; init(action) := idle;\n")
file.write("\tnext(state) := case\n")
file.write("\t\t(state = lowering | state = raising) & z >= u : idle;\n")
file.write("\t\tevent = approach : lowering;\n")
file.write("\t\tevent = exit : raising;\n")
file.write("\t\tTRUE : state;\n")
file.write("\t\tesac;\n\n")

file.write("\tnext(z) := case\n")
file.write("\t\t(state = lowering | state = raising) & z < u : z + 1;\n")
file.write("\t\t(state = lowering | state = raising) & z >= u : 0;\n")
file.write("\t\tTRUE : z;\n")
file.write("\t\tesac;\n\n")

file.write("\tnext(u) := u;\n\n")

file.write("\tnext(action) := case\n")
file.write("\t\tevent = approach & z >= u : lower;\n")
file.write("\t\tevent = exit & z >= u : raise;\n")
file.write("\t\tTRUE : action;\n")
file.write("\t\tesac;\n")

file.write("MODULE gate(event)\n")
file.write("VAR\n")
file.write("\tstate : {Open, MoveUp, MoveDown, Closed};\n")
file.write("\ty : -90..190;\n")
file.write("ASSIGN\n")
file.write("\tinit(y) := 90;\n")
file.write("\tinit(state) := Open;\n\n")

file.write("\tnext(state) := case\n")
file.write("\t\tstate = Open & event = lower : MoveDown;\n")
file.write("\t\tstate = Open & event = raise : Open;\n")
file.write("\t\tstate = MoveUp & y = 90 : Open;\n")
file.write("\t\tstate = MoveUp & event = lower : MoveDown;\n")
file.write("\t\tstate = MoveUp & y < 90 & event = raise : MoveUp;\n")
file.write("\t\tstate = MoveDown & y = 0 : Closed;\n")
file.write("\t\tstate = MoveDown & y > 0 & event = lower : MoveDown;\n")
file.write("\t\tstate = MoveDown & event = raise : MoveUp;\n")
file.write("\t\tstate = Closed & event = lower : Closed;\n")
file.write("\t\tstate = Closed & event = raise : MoveUp;\n")
file.write("\t\tTRUE : state;\n")
file.write("\t\tesac;\n\n")

file.write("\tnext(y) := case\n")
file.write("\t\ty > 90 : 90;\n")
file.write("\t\ty < 0 : 0;\n")
file.write("\t\tstate = Open : 90;\n")
file.write("\t\tstate = Closed : 0;\n")
file.write("\t\tstate = MoveDown : y - 9;\n")
file.write("\t\tstate = MoveUp : y + 9;\n")
file.write("\t\tTRUE : y;\n")
file.write("\t\tesac;\n")



















# nalunos = int(input("digite a quantidade de alunos ai: "))
# acc = 0
# for i in range(0, nalunos):
#	 print("digite a nota do aluno " + str(i) + ":")
# 	 nota = int(input())
# 	 acc = acc+nota
# media = acc/nalunos
# print("a media da sala é: ", media)
# print("a media da sala é :{:.0f}".format(media))

acc = 0
nalunos = 0
print("digite a nota do aluno ", nalunos)
nota = int(input())
while(nota>=0):
	acc = acc+nota
	nalunos = nalunos+1
	print("digite a nota do aluno ", nalunos)
	nota = int(input())
if (nalunos>0):
	media=acc/nalunos
	print("media dos alunos é: {:.0f}".format(media))
else:
	print("nao digitou nota alguma")

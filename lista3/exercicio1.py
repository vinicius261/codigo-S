 #Lista de exercícios: Dicionários e Sets

# Exercício 1

alunos_ingles = {"João Alves dos Santos" , "Maria Magalhães", "Antônio da Silva Ferreira", "José Júnior Jarbas", "Henrique da Silva Sauro", "Joaquina Ferreira da Silva", "Fabiana Aparecida Bianco", "Marrone Gutierres", "Carlos Magno Farad", "Antônio da Silva Júnior Amaral"}

alunos_frances = {"João Alves dos Santos", "Antônio da Silva Ferreira", "Fernanda Abdala Mohamed", "Abner Mignon Alib", "Alisson Figueiredo", "Henrique da Silva Sauro","Maria Magalhães", "Marrone Gutierres", "Joaquina Ferreira da Silva"}

total_de_alunos = len(alunos_ingles.union(alunos_frances))


print(f"\nA escola tem {total_de_alunos} alunos matriculados.")

print(f"\nEstão matriculados apenas em inglês {len(alunos_ingles-alunos_frances)} alunos, sendo eles : {alunos_ingles-alunos_frances}")

print(f"\nEstão matriculados apenas em francês {len(alunos_frances-alunos_ingles)} alunos, sendo eles : {alunos_frances-alunos_ingles}")

print(f"\nEstão matriculados em ambos os curos {len(alunos_ingles.intersection(alunos_frances))} alunos, sendo eles : {alunos_ingles.intersection(alunos_frances)}")

print(f"\nEstão matriculados em apenas um curso {len(alunos_ingles.union(alunos_frances)-alunos_ingles.intersection(alunos_frances))} alunos, sendo eles : {alunos_ingles.union(alunos_frances)-alunos_ingles.intersection(alunos_frances)}")
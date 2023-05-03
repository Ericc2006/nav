# Sastādīt programmu, kas lietotājam piedāvā risināt matemātiskos uzdevumus,
# piem. skaitļi varētu tikt ģenerēti nejauši
# tiktu piedāvāta kāda no darbībām, piem. +,-, *, /, kāpināšana
# piem. 7 * 3 = , lietotājam jāievada atbilde.
# Ja ievada 21, tad programmas izvada PAREIZI, ja nē, tad var rīkoties dažādi - izvada NEPAREIZI, vai arī neizvada neko un piedāvā nākamo uzdevumu vai arī izvada nepareizi un piedāvā ievadīt atkārtoti u.tml.

# Būtiski ir lietotājam pajautāt kādā apjomā piedāvāt skaitļus, piem. līdz 10 vai 100 vai citādi
# Programmas beigās izvada pareizo un nepareizo atbilžu skaitu, iegūto vērtējumu %.
# Programma varētu piedāvāt uzdevumus līdz lietotājs atbild, ka vēlas beigt darbu.
# Visi uzdevumi un atbildes jāizvada gan uz ekrāna gan failā.

# Uzdevuma risinājumā jāpielieto funkcijas.
# Visu pārējo funkcionalitāti katrs var papildināt pats.


import random

def generate_question(operation, max_number):
    """Funkcija, kas ģenerē matemātiskos uzdevumus"""
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = num1 / num2
        answer = round(answer, 2)
    question = f"{num1} {operation} {num2} = "
    return question, answer

def ask_question():
    """Funkcija, kas uzdod lietotājam jautājumu"""
    operation = random.choice(['+', '-', '*', '/', '^'])
    max_number = int(input("Ievadiet lielāko skaitli: "))
    question, answer = generate_question(operation, max_number)
    user_answer = input(question)
    if user_answer == str(answer):
        print("Pareizi!")
        return 1
    else:
        print("Nepareizi.")
        return 0

def main():
    """Galvenā programmas funkcija"""
    print("Sveiki! Šī ir matemātikas uzdevumu programma.")
    score = 0
    total_questions = 0
    while True:
        total_questions += 1
        score += ask_question()
        choice = input("Vai vēlaties turpināt? (jā/nē) ")
        if choice.lower() != 'jā':
            break
    percentage = round(score / total_questions * 100, 2)
    print(f"Jūsu kopējais rezultāts: {score}/{total_questions} ({percentage}%)")
    with open("rezultati.txt", "a") as f:
        f.write(f"Kopējais rezultāts: {score}/{total_questions} ({percentage}%)\n")

if __name__ == '__main__':
    main()

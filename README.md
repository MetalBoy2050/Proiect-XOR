# Proiect-XOR
criptare si decriptare cu xor

Membrii echipei:
Petrescu Alexandru-Antonio -> research si ajutor in crearea scriptului de criptare

Cristea Eduard-Gabriel -> research si ajutor in scrierea scriptului de decriptare

Ungureanu Dan-Andrei -> research si ajutor in scrierea scriptului de criptare si decriptare


Numele echipei adverse: ProiectASC

Cheia echipe adverse: ameaparola20

Codul nostru a aflat cheia pornind doar de la ouput. Am construit initial un string ce cuprinde toate caracterele posibile din input, fiind dat faptul ca textul de intrare e unul citet in limba romana. De asemenea, am mai creat un alt string cu toate caracterele ce pot face parte din parola. Dupa am parcurs toate lungimile de parola si pentru fiecare pozitie din cheie, am luat la rand toate caracterele posibile ce pot face parte din cheie si le-am xorat cu caracterele corespunzatoare din output. Daca toate xorarile dadeau caractere ce puteau face parte din input, atunci cel mai probabil acel caracter era pe acea pozitie in cheie, asa ca-l stocam in raspuns. Daca cel putin o xorare dadea un caracter gresit, atunci acel caracter de pe acea pozitie din cheie nu era bun si treceam la urmatorul caracter. Daca la sfarsit, in multimea caracterelor din raspuns nu avem acelasi numar de elemente ca lungimea cheii, inseamna ca lungimea cheii pe care am ales-o e gresita si trecem la urmatoarea lungime posibila.

PS: am luate mai multe caractere decat cele precizate in cerinta proiectului deoarece la alte echipe am intalnit texte scrise in limba engleza sau caractere mai putin intalnite in texte. La o echipa am si intalnit chiar o cheie de 8 caractere, asa ca am crescut range-ul pentru cheie :)))

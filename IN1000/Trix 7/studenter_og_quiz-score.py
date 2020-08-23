class Student :
    def __init__(self, navn = None, quizScore = 0, quizAmount = 0):
        self._navn = navn
        self._quizScore = quizScore
        self._quizAmount = quizAmount

    def legg_til_quiz_score(self, poeng) :
        self._quizScore += poeng
        self._quizAmount += 1

    def gjennomsnittlig_score(self):
        return self._quizScore / self._quizAmount

    def utskrift(self) :
        print(self._navn, self._quizScore, self._quizAmount)

joakim = Student("Joakim")
kristin = Student("Kristin", 100, 1)
dag = Student("Dag", 50, 1)

joakim.legg_til_quiz_score(60)
joakim.legg_til_quiz_score(45)

kristin.legg_til_quiz_score(95)
kristin.legg_til_quiz_score(47)

dag.legg_til_quiz_score(3)
dag.legg_til_quiz_score(2)

joakim.utskrift()
print("Gjennomsnittlig score:", joakim.gjennomsnittlig_score())
kristin.utskrift()
print("Gjennomsnittlig score:", joakim.gjennomsnittlig_score())
dag.utskrift()
print("Gjennomsnittlig score:", joakim.gjennomsnittlig_score())

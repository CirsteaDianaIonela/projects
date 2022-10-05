class Catalogue:

    def __init__(self, firstname, lastname, absences, subject, grades):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__absences = absences
        self.__subjects = {subject: grades}

    def __str__(self):
        return f'The first name is: {self.__firstname}, the last name is: {self.__lastname}, no of absences is ' \
               f'{self.__absences}, and the subjects with all the grades are {self.__subjects}'


    #decoratorul property ajusta sa folosim o metoda cu rol de atribut, metoda absences devine atribut si o apelez prin obiect.metoda, nu prin obiect.metoda().
    # cu ajutorul decoratorului putem declara getter/setter/deleter si avem control total asupra modului de accesare/setare si stergere a datelor
    #using propery decorator + getter function
    @property
    def absences(self):
        return self.__absences

    #using a setter function
    @absences.setter
    def add_absences(self, number_absences):
        self.__absences += number_absences

    # using a setter function
    @absences.setter
    def delete_absences(self, absences_todelete):
        if self.__absences > absences_todelete:
            self.__absences -= absences_todelete

    def add_subject(self, subject, grade):
        self.__subject = self.__subjects.update({subject: grade})

    def subjects_average(self):
        final_grades = {}
        for i, j in self.__subjects.items():
            if all(isinstance(x, int) for x in j):
                medie = sum(j) / len(j)
                final_grades.update({i: medie})
        return final_grades


student1 = Catalogue('Ion', 'Roata', 7, 'Python', [5, 6, 7])
print(student1)
student1.add_absences = 3
print(student1)
student1.delete_absences = 2
print(student1)
student1.add_subject('Java', [8, 9, 10])
print(student1)
# print(student1.subjects_average)

#pending nu mai merge subjects average + de pus setter/property pentru add_subject + subjects_average

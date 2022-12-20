import pandas as pd

# df = pd.read_csv('proiecte.csv') #citesc fisierul csv
# print(df)
# df.info() #vad informatii tehinice despre date
# df.loc[2] = ['Teodora', 'Fulas', 27, 12] #adaug linii noi
# df.loc[3] = ['Marian', 'Fulas', 30, 9]
# df.loc[4] = ['Mugurel', 'Predoiu', 33, 12]
# df.loc[5] = ['Maria', 'Manta', None, 4]
# print(df.head(3)) #vad primele 3 randuri
# print(df.describe()) #s used to generate descriptive statistics of the data
# print(df.memory_usage(deep=True)) #memory usage of each column (in bytes), using deep we get to know the actual space being taken by each column
# print(df.loc[0:2, ['First name', 'Age']]) #accesez doar primii 3 indecsi impreuna cu anumite coloane
# print(df.iloc[:3]) #vad primii 3 indecsi, randuri
# print(df['Working hours'].value_counts()) # numara de cate ori apare fiecare valoare in dataset
# print(df[df['Age']>29]) #pun conditie ca varsta sa fie mai mare de 29
# df = df.drop_duplicates() #sterge duplicatele
# print(df.groupby(by='First name').Age.mean()) #returneaza varsta medie grupata in functie de first name
# df = df.sort_values(by='First name', inplace=True) #sorteaza crescator/alfabetic
# print(df)
# print(df[df['Working hours'].between(10, 15)]) #conditie intre 10-15
# print(df[(df['Age'] > 28) & (df['Working hours'] > 9)]) #2 conditii
# print(df['Working hours'].sum()) #insumeaza tot de pe o anumita coloana
# print(df['Working hours'].mean()) #media de pe o anumita coloana
# print(len(df)) #numara randurile
# print(len(df.columns)) #numara coloanele excluzand-o pe cea cu index
# print(df[df['Age'].isnull()]) #caut in coloana Age unde am null
# print(df)
# df = df.drop(0) #sterg din lista
# print(df)
# df.to_csv('proiecte2.csv') #trimit in csv dupa ce am facut toate prelucrarile necesare


import pandas

data = pandas.read_csv("words_eng.csv")
new_csv = [row for (index, row) in data.iterrows() if row.portugues != "Carregando…"]
new_data = pandas.DataFrame(new_csv)
new_data.to_csv("english_words.csv", index=False)
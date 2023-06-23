import spacy
from spacy import displacy


def example1():
    nlp = spacy.load("ru_core_news_sm")
    doc = nlp("Снижение вероятности воздействия электрическим током на случайный биообъект.")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.dep_)


def example2():
    nlp = spacy.load("ru_core_news_sm")
    doc = nlp(
        "Программу назвали «Yandex», название придумали Илья Сегалович, директор «Яндекса» по технологиям, и генеральный директор компании — Аркадий Волож.")
    displacy.serve(doc, style="ent")
    # # Debug
    # html = displacy.render(doc, style="ent", jupyter=False)
    # with open("output.html", "w", encoding="utf-8") as f:
    #     f.write(html)

# example1()
example2()

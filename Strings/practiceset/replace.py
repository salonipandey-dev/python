letter='''Dear <|NAME|>,
              You are selected !
              <|date|>'''

print(letter.replace("<|NAME|>","Saloni").replace("<|date|>","20th June 2026"))

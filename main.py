from classes.Zamowienie import Zamowienie
from classes.Developer import Developer
from classes.Mieszkanie import Mieszkanie
from classes.Dom import Dom

developer_1 = Developer(1, 'Słoneczny developer', 'ul. Słoneczna 15',
                        '56845345')
mieszkanie_1 = Mieszkanie(1, 50, 'ul. Radosna 1', 4000.93)
dom_1 = Dom(1, 105, 'ul. Radosna 5', 9148.21)
zamowienie_1 = Zamowienie(1, developer_1, [mieszkanie_1, dom_1], 'Wesołe '
                                                               'osiedle')
print(zamowienie_1)

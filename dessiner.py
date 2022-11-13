# Hoang-Thi-Thi Cynthia Phan 20220019
# Vincent Hoang 20183549

# Le code ci-dessous programme un éditeur d'image. L'éditeur d'image permet
# à l'utilisateur de dessiner des rectangles de couleurs et de dimensions
# différentes à l'aide de la souris.

# couleurs est un tableaux de textes de couleurs
couleurs = ["#fff", "#000", "#f00", "#ff0", "#0f0", "#00f", "#f0f"]
largeur = 180           # largeur de la fenêtre de dessin en px
hauteur = 120           # hauteur de la fenêtre de dessin en px
hauteurMenu = 24        # hauteur de la barre de menu
taille = 12             # taille d'un bouton en px
espace = 6              # espace entre et au-dessus de chaque bouton en px
couleurEffacer = "#fff"  # couleur pour effacer les dessins


def coin1Bouton(couleurs, taille, espace):

    # La fonction coin1Bouton retourne un tableau d'enregistrement des
    # coordonnées du coin supérieur gauche de chaque bouton de la barre de
    # menu.

    coin1Tab = []   # tableau d'enregistrements  des coordonnées du coin supérieur gauche de chaque bouton
    i = 1
    for _ in range(len(couleurs) + 1):
        x = i * espace + (i - 1) * taille
        coin1Tab.append(struct(x=x, y=espace))
        i += 1
    return coin1Tab


def coin2Bouton(couleurs, taille, espace):

    # La fonction coin2Bouton retourne un tab;eau d'enregistrement des coordonnées du
    # coin inférieur droit de chaque bouton de la barre menu.

    coin2Tab = []   # tableau d'enregistrements des coordonnées du coin inférieur droit de chaque bouton
    y = espace + taille
    i = 1
    for _ in range(len(couleurs) + 1):
        x = i * (espace + taille)
        coin2Tab.append(struct(x=x, y=y))
        i += 1
    return coin2Tab


def creerBoutons(couleurs, taille, espace, couleurEffacer):

    # La fonction creerBoutons crée les boutons de couleurs et le bouton
    # effacer dans la barre de menu, et retourne un tableau d'enregistrements
    # qui représente les boutons.

    coin1Tab = coin1Bouton(couleurs, taille, espace)
    coin2Tab = coin2Bouton(couleurs, taille, espace)
    boutons = []
    i = 0
    for _ in range(len(couleurs) + 1):
        if i == 0:
            effacer = True
            boutons.append(struct(
                coin1=coin1Tab[i], coin2=coin2Tab[i], couleur=couleurEffacer, effacer=effacer))
        else:
            effacer = False
            boutons.append(struct(
                coin1=coin1Tab[i], coin2=coin2Tab[i], couleur=couleurs[i - 1], effacer=effacer))
        i += 1
    return boutons


def dessinerBoutons(couleurs, taille, espace, couleurEffacer):

    # La procédure dessinerBoutons dessine les boutons dans la barre de menu.

    coin1Tab = coin1Bouton(couleurs, taille, espace)
    coin2Tab = coin2Bouton(couleurs, taille, espace)
    for i in range(len(couleurs) + 1):
        if i == 0:
            fillRectangle(coin1Tab[i].x, coin1Tab[i].y,
                          taille, taille, couleurEffacer)
        else:
            fillRectangle(coin1Tab[i].x, coin1Tab[i].y,
                          taille, taille, couleurs[i - 1])

    for j in range(len(couleurs) + 1):
        # bordure supérieure
        for x1 in range(coin1Tab[j].x, coin2Tab[j].x):
            setPixel(x1, coin1Tab[j].y, "#000")
        # bordure droite
        for y1 in range(coin1Tab[j].y, coin2Tab[j].y):
            setPixel(coin2Tab[j].x - 1, y1, "#000")
        # bordure inférieure
        for x2 in range(coin1Tab[j].x, coin2Tab[j].x):
            setPixel(x2, coin2Tab[j].y - 1, "#000")
        # bordure gauche
        for y2 in range(coin1Tab[j].y, coin2Tab[j].y):
            setPixel(coin1Tab[j].x, y2, "#000")

    k = 1
    for _ in range(taille - 2):
        setPixel(coin1Tab[0].x + k, coin1Tab[0].y + k, "#f00")
        setPixel(coin1Tab[0].x + k, coin1Tab[0].y + taille - 1 - k, "#f00")
        k += 1


def trouverBouton(boutons, position):

    # La fonction trouverBouton prend comme paramètres le tableau
    # d'enregistrement retourné par la fonction creerBoutons (boutons) et un
    # enregistrement de coordonnées cartésiennes (position) pour déterminer
    # si le point du paramètre position se trouve dans un des carrés formés
    # par les boutons.

    if boutons == []:
        return None
    else:
        for i in range(len(boutons)):
            if position.x >= boutons[i].coin1.x and position.x <= boutons[i].coin2.x:
                if position.y >= boutons[i].coin1.y and position.y <= boutons[i].coin2.y:
                    return boutons[i]
                else:
                    return None


def imageOriginaleTab(largeur, hauteur):

    # La fonction imageOriginaleTab crée le tableau de imageOriginale.

    imageOriginaleTab = [None] * largeur
    if largeur == 0:
        return None
    else:
        for i in range(largeur):
            imageOriginaleTab[i] = [None] * hauteur
        return imageOriginaleTab


def imageOriginale():

    # La fonction imageOriginale retourne le tableau des tableaux contenants
    # les textes de couleurs de chaque pixel dans fenêtre de dessin.

    imageOriginale = imageOriginaleTab(getScreenWidth(), getScreenHeight())
    for i in range(getScreenWidth()):
        for j in range(getScreenHeight()):
            imageOriginale[i][j].append(getPixel(i, j))
    return imageOriginale


def dessinerRectangleFlottant(imageOriginale, debut, couleur):

    # La procédure dessinerRectangleFlottant anime le rectangle flottant tant
    # que le bouton de la souris de l'utilisateur reste enfoncé. Elle prend
    # comme paramètre imageOriginal, un tableau de tableaux de textes de
    # couleurs, debut, un enregistrement qui contient les coordonées
    # cartésiennes du clic initial de l'utilisateur, et couleur, le text de
    # la couleur du rectangle.


def restaurerImage(imageOriginale, rectangle):

    # La procédure restaurerImage dessine une section rectangulaire de l'image
    # imageOriginale. La procédure prend comme paramètres imageOriginale, un
    # tableau de tableaux de textes de couleurs, et rectangle, un
    # enregistrement qui contient deux champs (coin1 et coin2). coin1 et
    # coin2 sont aussi des enregistrements qui représentent des coordonnées
    # cartésiennes.


def ajouterRectangle(image, rectangle, couleur):

    # La procédure ajouterRectangle modifie une section du paramètre image.
    # Image est un tableau de tableaux de texte de couleurs. rectangle est un
    # enregistrement qui contient deux champs, coin1 et coin2. coin1 et coin2
    # sont des enregistrements de coordonnées cartésiennes


def traiterProchainClic(couleurs, taille, espace, couleurEffacer, hauteurMenu):

    # La procédre traiterProchainClic attend le prochain clic de la souris de
    # l'utilisateur. Cette procédure détermine si le clic a lieu sur un
    # bouton de couleurs, le bouton effacer, ou dans la fenêtre de dessin.

    boutons = creerBoutons(couleurs, taille, espace, couleurEffacer)
    coin1Tab = coin1Bouton(couleurs, taille, espace)
    coin2Tab = coin2Bouton(couleurs, taille, espace)
    while True:
        souris = getMouse()
        sleep(0.01)
        if souris.button == 0 or souris.button == 2:
            continue
        else:
            if souris.x > 0 and souris.x < getScreenWidth() and souris.y > hauteurMenu and souris.y < getScreenHeight():
                return struct(x=souris.x, y=souris.y)
            else:
                for i in range(len(boutons)):
                    if souris.x > coin1Tab[i].x and souris.x < coin2Tab[i].x and souris.y > coin1Tab[i].y and souris.y < coin2Tab[i].y:
                        if boutons[i].effacer == True:
                            fillRectangle(0, hauteurMenu, getScreenWidth(
                            ), getScreenHeight() - hauteurMenu, couleurEffacer)
                        else:
                            return boutons[i].couleur


def dessiner(largeur, hauteur, hauteurMenu, couleurs, taille, espace, couleurEffacer):

    # La procédure dessiner fait appel aux procédures et fonctions précédentes
    # pour démarrer l'éditeur d'image.

    setScreenMode(largeur, hauteur)
    fillRectangle(0, hauteurMenu, largeur, hauteur - hauteurMenu, "#fff")
    fillRectangle(0, 0, largeur, hauteurMenu, "#888")
    dessinerBoutons(couleurs, taille, espace, couleurEffacer)
    dessinerBordure(couleurs, taille, espace)
    dessinerEffacer(couleurs, taille, espace)


def testDessiner():

    # La procédure testDessiner teste les fonctions et procédures précêdentes.

    # tests pour coin1

    assert coin1([], 12, 6) == [struct(x=6, y=6)]
    assert coin1(["#fff"], 12, 6) == [struct(x=6, y=6), struct(x=24, y=6)]
    assert coin1(["#fff", "#000"], 12, 6) == [struct(
        x=6, y=6), struct(x=24, y=6), struct(x=42, y=6)]

    # tests pour coin2

    assert coin2([], 12, 6) == [struct(x=18, y=18)]
    assert coin2(["#fff"], 12, 6) == [struct(x=18, y=18), struct(x=36, y=18)]
    assert coin2(["#fff", "#000"], 12, 6) == [struct(
        x=18, y=18), struct(x=36, y=18), struct(x=54, y=18)]

    # tests pour creerBoutons

    assert creerBoutons([], 12, 6, "#fff") == [struct(coin1=struct(
        x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)]
    assert creerBoutons(["#fff"], 12, 6, "#fff") == [struct(coin1=struct(x=6, y=6), coin2=struct(
        x=18, y=18), couleur="#fff", effacer=True), struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False)]
    assert creerBoutons(["#fff", "#000"], 12, 6, "#fff") == [struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True), struct(coin1=struct(
        x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False), struct(coin1=struct(x=42, y=6), coin2=struct(x=54, y=18), couleur="#000", effacer=False)]
    assert creerBoutons(["#000", "#f00"], 12, 6, "#00f") == [struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#00f", effacer=True), struct(coin1=struct(
        x=24, y=6), coin2=struct(x=36, y=18), couleur="#000", effacer=False), struct(coin1=struct(x=42, y=6), coin2=struct(x=54, y=18), couleur="#f00", effacer=False)]
    assert creerBoutons(["#f00"], 4, 1, "#000") == [struct(coin1=struct(x=1, y=1), coin2=struct(
        x=5, y=5), couleur="#000", effacer=True), struct(coin1=struct(x=6, y=1), coin2=struct(x=10, y=5), couleur="#f00", effacer=False)]

    # tests pour trouverBouton

    assert trouverBouton([], struct(x=12, y=12)) == None
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)], struct(
        x=12, y=12)) == struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)], struct(
        x=3, y=3)) == None
    assert trouverBouton([struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#000", effacer=False)], struct(
        x=30, y=12)) == struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#000", effacer=False)
    assert trouverBouton([struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#000", effacer=False)], struct(
        x=21, y=12)) == None
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(
        x=18, y=18), couleur="#fff", effacer=True), struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False)], struct(x=12, y=12)) == struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(
        x=18, y=18), couleur="#fff", effacer=True), struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False)], struct(x=30, y=12)) == struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False)
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(
        x=18, y=18), couleur="#fff", effacer=True), struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur="#fff", effacer=False)], struct(x=21, y=12)) == None
    assert trouverBouton([struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18), couleur="#fff", effacer=True)], struct(
        x=12, y=3)) == None

    # tests pour imageOriginaleTab

    assert imageOriginaleTab(0, 10) == None
    assert imageOriginaleTab(1, 0) == [[]]
    assert imageOriginaleTab(3, 0) == [[], [], []]
    assert imageOriginaleTab(1, 1) == [[None]]
    assert imageOriginaleTab(1, 3) == [[None, None, None]]
    assert imageOriginaleTab(3, 1) == [[None], [None], [None]]
    assert imageOriginaleTab(2, 2) == [[None, None], [None, None]]


testDessiner()

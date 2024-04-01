def ordinateur_devine(x):
    petit = 1
    grand = x
    feedback = ''
    while feedback != 'c':
        devine = random.randint(petit, grand)
        feedback = input(f'Est-ce que {devine} est trop grand (G), trop petit (P), ou correct (C) ? ')
        if feedback == 'h':
            haut = devine - 1
        elif feedback == 'b':
            petit = devine + 1
    
    print(f'Hourra ! L\'ordinateur a deviné le nombre, {devine}, correctement')

ordinateur_devine(100)

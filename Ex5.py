def reverter_string():
    string = input('Ex5\nDigite uma frase: ')
    string_inv = ''
    tamanho = len(string)
    for i in range(tamanho):
        string_inv = string_inv + string[tamanho-1]
        tamanho = tamanho - 1
    return string_inv

from lexer import lexer

User_Commands = open("user_text.eevee", "r").readlines()
for line in User_Commands:
    lexer(line)
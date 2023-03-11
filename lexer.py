def lexer(main_syntax):
    State = 0
    Token = ""
    String = ""
    for Char in main_syntax:
        Token = Token + Char
        if Token == " ":
            if State == 0:
                Token = ""
        elif Token == "\n":
            Token = ""
        elif Token == "write":
            Token = ""
        elif Token == "\"":
            if State == 0:
                State = 1
                Token = ""
            elif State == 1:
                State = 0
        elif State == 1:
            String = String + Token
            Token = ""
    print(String)
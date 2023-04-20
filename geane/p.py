POUR_TOUT           = 8704
IL_EXISTE           = 8707
IL_EXISTE_UN_UNIQUE = -8707

INCLUS           = 8712
NON_INCLUS       = 8713

ACCEPT_TABLE = {
    -2: lambda x: False,
    -1: lambda x: True,

    0: lambda x: x in [POUR_TOUT, IL_EXISTE],

    1: lambda x: x in [
        *range(ord("a"), ord("z") + 1),
        *range(ord("A"), ord("Z") + 1)
    ],

    2: lambda x: x in [INCLUS, NON_INCLUS],
}


class P:
    def __init__(self, variables) -> None:
        self.vars = variables


    def get_next_word(self, chars, sp) -> tuple[str, int]:
        buffer = ""

        while (char := chars[sp + 1])[1] == " " or ACCEPT_TABLE[1](char[2]):
            sp += 1

            if char[1] != " ":
                buffer += char[1]

        return buffer, sp

    def test(self, expression: str) -> bool:
        sp = 0
        accept = 0

        # (index, char, ascii code)
        chars = [
            (i, c, ord(c)) for i, c in enumerate(expression)
        ]

        data = {}
        buffer = ""

        while sp < len(chars):
            _, char, code = chars[sp]

            if char == " ":
                sp += 1
                continue

            if ACCEPT_TABLE[accept](code):
                if accept == 0:
                    if chars[sp + 1][1] == "!":
                        code = IL_EXISTE_UN_UNIQUE
                        sp += 1

                    target, sp = self.get_next_word(chars, sp)

                    data["quantificator"] = {
                        "code": code,
                        "target": target
                    }

                    accept = 2

                elif accept == 2:
                    target, sp = self.get_next_word(chars, sp)

                    data["qualificator"] = {
                        "code": code,
                        "target": target
                    }

                    if chars[sp + 1][2] != 44:
                        raise

                    accept = -1
                    buffer = ""

                    sp += 1

                elif accept == -1:
                    buffer += char

                else:
                    raise

            else:
                raise Exception(chars[sp])

            sp += 1

        predicate_expr = buffer

        target_var = data["quantificator"]["target"]
        target_set = self.vars[data["qualificator"]["target"]]
        quantificator = data["quantificator"]["code"]

        if quantificator == POUR_TOUT:
            for i in range(len(target_set)):
                exec(f"{target_var}={target_set}[{i}]")

                if eval(predicate_expr) == False:
                    return False

        elif quantificator == IL_EXISTE:
            for i in range(len(target_set)):
                exec(f"{target_var}={target_set}[{i}]")

                if eval(predicate_expr) == True:
                    return True

        elif quantificator == IL_EXISTE_UN_UNIQUE:

            found = False

            for i in range(len(target_set)):
                exec(f"{target_var}={target_set}[{i}]")

                if eval(predicate_expr) == True:
                    if found == True:
                        return False

                    found = True

        return True
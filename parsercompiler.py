import ply.yacc as yacc
from lexercompiler import tokens
import lexercompiler
from QuadRuples import QuadRuple
from SymbolTable import Entry


class Parser:
    tokens = tokens

    def __init__(self):
        self.quadruples = []
        self.counter = 0
        self.counter2 = 0
        self.definedvar = []
        self.symbolTable = []
        self.meghdardehi = []

    def printSymbol(self):
        print("Symbol Table : ")
        for i in self.symbolTable:
            print(i[0], i[1])
            print(i[2], i[3])

    def goto_detect (self , myP ):
        if myP == 0 :
            return 0
        else:
            x = myP - 1
            print("=======================================")
            self.printQuadruples()
            print("=======================================")


            if x < len(self.quadruples) and x >= 0:
                del self.quadruples[x]
            else:
                print(" :( " , len(self.quadruples) , x-1  )
                if x-1 < len(self.quadruples) and x > 0:
                    del self.quadruples[x-1]

            print("=======================================")
            self.printQuadruples()
            print("=======================================")
            return 0

    def printQuadruples(self):
        print("QuadRuples : ")
        for i in self.quadruples:
            print("op : ", i.op, "arg1 : ", i.arg_one, "arg2 : ", i.arg_two, "result : ",i.result)
            print(i.result)

    def newTemp(self):
        self.counter += 1
        return 'Temp' + str(self.counter)

    def varType(self, newName):
        for i in self.symbolTable:
            if i[0] == newName:
                return i[1]

    def findTList(self, newName):
        for i in self.symbolTable:
            if i[0] == newName:
                print(i[2])
                return i[2]
        return []

    def findFList(self, newName):
        for i in self.symbolTable:
            if i[0] == newName:
                return i[3]
        return []

    def findType(self, name):
        for i in self.symbolTable:
            if i[0] == name:
                return i[1]
        return []

    def updateTList(self, newName , trueL):
        for i in self.symbolTable:
           if i[0] == newName:
                i[2] = trueL

    def updateFList(self, newName , falseL):
        for i in self.symbolTable:
            if i[0] == newName:
                i[3] = falseL

    def handle_goto(self):
        for q in self.quadruples:
            if q.result.replace(" ", "") == "goto":
                print("---------------")
                print("yaaaaaaaaaafffftaaaaaaaaaaammmm")
                print("---------------")
                q.result = q.result + str(len(self.quadruples))

    def p_R1(self, p):
        '''
        barnameh : PROGRAM ID tarifha
        '''
        print("Rule 1:  barnameh -> PROGRAM  ID tarifha")

    def p_R2(self, p):
        '''
        tarifha : tarifha tarif
                | tarif
        '''
        print("Rule 2: tarifha -> tarifha tarif | tarif ")

    def p_R3(self, p):
        '''
        tarif : STRUCT ID LBRACE tarifhayeMahalli RBRACE
              | STRUCT ID LBRACE RBRACE
              | jens tarifhayeMotheghayyerha SEMI
              |  jens ID LPAREN vorudiha RPAREN jomle
              | jens ID LPAREN RPAREN jomle
              | ID LPAREN vorudiha RPAREN jomle
              | ID LPAREN RPAREN jomle
        '''
        self.handle_goto()
        print("Rule 3:  STRUCT ID LBRACE tarifhayeMahalli RBRACE"
              "| STRUCT ID LBRACE RBRACE"
              "| jens tarifhayeMotheghayyerha SEMI"
              "|  jens ID LPAREN vorudiha RPAREN jomle"
              "| jens ID LPAREN RPAREN jomle"
              "| ID LPAREN vorudiha RPAREN jomle"
              "| ID LPAREN RPAREN jomle")

    def p_R5(self, p):
        '''
        tarifhayeMahalli : tarifhayeMahalli tarifeMoteghayyereMahdud
                         | tarifeMoteghayyereMahdud
        '''
        print("Rule 5:  tarifhayeMahalli -> tarifhayeMahalli tarifeMoteghayyereMahdud "
              "| tarifeMoteghayyereMahdud ")

    def p_R6(self, p):
        '''
        tarifeMoteghayyereMahdud : jenseMahdud tarifhayeMotheghayyerha SEMI
        '''
        p[0] = Entry()
        p[0].type = p[1].type
        for name in p[2]:
            if not int(name.lenght) <= 1:
                base = name.place
                for i in range(0,int(name.lenght)):
                    var = [base + str(i), p[1].type, name.true_list, name.false_list]
                    print(var)
                    self.symbolTable.append(var)
            else:
                var = [name.place, p[1].type, name.true_list, name.false_list]
                self.symbolTable.append(var)
        print("Rule 6:  tarifeMoteghayyereMahdud -> jenseMahdud tarifhayeMotheghayyerha SEMI")

    def p_R7(self, p):
        '''
        jenseMahdud : CONSTANT jens
                    | jens
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]
            # TODO
        print("Rule 7: jenseMahdud -> CONSTANT  jens | jens")

    def p_R8_0(self, p):
        '''
        jens : BOOL
        '''
        p[0] = Entry()
        p[0].type = 'bool'
        print("Rule 8_0 :  jens : BOOL ")

    def p_R8_1(self, p):
        '''
        jens : INT
        '''
        p[0] = Entry()
        p[0].type = 'arith'
        print("Rule 8:  jens : INT")

    def p_R8_2(self, p):
        '''
        jens : FLOAT
        '''
        p[0] = Entry()
        p[0].type = 'arith'
        print("Rule 8:  jens : FLOAT")

    def p_R8(self, p):
        '''
        jens : CHAR
        '''
        p[0] = Entry()
        p[0].type = 'char'
        print("Rule 8:  jens : CHAR  ")

    def p_R10(self, p):
        '''
        tarifhayeMotheghayyerha : tarifeMeghdareAvvalie
                                | tarifhayeMotheghayyerha COMMA tarifeMeghdareAvvalie
        '''
        # p[0] = Entry()
        if len(p) == 2:
            print("kkkkkk" , p[1].place )
            p[0] = []
            p[0].append(p[1])

        else:
            print(":|||||||||")
            p[1].append(p[3])
            p[0] = p[1]

        print("Rule 10:  tarifhayeMotheghayyerha -> tarifeMeghdareAvvalie"
              "| tarifhayeMotheghayyerha COMMA tarifeMeghdareAvvalie ")

    def p_R11(self, p):
        '''
        tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer
                                 | tarifeShenaseyeMoteghayyer EQUALS ebarateSade

        '''
        p[0] = p[1]
        if len(p) == 2 :
            self.meghdardehi.append([p[1].place, '1111111111111111'])

        if len(p) == 4:
            self.meghdardehi.append([p[1].place, p[3].place])
            p[0].true_list = p[3].true_list
            p[0].false_list = p[3].false_list
            p[0].detect = self.goto_detect(p[3].detect)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
            self.updateTList(p[0].place, p[0].true_list)
            self.updateFList(p[0].place, p[0].false_list)


        print("Rule 11:  tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer"
              "| tarifeShenaseyeMoteghayyer = ebarateSade ")

    def p_R12(self, p):
        '''
        tarifeShenaseyeMoteghayyer : ID
                                   | ID LBR ICONST RBR
        '''
        p[0] = Entry()
        p[0].place = p[1]
        print("bemir ;) " , len(p))
        if len(p) == 5:
            p[0].lenght = p[3]

        print("Rule 12:  tarifeShenaseyeMoteghayyer -> ID | ID [ ICONST ] ")

    def p_R15(self, p):
        '''
        vorudiha : vorudiha SEMI jensVorudiha
                 | jensVorudiha
        '''
        print("Rule 15:  vorudiha -> vorudiha ; jensVorudiha | jensVorudiha ")

    def p_R16(self, p):
        '''
        jensVorudiha : jens shenaseyeVorudiha
        '''
        print("Rule 16:  jensVorudiha -> jens shenaseyeVorudiha ")

    def p_R17(self, p):
        '''
        shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi
                          | shenaseyeVorudi
        '''
        print("Rule 17:  shenaseyeVorudiha -> shenaseyeVorudiha COMMA shenaseyeVorudi"
              "| shenaseyeVorudi ")

    def p_R18(self, p):
        '''shenaseyeVorudi : ID
                           | ID LBR RBR
        '''
        p[0] = Entry()
        p[0].place = p[1]
        print("Rule 42: shenaseyeVorudi ->  id | id [] ")

    def p_19_0(self, p):
        '''
        jomle : unmatched
              | matched
        '''

        p[0] = p[1]
        print ('to gaveeeee mani ')
        print("rule 19: jomle -> matched | unmatched ‌")

    def p_19_1(self, p):
        ''' matched : IF ebarateSade THEN M matched  Nelse M matched
                    | otherJomle
        '''
        p[0] = Entry()
        p[0].type = 'bool'
        if len (p) == 2 :
            p[0] = p[1]
        else:
            if p[2] is None :
                p[2].type = self.findType(p[2].place)
            if p[2].type == 'bool':
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[2].detect,
                      p[2].true_list, p[2].false_list)

                print("keeeeeeeeeeeeyliii khaaariiiiiiiiii" , p[4].quad , p[7].quad)
                self.printQuadruples()
                Entry.backpatch(p[2].true_list, self.quadruples, p[4].quad)
                Entry.backpatch(p[2].false_list, self.quadruples, p[7].quad)
                p[0].next_list = p[5].next_list + p[6].next_list + p[8].next_list
                self.printQuadruples()
            else:
                pass
            self.handle_goto()

        print("rule 19_1: matched : IF ebarateSade THEN matched ELSE matched | otherJomle")

    def p_19_2(self, p):
        ''' unmatched : IF ebarateSade THEN M jomle
                      | IF ebarateSade THEN M matched Nelse M unmatched
        '''
        p[0] = Entry()
        if len(p) == 6 :
            Entry.backpatch(p[2].true_list, self.quadruples, p[4].quad)
            p[0].next_list = p[2].false_list + p[5].next_list
            self.handle_goto()
        else:
            if p[2] is None:
                p[2].type = self.findType(p[2].place)
            if p[2].type == 'bool':

                Entry.backpatch(p[2].true_list, self.quadruples, p[4].quad)
                Entry.backpatch(p[2].false_list, self.quadruples, p[7].quad)
                p[0].next_list = p[5].next_list + p[6].next_list + p[8].next_list
                self.printQuadruples()
                print("rule 19_2: unmatched : IF ebarateSade THEN jomle |"
                 " IF ebarateSade THEN matched ELSE unmatched")
                self.handle_goto()

    def p_Nelse(self, p):
        '''
        Nelse : ELSE
        '''
        p[0] = Entry()
        p[0].next_list.append(len(self.quadruples))
        self.quadruples.append(QuadRuple('', '', '', 'goto'))

    def p_N(self, p):
        '''
        N :
        '''
        print('saaaaaaaaaaaaaaaaaaaaaaaaaaaalllllllllllllllllllllllllllllllllllllaaaaaaaaaaaaaaaaaaam')
        p[0] = Entry()
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        p[0].quad = (len(self.quadruples))

    def p_R20(self, p):
        '''otherJomle : LBRACE tarifhayeMahalli jomleha RBRACE
                        | LBRACE tarifhayeMahalli RBRACE
                        | ebarat SEMI
                        | SEMI
                        | jomleyeTekrar
                        | RETURN SEMI
                        | RETURN ebarat SEMI
                        | BREAK SEMI
                        '''
        p[0] = Entry()
        print("Rule 20:  jomle -> LBRACE tarifhayeMahalli jomleha RBRACE"
              "| LBRACE tarifhayeMahalli RBRACE"
              "| ebarat SEMI"
              "| SEMI"
              "| KEY LPAREN ebarateSade RPAREN onsoreHalat onsorePishfarz END"
              "| KEY LPAREN ebarateSade RPAREN onsoreHalat END"
              "| WHILE LPAREN ebarateSade RPAREN jomle"
              "| RETURN SEMI"
              "| RETURN ebarat SEMI"
              "| BREAK SEMI")



    def p_R20_1(self, p):
        '''jomleyeTekrar : WHILE M ebarateSade M jomle  '''

        p[0] = Entry()
        if p[3].true_list is None:
            p[3].true_list = self.findTList(p[3].place)

        # print (p[7].next_list , p[4].next_list , 'ablahhhhhhhhhhhhh')
        Entry.backpatch(p[5].next_list, self.quadruples, p[3].quad)
        Entry.backpatch(p[3].true_list, self.quadruples, p[4].quad)
        p[0].next_list = p[3].false_list
        self.quadruples.append(QuadRuple('', '', '', 'goto' + str(p[3].quad )))

    def p_R20_2(self, p):
        '''otherJomle : KEY LPAREN ebarateSade RPAREN onsoreHalat END
                        '''
        p[0] = Entry()
        c = 0
        for q in self.quadruples:
            if q.op == '!=' and q.arg_one == 'x' and q.result[:4] == 'goto' :

                if not self.quadruples[c+2].op == "=":
                    print(" ================================================")
                    print(" :) ")
                    print(" ================================================")
                    self.quadruples[c+1] = QuadRuple('', '', '', 'goto' + str(c+2))
                    break
            c += 1
        self.handle_goto()
        print("Rule 20_2 :  otherJomle -> KEY LPAREN ebarateSade RPAREN onsoreHalat END ")

    def p_R20_3 (self,p):
        '''otherJomle : KEY LPAREN ebarateSade RPAREN onsoreHalat onsorePishfarz END'''
        print("Rule 20_3 :  otherJomle -> KEY LPAREN ebarateSade RPAREN onsoreHalat onsorePishfarz END ")

    def p_R21(self, p):
        '''
        jomleha : jomleha jomle
                | jomle
        '''

        print("Rule 21:  jomleha -> jomleha jomle")

    def p_R24(self, p):
        '''onsoreHalat : stateKW2
                       | onsoreHalat stateKW2
        '''

        # self.quadruples.append(QuadRuple('', '', '', 'goto'))


        print("Rule 24:  onsoreHalat ->  state  ADAD: jomle ;"
              "| onsoreHalat  state  ADAD : jomle ; ")

    where = 0

    def p_R24_0 (self, p):
        '''stateKW1 : STATE ICONST COLON
        '''
        p[0] = Entry()
        p[0].IDdetect = False
        p[0].true_list.append(len(self.quadruples))
        p[0].false_list.append(len(self.quadruples) + 1)
        self.quadruples.append(QuadRuple('!=', 'x', str(p[2]), 'goto' ))
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        self.where = [len(self.quadruples) - 2]
        self.printQuadruples()

        p[0].type = 'bool'
        print("Rule 24_0 : stateKW1 -> STATE ICONST COLON")


    def p_R24_1 (self, p):
        '''stateKW2 : stateKW1 jomle N SEMI
        '''
        # s elf.quadruples.append(QuadRuple('', '', '', 'goto'))
        Entry.backpatch(self.where, self.quadruples, p[3].quad )
        print("Rule 24_1 : stateKW2 -> stateKW1 jomle N SEMI")

    def p_R25(self, p):
        'onsorePishfarz : DEFAULT COLON jomle SEMI'
        # TODO after a while :D
        print("Rule 25:  onsorePishfarz -> default : jomle ; ")

    def p_R29_1(self, p):
        '''ebarat : taghirpazir EQUALS ebarat
        '''
        p[0] = Entry()
        p[0].place = p[1].place
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
              p[0].true_list, p[0].false_list)

        p[0].detect = self.goto_detect(p[3].detect)
        print ('---------------',p[3].place,'--------------')
        self.quadruples.append(QuadRuple('=', p[3].place, '', p[1].place))
        self.updateTList(p[0].place, p[3].true_list)
        self.updateFList(p[0].place, p[3].false_list)
        self.printQuadruples()
        print('salam salam hale bozghale ')
        print("Rule 29:  ebarat -> taghirpazir = ebarat")

    def p_R29_2(self, p):
        '''ebarat :  taghirpazir PLUSEQUAL ebarat
        '''
        p[0] = Entry()
        self.quadruples.append(QuadRuple('+', p[1].place, p[3].place, p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir += ebarat")

    def p_R29_3(self, p):
        '''ebarat :  taghirpazir MINUSEQUAL ebarat
        '''
        p[0] = Entry()
        self.quadruples.append(QuadRuple('-', p[1].place, p[3].place, p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir -= ebarat")

    def p_R29_4(self, p):
        '''ebarat :  taghirpazir TIMESEQUAL ebarat
        '''
        p[0] = Entry()
        self.quadruples.append(QuadRuple('*', p[1].place, p[3].place, p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir *= ebarat")

    def p_R29_5(self, p):
        '''ebarat :  taghirpazir DIVEQUAL ebarat
        '''
        p[0] = Entry()
        self.quadruples.append(QuadRuple('/', p[1].place, p[3].place, p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir /= ebarat")

    def p_R29_6(self, p):
        '''ebarat :  taghirpazir PLUSPLUS
        '''
        p[0] = Entry()
        p[0] = p[1]
        self.quadruples.append(QuadRuple('+', p[1].place, '1', p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir ++ ")

    def p_R29_7(self, p):
        '''ebarat :  taghirpazir MINUSMINUS
        '''
        p[0] = Entry()
        p[0] = p[1]
        self.quadruples.append(QuadRuple('-', p[1].place, '1', p[1].place))
        print("Rule 29:  ebarat ->  taghirpazir -- ")

    def p_R29_8(self, p):
        '''ebarat :  ebarateSade
        '''
        p[0] = p[1]

        print("Rule 29:  ebarat -> ebarateSade ")

    def p_R30(self, p):
        '''

        ebarateSade :  ebarateSade3
                       | ebarateRiaziManteghi2 amalgareRiazi2 ebarateRiaziManteghi2
                       | ebarateRiaziManteghi1 amalgareRiazi1 ebarateRiaziManteghi1
                       | ebaratRabetei
        '''

        if len(p) == 2:
            p[0] = p[1]

            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
        else:
            p[1].detect = self.goto_detect(p[1].detect)
            p[3].detect = self.goto_detect(p[3].detect)

            p[0] = Entry()
            p[0].place = self.newTemp()
            p[0].type = 'arith'

            p[1].false_list = self.findFList(p[1].place)
            p[3].false_list = self.findFList(p[3].place)
            p[1].true_list = self.findTList(p[1].place)
            p[3].true_list = self.findTList(p[3].place)

            if p[1].type == 'char':
                print("heeelooooo  jooonemadaret ")
                p[1].type = 'arith'
                x = p[1].place
                p[1].place = str(ord(x[1]))
            if p[3].type == 'char':
                print("heeelooooo  jooonemadaret ")
                p[3].type = 'arith'
                x = p[3].place
                p[3].place = str(ord(x[1]))
            if p[3].type is None:
                p[3].type = self.varType(p[3].place)
            if p[1].type is None:
                p[1].type = self.varType(p[1].place)
            if p[1].type == 'arith' and p[3].type == 'arith':
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, p[3].place, p[0].place))
            elif p[1].type == 'arith' and p[3].type == 'bool':
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '0', p[0].place))
            elif p[1].type == 'bool' and p[3].type == 'arith':
                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '0', p[0].place))

            elif p[3].type == 'bool' and p[1].type == 'bool':
                temp = self.newTemp()
                print("ahmagh : ", p[1].true_list, p[1].false_list, p[3].true_list, p[3].false_list)
                self.printQuadruples()
                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '1', '', temp))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '0', '', temp))
                print(p[3].place, 'tu ruhe in zendegiiiiiiiiiiiii')
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(p[3].true_list[0])))
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, temp, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', temp, '', p[0].place))
            else:
                print(' shit :| ')

            print("keeeeeeeeeeeeyliii khaaariiiiiiiiii")
            self.printQuadruples()



        print("Rule 30: ebarateSade ->  ebarateSade3 "
              "| ebarateRiaziManteghi2 amalgareRiazi2 ebarateRiaziManteghi2"
              "| ebarateRiaziManteghi1 amalgareRiazi1 ebarateRiaziManteghi1")

    def p_30_0_0(self, p):
        '''
            ebarateSade0 : amalgareYegani ebarateYegani
        '''
        if p[1].place == '-':
            p[1].place = p[1].place + p[2].place
            p[1].type = 'arith'
            p[0] = p[1]

            # TODO ssssaaaaaaaaggggg
        print("Rule 30_0_0: ebarateSade0 ->  amalgareYegani ebarateYegani ")

    def p_30_0_1(self, p):
        '''
            ebarateSade0 : ID
        '''
        p[0] = Entry()
        p[0].place = p[1]
        p[0].true_list = self.findTList(p[0].place)
        p[0].false_list = self.findFList(p[0].place)
        p[0].type = self.findType(p[0].place)
        p[0].IDdetect = True
        p[0].detect = len(self.quadruples) + 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect, p[0].true_list,
              p[0].false_list)
        self.quadruples.append(QuadRuple('', '', '', 'goto'))

        # self.updateTList(p[0].place, p[0].true_list)
        # self.updateFList(p[0].place, p[0].false_list)

        print("Rule 30_0_1: ebarateSade0 ->  ID ")

    def p_30_0_2(self, p):
        '''
            ebarateSade0 : taghirpazir LBR ebarat RBR
        '''
        p[0] = Entry()
        p[0].place = p[1].place + str(p[3].place)
        p[0].true_list = self.findTList(p[0].place)
        p[0].false_list = self.findFList(p[0].place)
        p[0].type = self.findType(p[0].place)
        p[0].detect = len(self.quadruples) + 1
        p[0].IDdetect = True
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect, p[0].true_list,
              p[0].false_list)
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        print("Rule 30_0_2: ebarateSade0 ->  taghirpazir LBR ebarat RBR ")

    def p_30_0_3(self, p):
        '''
            ebarateSade0 : taghirpazir DOT ID
        '''
        print("Rule 30_0_3: ebarateSade0 ->  taghirpazir DOT ID ")

    def p_30_0_4(self, p):
        '''
            ebarateSade0 : LPAREN ebarat RPAREN
        '''
        p[0] = p[2]
        if p[2].IDdetect == True :
            print("khaaaaaaaheeesh mikonam dorost bash :( ")
            place = '1'
            detect = len(self.quadruples) + 1
            true_list = [len(self.quadruples)]
            self.quadruples.append(QuadRuple('', '', '', 'goto'))
            print("Rule 43 : meghdaresabet -> TRUE ")

            p[0] = Entry()
            p[0].IDdetect = False
            p[2].detect = self.goto_detect(p[2].detect)
            detect = self.goto_detect(detect)
            p[0].true_list.append(len(self.quadruples))
            p[0].false_list.append(len(self.quadruples) + 1)
            self.quadruples.append(QuadRuple('==', p[2].place, place, 'goto'))
            self.quadruples.append(QuadRuple('', '', '', 'goto'))
            p[0].type = 'bool'
        print("Rule 30_0_4 : ebarateSade0 ->  LPAREN ebarat RPAREN ")

    def p_30_0_5(self, p):
        '''
            ebarateSade0 : sedaZadan
        '''
        # TODO after a while :D
        print("Rule 30_0: ebarateSade0 ->  sedaZadan ")

    def p_30_6(self, p):
        '''
            ebarateSade0 : meghdaresabet
        '''
        p[0] = p[1]
        p[0].IDdetect = False
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  " , p[0].detect , p[0].true_list , p[0].false_list)
        print("Rule 30_0: ebarateSade0 ->  meghdaresabet")

    def p_R30_1(self, p):
        '''
        ebarateSade1 :  NOT ebarateSade1
                       | ebarateSade0
        '''
        if len(p) == 2:
            p[0] = p[1]
            p[0].IDdetect = True and p[1].IDdetect
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
        else:
            p[0] = p[1]
            p[0].IDdetect = False
            p[0].true_list = p[1].false_list
            p[0].false_list = p[1].true_list
            self.updateTList(p[0].place, p[0].true_list)
            self.updateFList(p[0].place, p[0].false_list)
        print("Rule 30_1: ebarateSade1 -> | NOT ebarateSade1| ebarateSade0 ")

    def p_R30_2(self, p):
        '''
        ebarateSade2 :  ebarateSade2 AND M ebarateSade2
                       | ebarateSade1
        '''
        if len(p) == 2:
            p[0] = p[1]
            p[0].IDdetect = True and p[1].IDdetect
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
        else:
            # p[1].detect = self.goto_detect(p[1].detect)
            # p[3].detect = self.goto_detect(p[3].detect)
            p[0] = Entry()
            p[0].place = self.newTemp()
            p[0].type = 'bool'
            p[0].IDdetect = False
            nakonim = False
            if p[1].false_list == [] :
                p[1].false_list = self.findFList(p[1].place)
                if not p[1].false_list == []:
                    nakonim = True
            if p[1].true_list == [] :
                p[1].true_list = self.findTList(p[1].place)
                if not p[1].true_list == []:
                    nakonim = True
            if p[4].false_list == [] :
                p[4].false_list = self.findFList(p[4].place)
                if not  p[4].false_list == []:
                    nakonim = True
            if p[4].true_list == []:
                p[4].true_list = self.findTList(p[4].place)
                if not p[4].true_list == []:
                    nakonim = True

            if p[4].type == None:
                p[4].type = self.varType(p[4].place)

            if p[1].type == None:
                p[1].type = self.varType(p[1].place)

            if p[4].type == None:
                p[4].type = self.varType(p[4].place)
            if p[1].type == None:
                p[1].type = self.varType(p[1].place)

            if p[1].type == 'bool' and p[4].type == 'bool':
                print ('saaaaalaaaaaaaaaaaaaaaaaaaaam')
                # if nakonim:
                #     self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                #     self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                #     self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                #     self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #     self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                #     self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[1].true_list, self.quadruples, p[3].quad)
                # if nakonim:
                #     self.quadruples.append(QuadRuple('=', '0', '', p[0].place))

                p[0].true_list = p[4].true_list
                p[0].false_list = p[1].false_list + p[4].false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)



            elif p[1].type == 'arith' and p[4].type == 'bool':
                t = Entry()
                t.true_list.append(len(self.quadruples))
                t.false_list.append(len(self.quadruples) + 1)
                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(t.true_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = p[4].true_list
                p[0].false_list = p[4].false_list + t.false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)


            elif p[1].type == 'bool' and p[4].type == 'arith':
                t = Entry()
                t.true_list.append(len(self.quadruples))
                t.false_list.append(len(self.quadruples) + 1)
                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[1].true_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = t.true_list
                p[0].false_list = p[1].false_list + t.false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)


            elif p[1].type == 'arith' and p[4].type == 'arith':

                if int ( p[1].place ) > 0 :
                    p[1].place = '1'
                else :
                    p[1].place = '0'

                if int(p[4].place) > 0:
                    p[4].place = '1'
                else:
                    p[4].place = '0'

                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[1].true_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))

                p[0].true_list = p[4].true_list
                p[0].false_list = p[1].false_list + p[4].false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)

                # t = Entry()
                # t.true_list.append(len(self.quadruples))
                # t.false_list.append(len(self.quadruples) + 1)
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                # t1 = Entry()
                # t1.true_list.append(len(self.quadruples))
                # t1.false_list.append(len(self.quadruples) + 1)
                # self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                # Entry.backpatch(t.true_list, self.quadruples, p[3].quad)
                # self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                # p[0].true_list = t1.true_list
                # p[0].false_list = t.false_list + t1.false_list
                # self.updateTList(p[0].place, p[0].true_list)
                # self.updateFList(p[0].place, p[0].false_list)

        print("Rule 30_2: ebarateSade2 ->  ebarateSade2 AND ebarateSade2 | ebarateSade1 ")

    def p_R30_3(self, p):
        '''
        ebarateSade2 :  ebarateSade2 ANDTHEN ebarateSade2
        '''
        # TODO what we should DO ? :(
        print("Rule 30_2: ebarateSade2 -> ebarateSade2 ANDTHEN ebarateSade2 ")

    def p_R30_4(self, p):
        '''
        ebarateSade3 :  ebarateSade3 OR M ebarateSade3
                       | ebarateSade2
        '''
        if len(p) == 2:
            p[0] = p[1]
            p[0].IDdetect = True and p[1].IDdetect
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
        else:
            # p[1].detect = self.goto_detect(p[1].detect)
            # p[3].detect = self.goto_detect(p[3].detect)
            p[0] = Entry()
            p[0].place = self.newTemp()
            p[0].type = 'bool'
            p[0].IDdetect = False
            nakonim = False
            if p[1].false_list == [] :
                p[1].false_list = self.findFList(p[1].place)
                if not p[1].false_list == []:
                    nakonim = True
            if p[1].true_list == [] :
                p[1].true_list = self.findTList(p[1].place)
                if not p[1].true_list == []:
                    nakonim = True
            if p[4].false_list == [] :
                p[4].false_list = self.findFList(p[4].place)
                if not  p[4].false_list == []:
                    nakonim = True
            if p[4].true_list == []:
                p[4].true_list = self.findTList(p[4].place)
                if not p[4].true_list == []:
                    nakonim = True

            if p[4].type == None:
                p[4].type = self.varType(p[4].place)

            if p[1].type == None:
                p[1].type = self.varType(p[1].place)

            if p[1].type == 'bool' and p[4].type == 'bool':
                # print('://///////////////////////////////////////////////////////////')
                # if nakonim:
                # self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                # self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[1].false_list, self.quadruples, p[3].quad)
                # if nakonim:
                # self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = p[1].true_list + p[4].true_list
                p[0].false_list = p[4].false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)

            elif p[1].type == 'arith' and p[4].type == 'bool':
                t = Entry()
                t.true_list.append(len(self.quadruples))
                t.false_list.append(len(self.quadruples) + 1)
                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[4].false_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = p[4].true_list + t.true_list
                p[0].false_list = t.false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)

                p[0].type = 'bool'

            elif p[1].type == 'bool' and p[4].type == 'arith':
                t = Entry()
                t.true_list.append(len(self.quadruples))
                t.false_list.append(len(self.quadruples) + 1)
                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                Entry.backpatch(p[1].false_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = p[1].true_list + t.true_list
                p[0].false_list = t.false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)

                p[0].type = 'bool'

            elif p[1].type == 'arith' and p[4].type == 'arith':
                if int ( p[1].place ) > 0 :
                    p[1].place = '1'
                else :
                    p[1].place = '0'

                if int(p[4].place) > 0:
                    p[4].place = '1'
                else:
                    p[4].place = '0'

                self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto' + str(len(self.quadruples) + 3)))
                # p[1].false_list.append(str(len(self.quadruples) + 3))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + str(len(self.quadruples) + 2)))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))
                self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto'))

                Entry.backpatch(p[1].false_list, self.quadruples, p[3].quad)
                self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                p[0].true_list = p[1].true_list + p[4].true_list
                p[0].false_list = p[4].false_list
                self.updateTList(p[0].place, p[0].true_list)
                self.updateFList(p[0].place, p[0].false_list)

                # t1 = Entry()
                # t1.true_list.append(len(self.quadruples))
                # t1.false_list.append(len(self.quadruples) + 1)
                # self.quadruples.append(QuadRuple('>', p[1].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                # t2 = Entry()
                # t2.true_list.append(len(self.quadruples))
                # t2.false_list.append(len(self.quadruples) + 1)
                # self.quadruples.append(QuadRuple('>', p[4].place, '0', 'goto' + (str(len(self.quadruples) + 2 ))))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                # self.quadruples.append(QuadRuple('=', '1', '', p[0].place))
                # self.quadruples.append(QuadRuple('', '', '', 'goto'))
                #
                # Entry.backpatch(t1.false_list, self.quadruples, p[3].quad)
                # self.quadruples.append(QuadRuple('=', '0', '', p[0].place))
                #
                # p[0].true_list = t1.true_list + t2.true_list
                # p[0].false_list = t2.false_list
                # self.updateTList(p[0].place, p[0].true_list)
                # self.updateFList(p[0].place, p[0].false_list)

                p[0].type = 'bool'

        print("Rule 30_3: ebarateSade3 ->  ebarateSade3 OR ebarateSade3 | ebarateSade2 ")

    def p_M(self, p):
        '''
        M :
        '''
        print("MMMMMMMMMMMMM")
        p[0] = Entry()
        p[0].quad = len(self.quadruples)
        # print("empty rule")

    def p_R30_5(self, p):
        '''
        ebarateSade3 :  ebarateSade3 ORELSE ebarateSade3
        '''
        # TODO what we should DO ? :(
        print("Rule 30_3: ebarateSade3 ->  ebarateSade3 ORELSE ebarateSade3 ")

    def p_R31(self, p):
        ''' ebaratRabetei : ebarateRiaziManteghi1 amalgareRabetei ebarateRiaziManteghi1
                            | ebarateRiaziManteghi2 amalgareRabetei ebarateRiaziManteghi2
        '''

        p[0] = Entry()
        p[0].IDdetect = False
        p[1].detect = self.goto_detect(p[1].detect)
        p[3].detect  = self.goto_detect(p[3].detect)
        p[0].true_list.append(len(self.quadruples))
        p[0].false_list.append(len(self.quadruples) + 1)
        self.quadruples.append(QuadRuple(p[2].place, p[1].place, p[3].place, 'goto'))
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        p[0].type = 'bool'

        print("Rule 31_3: ebarateRiaziManteghi1 amalgareRabetei ebarateRiaziManteghi1 "
              "| ebarateRiaziManteghi2 amalgareRabetei ebarateRiaziManteghi2 ")

    def p_R32_0(self, p):
        '''amalgareRabetei : LT '''
        p[0] = Entry()
        p[0].place = '<'
        print("Rule 32_0:  amalgareRabetei -> < ")

    def p_R32_1(self, p):
        '''amalgareRabetei : LE '''
        p[0] = Entry()
        p[0].place = '<='
        print("Rule 32:  amalgareRabetei ->  <= ")

    def p_R32_2(self, p):
        '''amalgareRabetei : GE '''
        p[0] = Entry()
        p[0].place = '>='
        print("Rule 32:  amalgareRabetei -> >= ")

    def p_R32_3(self, p):
        '''amalgareRabetei : EQ '''
        p[0] = Entry()
        p[0].place = '=='
        print("Rule 32:  amalgareRabetei -> == ")

    def p_R32_4(self, p):
        '''amalgareRabetei : GT'''
        p[0] = Entry()
        p[0].place = '>'
        print("Rule 32:  amalgareRabetei -> >")

    def p_R33_1(self, p):
        '''ebarateRiaziManteghi1 : ebarateSade0
                                | ebarateRiaziManteghi1 amalgareRiazi1 ebarateRiaziManteghi1 '''
        if len(p) == 2:
            p[0] = p[1]
            p[0].IDdetect = True and p[1].IDdetect
        else:

            p[1].detect = self.goto_detect(p[1].detect)
            p[3].detect = self.goto_detect(p[3].detect)
            p[0] = Entry()
            p[0].IDdetect = False
            p[0].place = self.newTemp()
            p[0].type = 'arith'
            p[1].false_list = self.findFList(p[1].place)
            p[3].false_list = self.findFList(p[3].place)
            p[1].true_list = self.findTList(p[1].place)
            p[3].true_list = self.findTList(p[3].place)

            if p[1].type == 'char':
                print("heeelooooo  jooonemadaret ")
                p[1].type = 'arith'
                x = p[1].place
                p[1].place = str(ord(x[0]))
            if p[3].type == 'char':
                print("heeelooooo  jooonemadaret ")
                p[3].type = 'arith'
                x = p[3].place
                p[3].place = str(ord(x[2]))
            if p[3].type == None:
                p[3].type = self.varType(p[3].place)
            if p[1].type == None:
                p[1].type = self.varType(p[1].place)

            if p[1].type == 'arith' and p[3].type == 'arith':
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, p[3].place, p[0].place))
            elif p[1].type == 'arith' and p[3].type == 'bool':
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '0', p[0].place))
            elif p[1].type == 'bool' and p[3].type == 'arith':
                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '0', p[0].place))
            elif p[3].type == 'bool' and p[1].type == 'bool':
                temp = self.newTemp()

                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '1', '', temp))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '0', '', temp))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(p[3].true_list[0])))
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, temp, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', temp, '', p[0].place))
            else:
                print(' shit :| ')
        print(
            "Rule 33_1: ebarateRiaziManteghi1 -> ebarateSade0 "
            " | ebarateRiaziManteghi1 amalgareRiazi1 ebarateRiaziManteghi1 ")

    def p_R33_2(self, p):
        '''ebarateRiaziManteghi2 : ebarateRiaziManteghi1
                                | ebarateRiaziManteghi2 amalgareRiazi2 ebarateRiaziManteghi2
        '''
        if len(p) == 2:
            p[0] = p[1]
            p[0].IDdetect = True and p[1].IDdetect
        else:
            p[1].detect = self.goto_detect(p[1].detect)
            p[3].detect = self.goto_detect(p[3].detect)
            p[0] = Entry()
            p[0].IDdetect = False
            p[0].place = self.newTemp()
            p[1].false_list = self.findFList(p[1].place)
            p[3].false_list = self.findFList(p[3].place)
            p[1].true_list = self.findTList(p[1].place)
            p[3].true_list = self.findTList(p[3].place)
            if p[1].type == 'char':
                p[1].type = 'arith'
                print("heeelooooo  jooonemadaret ")
                x = p[1].place
                p[1].place = str(ord(x[1]))
            if p[3].type == 'char':
                print("heeelooooo  jooonemadaret ")
                p[3].type = 'arith'
                x = p[3].place
                p[3].place = str(ord(x[1]))
            if p[3].type == None:
                p[3].type = self.varType(p[3].place)
            if p[1].type == None:
                p[1].type = self.varType(p[1].place)

            if p[1].type == 'arith' and p[3].type == 'arith':
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, p[3].place, p[0].place))
            elif p[1].type == 'arith' and p[3].type == 'bool':
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[1].place, '0', p[0].place))
            elif p[1].type == 'bool' and p[3].type == 'arith':
                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, p[3].place, '0', p[0].place))
            elif p[3].type == 'bool' and p[1].type == 'bool':
                temp = self.newTemp()
                Entry.backpatch(p[1].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '1', '', temp))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[1].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', '0', '', temp))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(p[3].true_list[0])))
                Entry.backpatch(p[3].true_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple(p[2].place, temp, '1', p[0].place))
                self.quadruples.append(QuadRuple('', '', '', 'goto ' + str(len(self.quadruples) + 2)))
                Entry.backpatch(p[3].false_list, self.quadruples, len(self.quadruples))
                self.quadruples.append(QuadRuple('', temp, '', p[0].place))
            else:
                print(' shit :| ')

        print("Rule 33_2: ebarateRiaziManteghi2 -> ebarateRiaziManteghi1 "
              " | ebarateRiaziManteghi2 amalgareRiazi2 ebarateRiaziManteghi2 ")

    def p_R34_0(self, p):
        '''
        amalgareRiazi1 : TIMES
        '''
        p[0] = Entry()
        p[0].place = '*'
        print("Rule 34_0:  amalgareRiazi1 -> * ")

    def p_R34_1(self, p):
        '''
        amalgareRiazi1 : DIVIDE
        '''
        p[0] = Entry()
        p[0].place = '/'
        print("Rule 34_1:  amalgareRiazi1 ->  / ")

    def p_R34_2(self, p):
        '''
        amalgareRiazi1 : MOD
        '''
        p[0] = Entry()
        p[0].place = '%'
        print("Rule 34_2:  amalgareRiazi1 ->  % ")

    def p_R34_3(self, p):
        '''
        amalgareRiazi2 : PLUS
        '''
        p[0] = Entry()
        p[0].place = '+'
        print("Rule 34_3 : amalgareRiazi -> + ")

    def p_R34_4(self, p):
        '''
        amalgareRiazi2 : MINUS
        '''
        p[0] = Entry()
        p[0].place = '-'
        print("Rule 34_4 : amalgareRiazi -> - ")

    def p_R35_0(self, p):
        '''
        ebarateYegani : amalgareYegani ebarateYegani
        '''
        if p[1].place == '-':
            p[1].place = p[1].place + p[2].place
            p[1].type = 'arith'
            p[0] = p[1]
            # TODO ssssaaaaaaaaggggg
        print("Rule 35_0 : ebarateYegani -> amalgareYegani ebarateYegani")

    def p_R35_1(self, p):
        '''
        ebarateYegani : ID
        '''
        p[0] = Entry()
        p[0].IDdetect = True
        p[0].place = p[1]
        print("Rule 35_1: ebarateYegani -> ID ")

    def p_R35_2(self, p):
        '''
        ebarateYegani : taghirpazir LBR ebarat RBR
        '''
        print("Rule 35_2: ebarateYegani -> taghirpazir LBR ebarat RBR ")

    def p_R35_3(self, p):
        '''
        ebarateYegani : taghirpazir DOT ID
        '''
        # TODO after a while :D
        print("Rule 35_3: ebarateYegani ->  taghirpazir DOT ID ")

    def p_R35_4(self, p):
        '''
        ebarateYegani : taghirnapazir
        '''
        p[0] = p[1]
        print("Rule 35_4: ebarateYegani -> taghirnapazir")

    def p_R36_0(self, p):
        '''
        amalgareYegani : MINUS
        '''
        p[0] = Entry()
        p[0].place = '-'
        print("Rule 36: amalgareYegani -> - ")

    def p_R36_1(self, p):
        '''
        amalgareYegani : TIMES

        '''
        p[0] = Entry()
        p[0].place = '*'
        print("Rule 36: amalgareYegani ->  *  ")

    def p_R36_2(self, p):
        '''
        amalgareYegani :  QM
        '''
        p[0] = Entry()
        p[0].place = '?'
        print("Rule 36: amalgareYegani ->  ? ")

    def p_R38_0(self, p):
        '''
        taghirpazir :  ID
        '''
        p[0] = Entry()
        p[0].place = p[1]
        p[0].IDdetect = True
        print("Rule 38_0:  taghirpazir -> ID")

    def p_R38_1(self, p):
        '''
        taghirpazir : taghirpazir LBR ebarat RBR
        '''
        p[0] = Entry()
        p[0].place = p[1].place + str(p[3].place)
        p[0].true_list = self.findTList(p[0].place)
        p[0].false_list = self.findFList(p[0].place)
        p[0].type = self.findType(p[0].place)
        p[0].detect = len(self.quadruples) + 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect, p[0].true_list,
              p[0].false_list)
        # self.quadruples.append(QuadRuple('', '', '', 'goto'))
        print("Rule 38_1:  taghirpazir -> taghirpazir LBR ebarat RBR ")

    def p_R38_2(self, p):
        '''
        taghirpazir :  taghirpazir DOT ID
        '''
        # TODO after a while :D
        print("Rule 38_2:  taghirpazir -> taghirpazir DOT ID ")

    def p_R39_0(self, p):
        '''
        taghirnapazir : LPAREN ebarat RPAREN
        '''
        p[0] = p[2]
        print("Rule 39:  taghirnapazir -> LPAREN ebarat RPAREN ")

    def p_R39_1(self, p):
        '''
        taghirnapazir : sedaZadan
        '''
        # TODO after a while :D
        print("Rule 39_1:  taghirnapazir -> sedaZadan ")

    def p_R39_2(self, p):
        '''
        taghirnapazir : meghdaresabet
        '''
        p[0] = p[1]
        p[0].IDdetect = False
        print("Rule 39_2:  taghirnapazir -> meghdaresabet")

    def p_R40(self, p):
        '''
        sedaZadan : ID LPAREN bordareVorudiha RPAREN
                  | ID LPAREN RPAREN
        '''
        # TODO after a while :D

        print("Rule 40:  sedaZadan -> ID LPAREN bordareVorudiha RPAREN | ID LPAREN RPAREN ")

    def p_R42(self, p):
        '''
        bordareVorudiha : bordareVorudiha COMMA ebarat
                         | ebarat
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[3]
        print("Rule 42: bordareVorudiha -> bordareVorudiha COMMA ebarat | ebarat ")

    def p_R43(self, p):
        '''
        meghdaresabet : ICONST
        '''
        p[0] = Entry()
        p[0].place = p[1]
        num = int(p[1])
        if num > 0 :
            p[0].detect = len(self.quadruples) + 1
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
            p[0].type = 'bool'
            p[0].true_list = [len(self.quadruples)]
        else:
            p[0].detect = len(self.quadruples) + 1
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ", p[0].detect,
                  p[0].true_list, p[0].false_list)
            p[0].type = 'bool'
            p[0].false_list = [len(self.quadruples)]
        self.printQuadruples()
        p[0].type = 'arith'
        print("Rule 43 : meghdaresabet -> ICONST ")

    def p_R44(self, p):
        '''
        meghdaresabet : CCONST
        '''
        print("heeeeeeeeeeey : ", p[1])
        p[0] = Entry()
        p[0].place = p[1]
        p[0].type = 'char'
        print("Rule 44 : meghdaresabet -> CCONST ")

    def p_R45(self, p):
        '''
        meghdaresabet : TRUE
        '''
        p[0] = Entry()
        p[0].place = p[1]
        p[0].detect = len(self.quadruples) + 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  " , p[0].detect , p[0].true_list , p[0].false_list)
        p[0].type = 'bool'
        p[0].true_list = [len(self.quadruples)]
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        # var = [p[0].place,p[0].type, p[0].true_list, p[0].false_list]
        # self.symbolTable.append(var)
        print("Rule 43 : meghdaresabet -> TRUE ")

    def p_R46(self, p):
        '''
        meghdaresabet : FALSE
        '''
        p[0] = Entry()
        p[0].place = p[1]
        p[0].detect = len(self.quadruples) + 1
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  " , p[0].detect , p[0].true_list , p[0].false_list)
        p[0].type = 'bool'
        p[0].false_list = [len(self.quadruples)]
        self.quadruples.append(QuadRuple('', '', '', 'goto'))
        # var = [p[0].place, p[0].type, p[0].true_list, p[0].false_list]
        # self.symbolTable.append(var)
        print("Rule 43 : meghdaresabet -> FALSE ")

    def p_error(self, t):
        print("what the fuck ... whoa whoa jesus christ", t)

    def build(self, **kwargs):
        '''
        build the parser
        '''
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

    def var_handler(self, word):
        for v in self.definedvar:
            if v[0] == word:
                return v[1]
        name = 'var' + str(self.counter2)
        newv = [word, name]
        self.definedvar.append(newv)
        self.counter2 += 1
        return name

    def numconverter(self, num):
        try:
            return {
                '\u06f0': '0',
                '\u06f1': '1',
                '\u06f2': '2',
                '\u06f3': '3',
                '\u06f4': '4',
                '\u06f5': '5',
                '\u06f6': '6',
                '\u06f7': '7',
                '\u06f8': '8',
                '\u06f9': '9',
            }[num]
        except KeyError:
            return False

    def checkinSym(self, word):
        for i in self.symbolTable:
            if i[0] == word:
                return True
        return False

    def generateC(self):
        # print('-6'.isdigit())
        qNum = 0
        line = 0
        line += 1
        print('L', line, ': ', "int main () {")
        for s in self.symbolTable:
            type = ""
            if s[1] == 'arith':
                type = "int"
            elif s[1] == "bool":
                type = "bool"
            elif s[1] == "char":
                type = "char"
            if s[0] == "غلط" or s[0] == "درست":
                continue
            name = self.var_handler(s[0])
            line += 1
            print('L', line, ': ', type, name, ";" )
            line += 1
            for var in self.meghdardehi:
                if s[0] == var[0]:
                    kooft = ""
                    if not (self.numconverter(var[1]) == False):
                        kooft = self.numconverter(var[1])
                    elif var[1].lstrip('-+').isdigit():
                        kooft = var[1]
                    elif var[1] == 'درست':
                        kooft = '1'
                    elif var[1] == 'غلط':
                        kooft = '0'
                    elif var[1].isalpha():

                        kooft = var[1]  # TODO man convert nakardam age char farsi bashe !
                    if kooft != '1111111111111111' :
                         print('L', line, ': ', name, ' = ', kooft, " ;" )

        for q in self.quadruples:

            qNum += 1
            arg1 = ""
            arg2 = ""
            op = ""
            result = ""
            if q.arg_one.startswith("Temp"):
                arg1 = q.arg_one
            elif self.checkinSym(q.arg_one):
                arg1 = self.var_handler(q.arg_one)
            elif not (self.numconverter(q.arg_one) == False):
                arg1 = self.numconverter(q.arg_one)
            elif q.arg_one.lstrip('-+').isdigit():
                arg1 = q.arg_one
            elif q.arg_one == 'درست':
                arg1 = '1'
            elif q.arg_one == 'غلط':
                arg1 = '0'
            elif q.arg_one.isalpha():
                arg1 = q.arg_one  # TODO man convert nakardam age char farsi bashe !
            else:
                arg1 = "aaannn e man  :) "

            if q.arg_two.startswith("Temp"):
                arg2 = q.arg_two
            elif self.checkinSym(q.arg_two):
                arg2 = self.var_handler(q.arg_two)
            elif not (self.numconverter(q.arg_two) == False):
                arg2 = self.numconverter(q.arg_two)
            elif q.arg_two.lstrip('-+').isdigit():
                arg2 = q.arg_two
            elif q.arg_two == 'درست':
                arg2 = '1'
            elif q.arg_two == 'غلط':
                arg2 = '0'
            elif q.arg_two.isalpha():
                arg2 = q.arg_two  # TODO man convert nakardam age char farsi bashe !
            else:
                arg2 = "aaannn e man  :) "

            if q.result.startswith("Temp"):
                result = q.result
            elif self.checkinSym(q.result):
                result = self.var_handler(q.result)
            elif q.result == "goto":
                pass  # TODO
            else:
                result = "aaannn e man  :) "

            if q.op == '+' or q.op == '-' or q.op == '*' or q.op == '-':
                line += 1
                print('L', line, ': ', result, " = ", arg1, q.op, arg2, ";")
            elif q.op == '=':
                line += 1
                print('L', line, ': ', result, " = ", arg1, ";")
            elif (q.op == '<' or q.op == '>' or q.op == '<=' or q.op == '>=' or q.op == '==' or q.op == '!='):
                line += 1
                if q.result == 'goto' or q.result == 'goto ':

                    print('L', line, ': ', "if ", arg1, q.op, arg2, q.result)
                else:
                    n1 = (q.result.strip()[4:])
                    max = 0
                    for i in n1.split(" "):
                        if not i == "":
                            if max < int(i):
                                max = int(i)
                    newLine = max - qNum + 1 + line
                    print('L', line, ': ', "if ", arg1, q.op, arg2, 'goto', newLine)

            elif q.op == '' and q.result.strip()[:4] == 'goto':
                line += 1
                if q.result == 'goto' or q.result == 'goto ':

                    print('L', line, ': ', q.result)
                else:

                    n2 = q.result.strip()[4:]
                    max = 0
                    for i in n2.split(" "):
                        if not i == "":
                            if max < int(i):
                                max = int(i)
                    newLine = max - qNum + 1 + line
                    print('L', line, ': ', 'goto', newLine)

        print("}")


if __name__ == "__main__":
    data = '''برنامه تست 
    حرف اصلي ( ) { 


    صحیح منیره = 1 ;
    کلید ( منیره )

    حالت 0 : اگر (منیره == 4)
    انگاه
    منیره = منیره + 1 ;;
    حالت 2 : منیره =  4  ;;
    تمام


وقتی (منیره < 8)
منیره = 9;

    }
    '''
    path = "code.txt"
    f = open(path)
    # data = f.read()
    f.close()

    parser = Parser()
    p = parser.build()
    p.parse(data, lexer=lexercompiler.build(), debug=False)
    parser.printQuadruples()
    parser.printSymbol()
    print()
    parser.generateC()
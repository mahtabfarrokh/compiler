import ply.lex as lex
import io

# Reserved words
reserved = (
    'PROGRAM', 'MAIN', 'STRUCT', 'CONSTANT', 'CHAR' , 'BOOL',
    'FLOAT', 'INT', 'IF', 'THEN', 'ELSE', 'KEY', 'END', 'STATE',
    'DEFAULT', 'WHILE', 'RETURN', 'BREAK', 'OR', 'AND',
    'ORELSE', 'ANDTHEN', 'NOT', 'FALSE', 'TRUE'
)

tokens = reserved + (

    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', 'TYPEID', 'ICONST', 'CCONST',

    # Operators (+,-,*,/,%, !, <, <=, >, >=, == ,?)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LT', 'LE', 'GT', 'GE', 'EQ','QM',

    # Assignment (=, *=, /=, +=, -= )
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Delimeters ( ) { } , ; : . [ ]
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMMA', 'SEMI', 'COLON', 'DOT',
    'LBR' , 'RBR'

)


# Completely ignored characters
t_ignore = ' \t\x0c'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

reserved_map = {}
#identifier & reserved words

def t_ID(t):
    r'[\u0627\u0628\u067E\u062A\u062B\u062C\u0686\u062D' \
    r'\u062E\u062F\u0630\u0631\u0632\u0698\u0633\u0634\u0635\u0636\u0637' \
    r'\u0638\u0639\u063A\u0641\u0642\u06A9\u06AF\u0644\u0645\u0646\u0648\u0647\u06CC'  \
    r'\u0061\u0062\u0063\u0064\u0065\u0066\u0067\u0068\u0069\u006a\u006b\u006c\u006d' \
    r'\u006e\u006f\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077\u0078\u0079\u007a_][\w_]*'

    if (t.value == '\u0628\u0631\u0646\u0627\u0645\u0647'):
        t.type = reserved_map.get(t.value, "PROGRAM")     # برنامه
        return t
    elif (t.value == '\u0627\u0635\u0644\u06CC'):
        t.type = reserved_map.get(t.value,"MAIN") #اصلی
        return t
    elif (t.value =='\u0633\u0627\u062E\u062A\u0627\u0631'):
        t.type = reserved_map.get(t.value, "STRUCT")    # ساختار
        return t
    elif (t.value =='\u062B\u0627\u0628\u062A'):
        t.type = reserved_map.get(t.value,"CONSTANT" )    # ثابت
        return t
    elif (t.value =='\u062D\u0631\u0641' ):
        t.type = reserved_map.get(t.value, "CHAR")  # حرف
        return t
    elif (t.value == '\u0645\u0646\u0637\u0642\u06CC'):
        t.type = reserved_map.get(t.value,"BOOL")         #منطقی
        return t
    elif (t.value =='\u0627\u0639\u0634\u0627\u0631\u06CC'):
        t.type = reserved_map.get(t.value, "FLOAT")     #اعشاری
        return t
    elif (t.value =='\u0635\u062D\u06CC\u062D'):
        t.type = reserved_map.get(t.value,"INT" )   #صحیح
        return t
    elif (t.value =='\u0627\u06AF\u0631'):
        t.type = reserved_map.get(t.value,"IF" ) #اگر
        return t
    elif (t.value == '\u0627\u0646\u06AF\u0627\u0647'):
        t.type = reserved_map.get(t.value,"THEN")   # آنگاه
        return t
    elif (t.value =='\u0648\u06AF\u0631\u0646\u0647'):
        t.type = reserved_map.get(t.value,"ELSE" )       # وگرنه
        return t
    elif (t.value =='\u06A9\u0644\u06CC\u062F'):
        t.type = reserved_map.get(t.value,"KEY" )        # کلید
        return t
    elif (t.value =='\u062A\u0645\u0627\u0645' ):
        t.type = reserved_map.get(t.value,"END" )        # تمام
        return t
    elif (t.value =='\u062D\u0627\u0644\u062A' ):
        t.type = reserved_map.get(t.value,"STATE")      # حالت
        return t
    elif (t.value =='\u067E\u06CC\u0634\u0641\u0631\u0636'):
        t.type = reserved_map.get(t.value,"DEFAULT" )    # پیشفرض
        return t
    elif (t.value == '\u0648\u0642\u062A\u06CC'):
        t.type = reserved_map.get(t.value,"WHILE" ) # وقتی
        return t
    elif (t.value =='\u0628\u0631\u06AF\u0631\u062F\u0627\u0646'):
        t.type = reserved_map.get(t.value,"RETURN" )    # برگردان
        return t
    elif (t.value =='\u0628\u0634\u06A9\u0646' ):
        t.type = reserved_map.get(t.value, "BREAK")    # بشکن
        return t
    elif (t.value =='\u06CC\u0627'):
        t.type = reserved_map.get(t.value,"OR" )        # یا
        return t
    elif (t.value == '\u0648'):
        t.type = reserved_map.get(t.value,"AND" )       # و
        return t
    elif (t.value =='\u06CC\u0627\u0648\u06AF\u0631\u0646\u0647'):
        t.type = reserved_map.get(t.value, "ORELSE")         # یا وگرنه
        return t
    elif (t.value == '\u0648\u0647\u0645\u0686\u0646\u06CC\u0646' ):
        t.type = reserved_map.get(t.value, "ANDTHEN")       # و همچنین
        return t
    elif (t.value =='\u062E\u0644\u0627\u0641' ):
        t.type = reserved_map.get (t.value, "NOT" )         # خلاف
        return t
    elif (t.value == '\u063A\u0644\u0637'):
        t.type = reserved_map.get (t.value, "FALSE")        # غلط
        return t
    elif (t.value =='\u062F\u0631\u0633\u062A' ):
        t.type = reserved_map.get (t.value,"TRUE" )         # درست
        return t
    t.type = reserved_map.get(t.value, "ID")
    return t


# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_QM = r'\?'
# Assignment operators

t_EQUALS = r'='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='

# Increment/decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'


# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMI = r';'
t_COLON = r':'
t_DOT = r'\.'
t_LBR = r'\['
t_RBR = r'\]'

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'


L2 = {'\u0627', '\u0628', '\u067E', '\u062A', '\u062B', '\u062C', '\u0686', '\u062D',
      '\u062E', '\u062F', '\u0630', '\u0631', '\u0632', '\u0698', '\u0633', '\u0634', '\u0635', '\u0636', '\u0637',
      '\u0638', '\u0639', '\u063A', '\u0641', '\u0642', '\u06A9', '\u06AF', '\u0644', '\u0645', '\u0646', '\u0648',
      '\u0647', '\u06CC',
      '\u0061', '\u0062', '\u0063', '\u0064', '\u0065', '\u0066', '\u0067', '\u0068', '\u0069', '\u006a', '\u006b',
      '\u006c', '\u006d', '\u006e', '\u006f', '\u0070', '\u0071', '\u0072', '\u0073', '\u0074', '\u0075', '\u0076',
      '\u0077', '\u0078', '\u0079', '\u007a'}

# Character constant 'c' or L'c'
t_CCONST = r'(L2)?\'([^\\\n]|(\\.))*?\''

# Comments


def t_comment(t):
    r'(/\*(.|\n)*?\*/)|//'
    t.lexer.lineno += t.value.count('\n')

# Preprocessor directive (ignored)


def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


def build():
        '''
        build the lexer
        '''
        lexer = lex.lex()
        return lexer


if __name__ == "__main__":
    # lex.runmain(lexer)
    path = "code.txt"
    f = open(path)
    # with io.open(path, 'r', encoding='utf8') as f:
    #     text = f.read()
    text = f.read()
    f.close()

    lexer = lex.lex()
    lexer.input(text)
    #f2 = open("res.txt" , "w+")
    for token in lexer:
        s = str (token)
        x = s.find(",")
        print(s)
     #   f2.write(s[9:x] + "\n")

    #f2.close()
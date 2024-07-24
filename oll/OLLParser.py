# Generated from OLL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,43,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,
        10,12,14,16,18,20,22,0,0,64,0,27,1,0,0,0,2,30,1,0,0,0,4,42,1,0,0,
        0,6,44,1,0,0,0,8,47,1,0,0,0,10,50,1,0,0,0,12,53,1,0,0,0,14,55,1,
        0,0,0,16,57,1,0,0,0,18,59,1,0,0,0,20,61,1,0,0,0,22,64,1,0,0,0,24,
        26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,1,1,0,0,0,29,27,1,0,0,0,30,31,3,4,2,0,31,32,5,1,0,0,32,3,1,
        0,0,0,33,43,3,6,3,0,34,43,3,8,4,0,35,43,3,10,5,0,36,43,3,12,6,0,
        37,43,3,14,7,0,38,43,3,16,8,0,39,43,3,18,9,0,40,43,3,20,10,0,41,
        43,3,22,11,0,42,33,1,0,0,0,42,34,1,0,0,0,42,35,1,0,0,0,42,36,1,0,
        0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,
        1,0,0,0,43,5,1,0,0,0,44,45,5,4,0,0,45,46,5,2,0,0,46,7,1,0,0,0,47,
        48,5,5,0,0,48,49,5,3,0,0,49,9,1,0,0,0,50,51,5,6,0,0,51,52,5,3,0,
        0,52,11,1,0,0,0,53,54,5,7,0,0,54,13,1,0,0,0,55,56,5,8,0,0,56,15,
        1,0,0,0,57,58,5,9,0,0,58,17,1,0,0,0,59,60,5,10,0,0,60,19,1,0,0,0,
        61,62,5,11,0,0,62,63,5,4,0,0,63,21,1,0,0,0,64,65,5,12,0,0,65,66,
        5,4,0,0,66,23,1,0,0,0,2,27,42
    ]

class OLLParser ( Parser ):

    grammarFileName = "OLL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "':'", "<INVALID>", "<INVALID>", 
                     "'PUSH'", "'POP'", "'ADD'", "'SUB'", "'PRINT'", "'READ'", 
                     "'JUMP.EQ.0'", "'JUMP.GT.0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "LABEL", 
                      "PUSH", "POP", "ADD", "SUB", "PRINT", "READ", "JUMPEQ0", 
                      "JUMPGT0" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_label = 3
    RULE_push = 4
    RULE_pop = 5
    RULE_add = 6
    RULE_sub = 7
    RULE_print = 8
    RULE_read = 9
    RULE_jumpeq0 = 10
    RULE_jumpgt0 = 11

    ruleNames =  [ "program", "line", "statement", "label", "push", "pop", 
                   "add", "sub", "print", "read", "jumpeq0", "jumpgt0" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    LABEL=4
    PUSH=5
    POP=6
    ADD=7
    SUB=8
    PRINT=9
    READ=10
    JUMPEQ0=11
    JUMPGT0=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OLLParser.LineContext)
            else:
                return self.getTypedRuleContext(OLLParser.LineContext,i)


        def getRuleIndex(self):
            return OLLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OLLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8176) != 0):
                self.state = 24
                self.line()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(OLLParser.StatementContext,0)


        def getRuleIndex(self):
            return OLLParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = OLLParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.statement()
            self.state = 31
            self.match(OLLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(OLLParser.LabelContext,0)


        def push(self):
            return self.getTypedRuleContext(OLLParser.PushContext,0)


        def pop(self):
            return self.getTypedRuleContext(OLLParser.PopContext,0)


        def add(self):
            return self.getTypedRuleContext(OLLParser.AddContext,0)


        def sub(self):
            return self.getTypedRuleContext(OLLParser.SubContext,0)


        def print_(self):
            return self.getTypedRuleContext(OLLParser.PrintContext,0)


        def read(self):
            return self.getTypedRuleContext(OLLParser.ReadContext,0)


        def jumpeq0(self):
            return self.getTypedRuleContext(OLLParser.Jumpeq0Context,0)


        def jumpgt0(self):
            return self.getTypedRuleContext(OLLParser.Jumpgt0Context,0)


        def getRuleIndex(self):
            return OLLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OLLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.label()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.push()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.pop()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.add()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.sub()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.print_()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                self.read()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.jumpeq0()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 9)
                self.state = 41
                self.jumpgt0()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(OLLParser.LABEL, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = OLLParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(OLLParser.LABEL)
            self.state = 45
            self.match(OLLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUSH(self):
            return self.getToken(OLLParser.PUSH, 0)

        def NUMBER(self):
            return self.getToken(OLLParser.NUMBER, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_push

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPush" ):
                return visitor.visitPush(self)
            else:
                return visitor.visitChildren(self)




    def push(self):

        localctx = OLLParser.PushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(OLLParser.PUSH)
            self.state = 48
            self.match(OLLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POP(self):
            return self.getToken(OLLParser.POP, 0)

        def NUMBER(self):
            return self.getToken(OLLParser.NUMBER, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_pop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPop" ):
                return visitor.visitPop(self)
            else:
                return visitor.visitChildren(self)




    def pop(self):

        localctx = OLLParser.PopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(OLLParser.POP)
            self.state = 51
            self.match(OLLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(OLLParser.ADD, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_add

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = OLLParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(OLLParser.ADD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(OLLParser.SUB, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_sub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)




    def sub(self):

        localctx = OLLParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(OLLParser.SUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(OLLParser.PRINT, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = OLLParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(OLLParser.PRINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(OLLParser.READ, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_read

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = OLLParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(OLLParser.READ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jumpeq0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JUMPEQ0(self):
            return self.getToken(OLLParser.JUMPEQ0, 0)

        def LABEL(self):
            return self.getToken(OLLParser.LABEL, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_jumpeq0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpeq0" ):
                return visitor.visitJumpeq0(self)
            else:
                return visitor.visitChildren(self)




    def jumpeq0(self):

        localctx = OLLParser.Jumpeq0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_jumpeq0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(OLLParser.JUMPEQ0)
            self.state = 62
            self.match(OLLParser.LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jumpgt0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JUMPGT0(self):
            return self.getToken(OLLParser.JUMPGT0, 0)

        def LABEL(self):
            return self.getToken(OLLParser.LABEL, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_jumpgt0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpgt0" ):
                return visitor.visitJumpgt0(self)
            else:
                return visitor.visitChildren(self)




    def jumpgt0(self):

        localctx = OLLParser.Jumpgt0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_jumpgt0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(OLLParser.JUMPGT0)
            self.state = 65
            self.match(OLLParser.LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






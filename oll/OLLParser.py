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
        4,1,15,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,70,0,29,1,
        0,0,0,2,32,1,0,0,0,4,45,1,0,0,0,6,47,1,0,0,0,8,50,1,0,0,0,10,52,
        1,0,0,0,12,55,1,0,0,0,14,58,1,0,0,0,16,60,1,0,0,0,18,62,1,0,0,0,
        20,65,1,0,0,0,22,67,1,0,0,0,24,70,1,0,0,0,26,28,3,2,1,0,27,26,1,
        0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,
        29,1,0,0,0,32,33,3,4,2,0,33,34,5,1,0,0,34,3,1,0,0,0,35,46,3,6,3,
        0,36,46,3,8,4,0,37,46,3,10,5,0,38,46,3,12,6,0,39,46,3,14,7,0,40,
        46,3,16,8,0,41,46,3,18,9,0,42,46,3,20,10,0,43,46,3,22,11,0,44,46,
        3,24,12,0,45,35,1,0,0,0,45,36,1,0,0,0,45,37,1,0,0,0,45,38,1,0,0,
        0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,43,
        1,0,0,0,45,44,1,0,0,0,46,5,1,0,0,0,47,48,5,13,0,0,48,49,5,2,0,0,
        49,7,1,0,0,0,50,51,5,3,0,0,51,9,1,0,0,0,52,53,5,4,0,0,53,54,5,12,
        0,0,54,11,1,0,0,0,55,56,5,5,0,0,56,57,5,12,0,0,57,13,1,0,0,0,58,
        59,5,6,0,0,59,15,1,0,0,0,60,61,5,7,0,0,61,17,1,0,0,0,62,63,5,8,0,
        0,63,64,5,14,0,0,64,19,1,0,0,0,65,66,5,9,0,0,66,21,1,0,0,0,67,68,
        5,10,0,0,68,69,5,13,0,0,69,23,1,0,0,0,70,71,5,11,0,0,71,72,5,13,
        0,0,72,25,1,0,0,0,2,29,45
    ]

class OLLParser ( Parser ):

    grammarFileName = "OLL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "':'", "'HALT'", "'PUSH'", "'POP'", 
                     "'ADD'", "'SUB'", "'PRINT'", "'READ'", "'JUMP.EQ.0'", 
                     "'JUMP.GT.0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "HALT", "PUSH", 
                      "POP", "ADD", "SUB", "PRINT", "READ", "JUMPEQ0", "JUMPGT0", 
                      "NUMBER", "LABEL", "STRING", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_label = 3
    RULE_halt = 4
    RULE_push = 5
    RULE_pop = 6
    RULE_add = 7
    RULE_sub = 8
    RULE_print = 9
    RULE_read = 10
    RULE_jumpeq0 = 11
    RULE_jumpgt0 = 12

    ruleNames =  [ "program", "line", "statement", "label", "halt", "push", 
                   "pop", "add", "sub", "print", "read", "jumpeq0", "jumpgt0" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    HALT=3
    PUSH=4
    POP=5
    ADD=6
    SUB=7
    PRINT=8
    READ=9
    JUMPEQ0=10
    JUMPGT0=11
    NUMBER=12
    LABEL=13
    STRING=14
    WS=15

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12280) != 0):
                self.state = 26
                self.line()
                self.state = 31
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
            self.state = 32
            self.statement()
            self.state = 33
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


        def halt(self):
            return self.getTypedRuleContext(OLLParser.HaltContext,0)


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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.label()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.halt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.push()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.pop()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.add()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.sub()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.print_()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.read()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 9)
                self.state = 43
                self.jumpeq0()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 10)
                self.state = 44
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
            self.state = 47
            self.match(OLLParser.LABEL)
            self.state = 48
            self.match(OLLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HaltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HALT(self):
            return self.getToken(OLLParser.HALT, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_halt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHalt" ):
                return visitor.visitHalt(self)
            else:
                return visitor.visitChildren(self)




    def halt(self):

        localctx = OLLParser.HaltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_halt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(OLLParser.HALT)
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
        self.enterRule(localctx, 10, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(OLLParser.PUSH)
            self.state = 53
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
        self.enterRule(localctx, 12, self.RULE_pop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(OLLParser.POP)
            self.state = 56
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
        self.enterRule(localctx, 14, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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
        self.enterRule(localctx, 16, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
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

        def STRING(self):
            return self.getToken(OLLParser.STRING, 0)

        def getRuleIndex(self):
            return OLLParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = OLLParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(OLLParser.PRINT)
            self.state = 63
            self.match(OLLParser.STRING)
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
        self.enterRule(localctx, 20, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
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
        self.enterRule(localctx, 22, self.RULE_jumpeq0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(OLLParser.JUMPEQ0)
            self.state = 68
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
        self.enterRule(localctx, 24, self.RULE_jumpgt0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(OLLParser.JUMPGT0)
            self.state = 71
            self.match(OLLParser.LABEL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






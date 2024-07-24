# Generated from OLL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OLLParser import OLLParser
else:
    from OLLParser import OLLParser

# This class defines a complete generic visitor for a parse tree produced by OLLParser.

class OLLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OLLParser#program.
    def visitProgram(self, ctx:OLLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#line.
    def visitLine(self, ctx:OLLParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#statement.
    def visitStatement(self, ctx:OLLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#label.
    def visitLabel(self, ctx:OLLParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#halt.
    def visitHalt(self, ctx:OLLParser.HaltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#push.
    def visitPush(self, ctx:OLLParser.PushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#pop.
    def visitPop(self, ctx:OLLParser.PopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#add.
    def visitAdd(self, ctx:OLLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#sub.
    def visitSub(self, ctx:OLLParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#print.
    def visitPrint(self, ctx:OLLParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#read.
    def visitRead(self, ctx:OLLParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#jumpeq0.
    def visitJumpeq0(self, ctx:OLLParser.Jumpeq0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OLLParser#jumpgt0.
    def visitJumpgt0(self, ctx:OLLParser.Jumpgt0Context):
        return self.visitChildren(ctx)



del OLLParser
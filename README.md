# bvdl-oll-antlr4
ANTLR4 Implementation of bvdl.io's oll

## Running ANTLR4 on the grammar file

You only need to do this if you change the grammar file `oll.g4`:

    curl -o antlr-4.13.1-complete.jar https://www.antlr.org/download/antlr-4.13.1-complete.jar

To run it:

    java -jar antlr-4.13.1-complete.jar -Werror -no-listener -visitor -Dlanguage=Python3 -o oll OLL.g4

This is also provided in the shell script `antlr4.sh`

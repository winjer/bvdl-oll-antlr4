#!/bin/sh
java -jar antlr-4.13.1-complete.jar -Werror -no-listener -visitor -Dlanguage=Python3 -o oll OLL.g4
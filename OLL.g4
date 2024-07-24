grammar OLL;

program: line*;

line: statement '\n';

statement:
	label
	| push
	| pop
	| add
	| sub
	| print
	| read
	| jumpeq0
	| jumpgt0;

label: LABEL ':';
push: PUSH NUMBER;
pop: POP NUMBER;
add: ADD;
sub: SUB;
print: PRINT;
read: READ;
jumpeq0: JUMPEQ0 LABEL;
jumpgt0: JUMPGT0 LABEL;

NUMBER: [0-9]+;
LABEL: [a-zA-Z]+;
PUSH: 'PUSH';
POP: 'POP';
ADD: 'ADD';
SUB: 'SUB';
PRINT: 'PRINT';
READ: 'READ';
JUMPEQ0: 'JUMP.EQ.0';
JUMPGT0: 'JUMP.GT.0';
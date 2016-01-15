all: count-lines count-lwc count-num calc text-cleanup

#optional: ex1 ex2 ex3 ex4

#since make knows about lex, just giving the following is sufficient
count-lwc: count-lwc.o
	cc -o count-lwc count-lwc.o -ll

count-lines: count-lines.o
	cc -o count-lines count-lines.o -ll

count-num: count-num.o
	cc -o count-num count-num.o -ll

text-cleanup: text-cleanup.o
	cc -o text-cleanup text-cleanup.o -ll

calc: lex.yy.c y.tab.c y.tab.h
	cc lex.yy.c y.tab.c -o calc

lex.yy.c: calc.l
	lex calc.l

y.tab.c: calc.y
	yacc -d calc.y

.PHONY: clean
clean:
	rm -f count-lines count-lines.o count-lines.c count-lwc count-lwc.o count-lwc.c\
	count-num count-num.o count-num.c calc calc.c lex.yy.c y.tab.c y.tab.h 

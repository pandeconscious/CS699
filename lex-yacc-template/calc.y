%{
	#include <stdio.h>
	int yylex(void);
	void yyerror(char *);
%}

%token INTEGER
%left '+' '-' /* + and - are left associative */
%left '*' '/' /*the last definition listed has the highest precedence*/ 
%%

program:
	program expr '\n' {printf("%d\n", $2);}
	| '\n' {}
	|
	;

expr:
	INTEGER {$$ = $1;}
	| expr '+' expr {$$ = $1 + $3;}
	| expr '-' expr {$$ = $1 - $3;}
	| expr '*' expr {$$ = $1 * $3;}
	| expr '/' expr {$$ = (float)$1 / $3;}
	| '(' expr ')' {$$ = $2;}
	;

%%

void yyerror(char *s){
	fprintf(stderr, "%s\n", s);
}

int main(void){
	yyparse();
	return 0;
}


/*This program counts no. of integers and no. of floats separately/

/*
Crucial points regarding lex:
1. If two patterns match the same string, the longest match wins, thus only the action corresponding to that pattern will be executed.
2. In case both matches are the same length, then the first pattern listed is used.
3. The inbuilt yyleng stores no. of characters matched.
*/

/*definitions*/
%{
	/*definitions pertatining to C code go here in between %{ and %}*/
	int intCount = 0;
	int floatCount = 0;
%}

/*non-C definition go here*/
digit [0-9]
whitespace [ \t\n]
%%
{whitespace}+{digit}+{whitespace}+ {intCount++ ; printf("The matched int is %s \n", yytext); }
{digit}+[.]{digit}+ floatCount++ ;
. ;
%%

/*C code*/
int main(){
	yylex();
	printf("\nNumber of integers and number of floats are %d and %d \n", intCount, floatCount);
	return 0;
}

/*code to count no. of lines in an input*/
/*definitions*/
%{
	int linesCount = 0;
%}

/*rules*/
%%

. ; /*do nothing on seeing a character, otherwise it prints what it reads*/
\n linesCount++; /*increase linecount on seeing a new line character*/

%%

/*C code*/
int main(){
	yylex();
	printf("\nNumber of lines in the input = %d \n", linesCount);
	return 0;
}


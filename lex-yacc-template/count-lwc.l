/*This program counts no. of lines, no.of words(alphanumeric only) and no. of characters(allpossible)*/

/*
Crucial points regarding lex:
1. If two patterns match the same string, the longest match wins, thus only the action corresponding to that pattern will be executed.
2. In case both matches are the same length, then the first pattern listed is used.
3. The inbuilt yyleng stores no. of characters matched.
*/

/*definitions*/
%{
	/*definitions pertatining to C code go here in between %{ and %}*/
	int linesCount = 0;
	int wordCount = 0;
	int charCount = 0;
%}

/*non-C definition go here*/
alphanum [a-zA-z0-9]

%%

{alphanum}+ {wordCount++; charCount += yyleng;/* yyleng will give count of characters when a word is matched*/}
. charCount++;/*pattern in thi rule won't match newline and also the alphanum rule will
override this rule, so characters in words as defined in the question won't be counted*/
\n {linesCount++; charCount++;} /*increase linecount on seeing a new line character*/

%%

/*C code*/
int main(){
	yylex();
	printf("\nNumber of lines = %d \nNum of words = %d \nNum of characters = %d \n ", linesCount, wordCount, charCount);
	return 0;
}

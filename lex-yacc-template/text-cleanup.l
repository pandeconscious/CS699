/*the text cleaning - removing unnecessay spaces and taking care of spaces around
parentheses*/

punct [,.;:!?]
text [a-zA-Z]
space [ \t]
%%

")"{space}+/{punct} {while (yytext[yyleng-1] == ' ' || yytext[yyleng-1] == '\t') yyleng--; ECHO;/*no space between closing parentheses and punctuation*/}
")"/{text} {printf(") ");/*single space between closing parenthese and text*/}
{text}+" "+/")" {while (yytext[yyleng-1] ==' ') yyleng--; ECHO;/*no space between text and closing parentheses*/}
({punct}|{text}+)/"(" {ECHO; printf(" ");/*single space between text|punct and closing parentheses */}
"("" "+/{text} {while (yytext[yyleng-1]==' ') yyleng--; ECHO;}
{text}+" "+/{punct} {while (yytext[yyleng-1]==' ') yyleng--; ECHO;}
^" "+ ;
" "+ {printf(" ");}
. {ECHO;}
\n/[\n]+ ;
\n {ECHO;}

%%

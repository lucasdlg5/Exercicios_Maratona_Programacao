# Exercicios_Maratona_Programacao

Outros Links uteis:
http://www.lia.ufc.br/~wladimir/gemp/index.html
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=0
https://www.computersciencemaster.com.br/exercicios-de-logica-de-programacao/
https://fit.faccat.br/~fpereira/apostilas/exerc_resp_alg_mar2007.pdf

Texto abaixo retirado de: https://www.fateclins.edu.br/site/maratona/dicas.php
## Como preparar-se

Alguns Links interessantes:

• http://maratona.ime.usp.br - Site oficial da Maratona de Programação promovida pela Sociedade Brasileira de Computação;


• http://br.spoj.pl - SPOJ Brasil . Site usado para praticar a resolucão de problemas, possui arquivo de problemas das maratonas passadas;


• http://br.spoj.pl/forum - Forum do site acima. É bem util quando você não consegue resolver um problema, pois pode procurar pelos tópicos sobre o problema e ver o que os outros usuários falaram;

• http://www.spoj.pl - Site para praticar programação, em inglês. Possui mais problemas;


• http://cerberus.delos.com:790/usacogate - USAco Trainning. Curso preparatório para a IOI (International Olympiads of Informatics). Apresenta diferentes problemas clássicos em ordem crescente de dificuldade com explicações e técnicas úteis para problemas de competições;


• http://uva.onlinejudge.org - Sistema de Competições on-line da Universidade de Valladolid. Possui centenas de problemas que podem ser testados através de um sistema de correção automática;


• http://www.codechef.com - CODEChef - Outro site em inglês, com competicões online;


• http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=alg_index - TOPCoder - Página de tutoriais, dicas e artigos sobre resolução de problemas.

• http://www.lia.ufc.br/~wladimir/gemp/index.html - Página de Treinamento do Grupo de Maratona da Universidade Federal do Ceará com Dicas, Links, Exemplos e material de estudo para Maratonas de Programação. 

## Exemplo de problema

Dada uma lista de N inteiros, encontre a soma de todos eles.


### Entrada
A entrada é composta de um único caso de teste. A primeira linha contém um inteiro positivo N. As N linhas seguintes contêm cada uma um inteiro X, representando os N números a serem somados.


### Saída
Seu programa deve produzir uma única linha na saída, contendo a soma de todos os N inteiros.


Restrições
0 ≤ N ≤ 50
|X| ≤ 5000



Exemplo Entrada
2
2
3


Saída
5	Exemplo Entrada
3
1
5
3


Saída
9


Exemplo de código soma.c

```C
#include <stdio.h>
int main(int argc, const char * argv[]){
  int n, s, i, t=0;

  scanf("%i", &n);

  for(i=0; i<n; i++){
     scanf("%i", &s);
     t += s;
  }
  printf("%i\n", t);
  return 0;
}
```
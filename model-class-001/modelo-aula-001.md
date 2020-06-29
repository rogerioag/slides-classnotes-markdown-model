---
classnumber: Aula 01
title: Introdução à Computação Paralela em Sistemas Heterogêneos
subtitle: Apresentação e Visão Geral da Disciplina
author:
- name: Prof. Rogério Aparecido Gonçalves
  citation: R. A. GONÇALVES
  id: 1
  affiliation: Universidade Tecnológica Federal do Paraná (UTFPR)
  department: Departamento de Computação (DACOM)
  citystatecountry: Campo Mourão - Paraná - Brasil
  email: rogerioag@utfpr.edu.br
date: 23 de Junho de 2020
coursename: Ciência da Computação
subjectname: BCC33B - Arquitetura e Organização de Computadores
idsubjectcourseinstitution: BCC33B-IC3A
abstract: Resumo da Aula.
banner: figuras/banner.pdf
banner-slides: figuras/banner-slides.pdf
banner-classnotes: figuras/banner-classnotes.pdf
---

# Introdução

## Introdução

* Tópico nível 1
  + Tópico nível 2
    - Tópico nível 3

## Bloco

* Blabla
  \note{Nota Bla Bla}

### Bloco Teste

* Bla bla bla bla

### Bloco Teste 2
Bla bla bla bla

## Duas colunas

[columns]

[column=0.5]

~~~~python
    if __name__ == "__main__":
        print "Hello World"
~~~~

Conforme Figura \ref{lstpreprocess}

~~~~{.python .numberLines caption="The preprocessing step" label=lstpreprocess}
def myfunction(var):
  """ Oh how awesome this is. """
  pass
~~~~

~~~~{.C .numberLines caption="This is a caption"}
int main(){
  return 0;
}
~~~~

[column=0.5]

This is how a "Hello World" looks like in Python

```Pseudo
int main(){
  return 0;
}
```
[/columns]

## Código em uma página

```{.Pseudo caption="This is a Pseudo"}
int main(){
  int a, b = 0;
  int f =  a + b;
  return 0;
}
```

## Citações

Segundo [@2014:PCC:2935593] 

Bla bla bla [@nvidia:maxwell]

![This is the caption \label{mylabel}](figuras/fig.png)

Conforme foi apresentado na Figura \ref{mylabel}.

# Seção 2

## Exemplo de Código

```c
  #include <stdio.h>

  int main() {
      printf("Hello World from C  :-)\n");
      return 0;
  }
```

## Exemplo de Código usando estilo

```{.c caption="Código" style=C basicstyle=\scriptsize\ttfamily}
  /*
   * cHelloWorld.c
   *
   */
  #include <stdio.h>

  int main() {
      printf("Hello World from C  :-)\n");
      return 0;
  }
```

## Hello World

* Bla

## Estrutura de um programa em CUDA

* Bla
+ Bla bla
- bla

## Saída de Terminal {.fragile .allowframebreaks}

[terminal]
rogerio@chamonix:hello-world$  ./hello-world.exe
Hello World!!!
Teste
Teste2
teste3
rogerio@chamonix:hello-world$
[/terminal]

## Organizando as Threads {.allowframebreaks}
* Teste
* Teste 2

[framebreak]

* Teste 3
* Teste 4

## Hide on Beamer {.fragile .allowframebreaks}

* Primeira linha.

[hideonbeamer]

* Texto oculto no beamer.

[/hideonbeamer]

* Segunda Linha.
* Terceira linha.
* Quarta linha.

## Blocos de Exemplos

* Texto antes do bloco.

[block]{Título do Bloco}

Conteúdo do Bloco sem ter problemas com níveis.

[/block]

[exampleblock]{Título do Bloco de Exemplo}

Conteúdo do Bloco de exemplo sem ter problemas com níveis. sdklfjasd sdlfjasdkl fjasd lsd fsdjfsd flasd sdjfsdlfsdjfsdjf sdf sdlfjasd sdl sdfjflasdjfsd sd flasdjf sdfl sdjfjasdlf asdlfjsdl fsd.

[/exampleblock]

[alertblock]{Título do Bloco de Alerta}

Conteúdo do Bloco de alerta sem ter problemas com níveis.

[/alertblock]

[background]{figuras/tux-search.png}

## Código dentro de Blocos

[exampleblock]{Código de Exemplo}

```c
  #include <stdio.h>

  int main() {
      printf("Hello World from C  :-)\n");
      return 0;
  }
```

[/exampleblock]

## Final Slide

* Tentativa de Colocar uma imagem de background.

<!-- 
## {.fragile .allowframebreaks .standout}
Thank you!
--> 

<!-- [appendix] -->

## Frame extra

* Teste de frame extra.

## Referências
\normalsize

LOUDEN, Kenneth C. Compiladores: princípios e práticas. São Paulo, SP: Thomson, c2004. xiv, 569 p. ISBN 8522104220.



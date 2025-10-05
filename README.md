# Projeto Redes Sociais

Uma interface estática que simula um smartphone, exibindo páginas de redes sociais dentro de um iframe central. A barra de ícones fica à direita no desktop e, no mobile, aparece através de um botão flutuante (FAB) com animação — tudo feito apenas com HTML e CSS.

## Demo
- GitHub Pages: https://mateusoliveiradev1.github.io/projeto-social/

## Funcionalidades
- Moldura de telefone centralizada com proporção correta (`images/frame-iphone.png`).
- Páginas individuais para cada rede dentro do iframe (`pages/`).
- Barra vertical de ícones com rolagem quando necessário.
- Menu mobile com botão flutuante (FAB) e animação hambúrguer → X (CSS-only).
- Responsividade com `clamp()` e media queries para tamanhos pequenos.
- Otimizações simples de LCP com preload de imagens críticas.

## Estrutura
```
projeto-social/
├── index.html
├── style/
│   ├── style.css      # Layout geral (moldura, barra de ícones, responsivo)
│   └── social.css     # Estilos das páginas dentro do iframe
├── pages/             # Páginas de cada rede social
│   ├── home.html
│   ├── youtube.html
│   ├── instagram.html
│   ├── twitter.html
│   ├── facebook.html
│   └── github.html
└── images/            # Imagens de fundo, moldura e logos
```

## Executar localmente
Requisitos: qualquer navegador moderno. Opcionalmente, Python para um servidor simples.

- Com Python (recomendado):
  - Entre na pasta do projeto e rode:
    - `python -m http.server 8000`
  - Abra: `http://localhost:8000/`

- Sem servidor: abra `index.html` diretamente no navegador (algumas features funcionam melhor via servidor).

## Publicação (GitHub Pages)
- O projeto está configurado como site estático. Para publicar:
  - Suba para a branch `main`.
  - Ative GitHub Pages em Settings → Pages, apontando para `main` (root).
  - A URL ficará como: `https://SEU_USUARIO.github.io/projeto-social/`.

## Como adicionar uma nova rede
1. Adicione o logo em `images/` e a imagem da tela (opcional).
2. Crie um arquivo em `pages/` seguindo o padrão das outras páginas e inclua `../style/social.css`.
3. Em `index.html`, adicione um novo `<a>` na seção `#redes-sociais` apontando para a página criada, com `target="tela"` e um `<img>` do logo.
4. Ajuste `style/style.css` somente se precisar mudar espaçamentos ou tamanhos.

## Personalização
- Fundo de madeira: troque `images/fundo-madeira.jpg` e ajuste `background` em `style.css`.
- Moldura do telefone: troque `images/frame-iphone.png` mantendo a proporção.
- Diâmetro dos ícones: controlado por `clamp()` em `section#redes-sociais img`.
- Posição do FAB: controlada por `#menu-button` em `index.html`.

## Acessibilidade
- Ícones possuem `alt` descritivo; considere adicionar `aria-label` nos links para leitores de tela.
- Contraste do FAB e foco podem ser ajustados conforme necessidade.

## Licença
- MIT (veja `LICENSE`).

## Créditos
- Imagens e logos utilizados apenas para fins didáticos/demonstração.
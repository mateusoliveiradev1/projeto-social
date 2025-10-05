<div align="center">

  <img src="favicon.ico" alt="Ícone" width="64" />

  <h1>Projeto Redes Sociais 📱</h1>
  <p><i>Uma UI estilo smartphone, com conteúdos de redes sociais exibidos no visor. Barra de ícones à direita no desktop e menu mobile com FAB animado — tudo em HTML + CSS.</i></p>

  <a href="https://mateusoliveiradev1.github.io/projeto-social/" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Demo-acesse-success" alt="Live Demo" />
  </a>
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License" />
  <img src="https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white" alt="HTML" />
  <img src="https://img.shields.io/badge/CSS-3-1572B6?logo=css3&logoColor=white" alt="CSS" />

</div>

---

## Sumário
- Visão Geral
- Funcionalidades
- Capturas de tela
- Executar localmente
- Publicação (GitHub Pages)
- Estrutura
- Como adicionar uma nova rede
- Personalização
- Acessibilidade
- Roadmap
- Licença e Créditos

## Visão Geral
Interface estática que simula um smartphone. A moldura central acomoda um `iframe` onde páginas de redes sociais são exibidas. No desktop, a barra de ícones fica fixa à direita; no mobile, um **botão flutuante (FAB)** abre/fecha a barra com uma animação hambúrguer → X, sem JavaScript.

## Funcionalidades
- Moldura de telefone centralizada com proporção correta (`images/frame-iphone.png`).
- Páginas específicas dentro do `iframe` (`pages/`).
- Barra vertical de ícones com rolagem e espaçamento fluido por `gap`.
- Menu mobile com botão flutuante (FAB) e animação hambúrguer → X (CSS-only).
- Responsividade com `clamp()` e media queries para telas pequenas.
- Preload de imagens críticas no `index.html` para melhorar LCP.

## Capturas de tela
<p align="center">
  <img src="images/tela-home.jpg" alt="Tela Home dentro do visor" width="420" />
</p>
<p align="center">
  <img src="images/frame-iphone.png" alt="Moldura do iPhone usada na UI" width="220" />
</p>

> Dica: se quiser, podemos adicionar uma captura completa da interface diretamente aqui. É só enviar uma imagem ou me pedir para gerar e incluir.

## Executar localmente
Requisitos: qualquer navegador moderno. Opcionalmente, Python para um servidor simples.

- Com Python (recomendado):
  - Entre na pasta do projeto e rode: `python -m http.server 8000`
  - Abra: `http://localhost:8000/`

- Sem servidor: abra `index.html` diretamente no navegador (algumas features funcionam melhor via servidor).

## Publicação (GitHub Pages)
1. Suba a branch `main` para seu repositório.
2. Acesse Settings → Pages e selecione Deploy from Branch, apontando para `main` (root).
3. Acesse: `https://SEU_USUARIO.github.io/projeto-social/`.

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

## Como adicionar uma nova rede
1. Adicione o logo em `images/` e a imagem da tela (opcional).
2. Crie um arquivo em `pages/` seguindo o padrão das outras páginas e inclua `../style/social.css`.
3. Em `index.html`, adicione um novo `<a>` na seção `#redes-sociais` apontando para a página criada, com `target="tela"` e um `<img>` do logo.
4. Ajuste `style/style.css` apenas se precisar mudar espaçamentos ou tamanhos.

## Personalização
- Fundo: troque `images/fundo-madeira.jpg` e ajuste `background` em `style.css`.
- Moldura: troque `images/frame-iphone.png` mantendo a proporção.
- Diâmetro dos ícones: controlado por `clamp()` em `section#redes-sociais img`.
- Posição do FAB: controlada por `#menu-button` em `index.html`.

## Acessibilidade
- Ícones possuem `alt`; considere adicionar `aria-label` nos links.
- Mantenha contraste do FAB adequado; foque em estados `:focus-visible` se desejar.

## Roadmap
- [ ] Adicionar screenshot completo da interface no README
- [ ] Ícones em SVG otimizados e placeholders para redes futuras
- [ ] Tema claro/escuro via CSS variables
- [ ] Ajustes finos para diferentes densidades de tela

## Licença e Créditos
- Licença: MIT (veja `LICENSE`).
- Imagens e logos utilizados apenas para fins didáticos/demonstração.
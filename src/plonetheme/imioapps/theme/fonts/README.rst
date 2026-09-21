Fonts
=====

The theme self-hosts its fonts. It does not load them from Google Fonts,
because a Belgian public sector site must not send visitor IP addresses
to a third party font service.

Put these files here:

- ``quicksand-latin-300-normal.woff2``
- ``quicksand-latin-400-normal.woff2``
- ``quicksand-latin-500-normal.woff2``
- ``quicksand-latin-600-normal.woff2``
- ``quicksand-latin-700-normal.woff2``
- ``nunito-latin-400-normal.woff2``
- ``nunito-latin-600-normal.woff2``
- ``nunito-latin-700-normal.woff2``

Quicksand is the display face. Nunito stands in for Avenir LT Std as the
body face. Replace Nunito with Avenir when the licence is available.

``scss/_fonts.scss`` declares the ``@font-face`` rules for these files.

Roboto
------

The Barceloneta base declares ``@font-face`` rules for Roboto. This theme
overrides the font stack with Quicksand and Nunito, so no rule uses
Roboto. A browser does not download a font that no rule uses, so the
theme does not ship the Roboto files.

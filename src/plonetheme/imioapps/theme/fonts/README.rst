Fonts
=====

The theme self-hosts its fonts. It does not load them from Google Fonts,
because a Belgian public sector site must not send visitor IP addresses
to a third party font service.

``npm run build`` copies the files here from the Fontsource packages.
``npm run copy:fonts`` does it on its own. Quicksand and Nunito are both
under the SIL Open Font License.

Quicksand is the display face. Nunito stands in for Avenir LT Std as the
body face. Replace Nunito with Avenir when the licence is available: drop
the woff2 files here, change ``scss/_fonts.scss`` and take nunito out of
``scripts/copy-fonts.mjs``.

Keep the weight lists in ``scripts/copy-fonts.mjs`` and
``scss/_fonts.scss`` in step.


Roboto
------

The Barceloneta base declares ``@font-face`` rules for Roboto. This theme
overrides the font stack with Quicksand and Nunito, so no rule uses
Roboto. A browser does not download a font that no rule uses, so the
theme does not ship the Roboto files.

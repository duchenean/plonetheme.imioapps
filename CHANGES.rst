Changelog
=========

3.0.0.dev0 (unreleased)
-----------------------

- Add the application chrome: top bar with the brand tile, the section
  tabs and the search; a marker on the meeting configuration tabs, which
  switch application; the left rail of saved searches; the Plone toolbar
  in the chrome colors. The shell takes the full window width.
  [duchenean]

- Skin bundles declare ``depends`` as ``all``. Plone renders the Diazo
  theme CSS after every ordinary bundle, so a skin needs the deferred
  group to load last and win.
  [duchenean]

- Rewrite of the theme for Plone 6.1 Classic UI on Bootstrap 5.
  The theme is now a Barceloneta child theme driven by the iMio design
  tokens. It replaces the Plone 4 skin layers.
  [duchenean]

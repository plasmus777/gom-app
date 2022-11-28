gom_app_sources = [
  'main.c',
  'gom-app-application.c',
  'gom-app-window.c',
]

gom_app_deps = [
  dependency('gtk4'),
  dependency('libadwaita-1'),
]

gom_app_sources += gnome.compile_resources('gom-app-resources',
  'gom-app.gresource.xml',
  c_name: 'gom_app'
)

executable('gom-app', gom_app_sources,
  dependencies: gom_app_deps,
       install: true,
)

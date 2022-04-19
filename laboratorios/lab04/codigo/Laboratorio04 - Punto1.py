# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

Proyecto = {'Root 4.0K': {'mauriciotoro 252K':'treeEtc.txt'},
            'mauriciotoro 4.0K': {'mauriciotoro 463K':'ED1-Guia-Proyecto-Enterga.doc',
                                  'mauriciotoro 1.5M':'ED1-Plantilla-Eafit.pptx',
                                  'mauriciotoro 1.1M':'plantilla-ACM-en-Latex.zip',
                                  'root 1.2M':'plantilla-ACM-en-Word.doc',
                                  'mauriciotoro 4.0K': {'mauriciotoro 9.4K':'acmcopyright.sty',
                                                        'mauriciotoro 144K':'acm-update.pdf',
                                                        'mauriciotoro 336K':'flies.eps',
                                                        'mauriciotoro 151K':'fly.eps',
                                                        'mauriciotoro 3.4K':'rosette.eps',
                                                        'mauriciotoro 65K':'sig-alternate-05-2015.cls',
                                                        'mauriciotoro 124K':'sig-alternate-guide.doc',
                                                        'mauriciotoro 572K':'sig-alternate-guide.pdf',
                                                        'mauriciotoro 255K':'sig-alternate-sample.pdf',
                                                        'mauriciotoro 26K':'sig-alternate-sample.tex',
                                                        'mauriciotoro 1.5K':'sigproc.bib'
                                                        }
                                  },
            'mauriciotoro 571K':'Proyecto final ED1 Sistema-directorios Vr 2.0.pdf'}

try:
  print(Proyecto['Root 4.0K']['mauriciotoro 252K'])
  print(Proyecto['mauriciotoro 4.0K']['mauriciotoro 4.0K']['mauriciotoro 1.5K'])
  print(Proyecto['Root 4.0K']['mauriciotoro 463K'])

except KeyError:
  print('No such file or directory')

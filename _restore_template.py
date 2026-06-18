"""Restore title separator with hyphen in baseof.html"""
path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\layouts\_default\baseof.html"
with open(path, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace('{{ .Title }}{{ end }}</title>', '{{ .Title }} - {{ .Site.Title }}</title>')

# Also handle the meta og:title and twitter:title
t = t.replace('{{ .Title }}{{ end }}">\n  <meta property="og:description"', '{{ .Title }} - {{ .Site.Title }}">\n  <meta property="og:description"')
t = t.replace('{{ .Title }}{{ end }}">\n  <meta name="twitter:card"', '{{ .Title }} - {{ .Site.Title }}">\n  <meta name="twitter:card"')

with open(path, "w", encoding="utf-8") as f:
    f.write(t)
print("Done")

# ScreenBuddy 0.7 – iPhone-Webtest

Dies ist eine eigenständige PWA auf Basis der Spielregeln aus Flutter 0.6; sie ist **keine kompilierte Flutter-iOS-App**. Die 8 GLB-Dateien stammen aus Version 0.6.

## Ohne Computer veröffentlichen
1. Auf dem iPhone in Safari einen GitHub-Account öffnen und ein **öffentliches** Repository `screenbuddy-test` erstellen. Keine Zugangsdaten in die Dateien schreiben.
2. Die Dateien aus diesem ZIP inklusive `models/` in das Repository hochladen. Die Weboberfläche von GitHub kann Mehrfach-Uploads auf Mobilgeräten erschweren; alternativ einen mobilen Git-Client oder einen statischen Hosting-Dienst mit ZIP-Upload verwenden.
3. Im Repository unter **Settings → Pages** die Veröffentlichung aus Branch `main` und Ordner `/ (root)` aktivieren.
4. Nach der Bereitstellung die angezeigte HTTPS-Adresse in Safari öffnen. Die Veröffentlichung kann einige Minuten dauern.
5. Safari: **Teilen → Zum Home-Bildschirm**. Danach über das neue Symbol öffnen.

**Hinweis:** Das Hochladen und Veröffentlichen wurde nicht durchgeführt. Die öffentliche URL entsteht erst durch dein Hosting. GitHub Pages ist für öffentliche Repositories verfügbar, prüfe aktuelle Bedingungen.

## Testfälle
- Start, Navigation durch fünf Bereiche, Pflege, Namensänderung
- 3D-Modell laden und zwischen Zuständen wechseln
- Skin-Auswahl und lokale Speicherung nach Neustart
- Fokustimer starten, Safari verlassen, zurückkehren, Zeit prüfen
- Nach zwei vollständigen Fokus-Sessions Evolution prüfen
- Flugmodus-Test: 3D-Viewer-Bibliothek wird von CDN geladen und ist **nicht zuverlässig offline** verfügbar

## Grenzen
- Keine iOS-Systemdaten (Bildschirmzeit/Schritte/Akku)
- Keine Push-Benachrichtigungen oder In-App-Käufe
- Keine automatische Übernahme der Flutter-0.6-Spielstände
- Kein nativer IPA-Build; keine echte iPhone-Installation via App Store
- 3D-Rendering und Animationen müssen auf Safari real getestet werden
- Die externe `model-viewer`-Bibliothek wird online geladen

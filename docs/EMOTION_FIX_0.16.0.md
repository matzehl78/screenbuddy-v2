# ScreenBuddy 0.16.0 – Emotionsreparatur

## Ausgangspunkt
Der vorhandene PWA-Code verwendet model-viewer, GLB-Wechsel und temporäre Emotionszustände. Bei wiederholtem Auslösen einer Emotion kann der Mund als dünner Strich erscheinen. Ursache noch nicht bestätigt.

## Vorgehen
1. Ausgangsverhalten auf echtem iPhone dokumentieren.
2. GLB-Animationen und Modellwechsel getrennt untersuchen.
3. Emotionszustand und Animationswiedergabe entkoppeln.
4. Modell-Load-Callbacks gegen veraltete Anforderungen absichern.
5. Nach jedem Wechsel Front- und Seitenansicht prüfen.
6. Erst nach bestandenen Tests auf main übernehmen.

## Abnahmekriterien
- Freude, Traurig, Überrascht je 10-mal hintereinander auslösen.
- Freude → Traurig → Freude → Überrascht je 10 Durchgänge.
- Mund bleibt in Front- und Seitenansicht korrekt geformt.
- Kameraausrichtung bleibt erhalten.
- Keine JavaScript-Fehler, kein verschwundenes Modell.
- Lokaler Spielstand bleibt erhalten.

## Sicherheit
Keine Änderungen an main und kein Pages-Deployment vor erfolgreichem Test.

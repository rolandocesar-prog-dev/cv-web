# Build a single SVG sprite from img/icons-src/*.svg into img/icons.svg
# Mantiene atributos stroke en \u00edconos UI (Lucide) que se pierden al strip del <svg> outer.

$src = "img/icons-src"
$out = "img/icons.svg"
if (-not (Test-Path $src)) {
    Write-Error "Carpeta fuente '$src' no existe. Coloca los SVG originales ah\u00ed antes de ejecutar."
    exit 1
}

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">')

Get-ChildItem $src -Filter *.svg | Sort-Object Name | ForEach-Object {
    $raw = Get-Content $_.FullName -Raw
    $id = $_.BaseName
    $viewBox = "0 0 24 24"
    if ($raw -match 'viewBox="([^"]+)"') { $viewBox = $matches[1] }
    $inner = $raw -replace '(?s)^.*?<svg[^>]*>', '' -replace '</svg>\s*$', ''
    $inner = $inner -replace '<\?xml[^?]+\?>', ''

    # Para iconos Lucide (UI) preservamos atributos de stroke
    if ($id.StartsWith('ui-')) {
        [void]$sb.AppendLine("  <symbol id=`"$id`" viewBox=`"$viewBox`" fill=`"none`" stroke=`"currentColor`" stroke-width=`"2`" stroke-linecap=`"round`" stroke-linejoin=`"round`">$inner</symbol>")
    } else {
        [void]$sb.AppendLine("  <symbol id=`"$id`" viewBox=`"$viewBox`">$inner</symbol>")
    }
}

[void]$sb.AppendLine('</svg>')
Set-Content -Path $out -Value $sb.ToString() -Encoding UTF8
"Sprite built: $out ($([math]::Round((Get-Item $out).Length/1KB,1)) KB)"

rule Lab39_Base64Marker {
 strings:
  $enc = "LAB39_HARMLESS_MARKER" base64
 condition:
  filesize < 1024 and $enc
}

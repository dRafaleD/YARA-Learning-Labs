rule Lab35_XorEncodedMarker {
 strings:
  $enc = "LAB35_HARMLESS_MARKER" xor
 condition:
  filesize < 1024 and $enc
}

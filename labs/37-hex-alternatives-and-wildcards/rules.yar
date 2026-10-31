rule Lab37_HexAlternatives {
 strings:
  $h = { 4C 41 42 33 37 ( 41 | 42 ) ?? 5F 4D }
 condition:
  $h
}

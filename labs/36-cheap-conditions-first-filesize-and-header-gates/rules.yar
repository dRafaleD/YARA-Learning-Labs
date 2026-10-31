rule Lab36_HeaderGate {
 strings:
  $m = "LAB36_HARMLESS_MARKER" ascii
 condition:
  uint16(0) == 0x5A4D and filesize < 4096 and $m
}

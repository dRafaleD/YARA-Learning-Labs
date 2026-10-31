global rule Lab40_SizeScope {
 condition:
  filesize < 1024
}

rule Lab40_Marker {
 strings:
  $m = "LAB40_HARMLESS_MARKER" ascii
 condition:
  $m
}

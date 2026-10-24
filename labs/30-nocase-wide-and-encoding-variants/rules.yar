rule Lab30_EncodingVariants {
 strings:
  $ci = "lab30_marker" ascii nocase
  $w = "lab30_marker" wide
 condition:
  filesize < 1024 and any of them
}

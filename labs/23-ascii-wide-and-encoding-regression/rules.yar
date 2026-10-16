rule Lab23_Encoding_Test : training {
 strings:
  $a = "LAB23_MARKER" ascii wide
  $b = "training_context" ascii wide
 condition:
  filesize < 10KB and all of them
}

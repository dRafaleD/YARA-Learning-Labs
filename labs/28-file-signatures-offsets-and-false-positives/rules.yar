rule Lab28_Header_And_Context : training {
 strings:
  $header = { 4C 41 42 32 38 }
  $context = "safe_document" ascii
 condition:
  filesize < 1024 and $header at 0 and $context
}

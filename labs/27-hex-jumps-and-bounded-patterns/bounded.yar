rule Lab27_Bounded_Training : training {
 strings:
  $a = { 4C 41 42 32 37 [2-4] 45 4E 44 }
 condition:
  filesize < 1024 and $a at 0
}

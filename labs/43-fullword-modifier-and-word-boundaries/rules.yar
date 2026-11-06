rule Lab43_Fullword {
 strings:
  $w = "LAB43WORD" ascii fullword
 condition:
  $w
}

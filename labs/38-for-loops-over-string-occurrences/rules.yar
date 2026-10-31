rule Lab38_EarlyOccurrence {
 strings:
  $a = "LAB38_ITEM" ascii
 condition:
  #a >= 1 and for any i in (1..#a) : ( @a[i] < 16 )
}

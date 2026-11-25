/* Synthetic training text only. */
rule Practice_Blue {
 strings:
  $a = "BLUE-TOKEN" ascii fullword
 condition:
  $a
}

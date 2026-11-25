/* Synthetic training text only. */
rule Practice_Blue_Green {
 strings:
  $a = "BLUE-TOKEN" ascii fullword
  $b = "GREEN-TOKEN" ascii fullword
 condition:
  any of them
}

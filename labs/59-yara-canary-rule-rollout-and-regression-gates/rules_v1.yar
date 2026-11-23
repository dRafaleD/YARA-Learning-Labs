/* Toy V1: harmless BLUE token only. */
rule Training_V1_Blue {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
    condition:
        $b
}

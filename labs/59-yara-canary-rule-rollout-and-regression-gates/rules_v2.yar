/* Toy V2: expected expansion to GREEN token. */
rule Training_V2_Blue_Or_Green {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}

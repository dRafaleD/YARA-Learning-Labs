/* Deliberately broader toy rule for comparing regression results. */
rule Toy_Blue_Or_Green {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}

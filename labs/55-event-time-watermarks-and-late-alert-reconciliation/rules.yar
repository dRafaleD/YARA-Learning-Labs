/* Harmless educational tokens only; NOT malware signatures. */
rule Toy_Any_Color {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}
rule Toy_Both_Colors {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        all of them
}

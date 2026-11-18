/* Harmless colored tokens, not real malware indicators. */
rule Toy_Any_Color {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}
rule Toy_Both_Colors {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        all of them
}

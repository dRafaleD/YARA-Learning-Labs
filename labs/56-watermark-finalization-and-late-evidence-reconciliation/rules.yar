/* Harmless strings: intentionally not production malware indicators. */
rule Toy_Color_Any {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}
rule Toy_Color_Both {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
    condition:
        all of them
}

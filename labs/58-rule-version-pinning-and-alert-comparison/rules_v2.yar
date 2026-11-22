/* Harmless training text. Version 2 also detects GREEN. */
rule Toy_V2_Any {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}

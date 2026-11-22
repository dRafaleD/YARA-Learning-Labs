/* Harmless training text. Version 1 deliberately detects only BLUE. */
rule Toy_V1_Blue {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
    condition:
        $blue
}

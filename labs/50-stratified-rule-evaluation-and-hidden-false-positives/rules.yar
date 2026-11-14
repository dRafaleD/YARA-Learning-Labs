/* Harmless training tokens; these are not real malware signatures. */
rule Training_Any {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}

rule Training_Both {
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        all of them
}

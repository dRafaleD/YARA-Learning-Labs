/* Toy V3: deliberate overbroad regression with TRAINING-NOTE. */
rule Training_V3_Overbroad {
    strings:
        $b = "BLUE-TOKEN" ascii fullword
        $g = "GREEN-TOKEN" ascii fullword
        $n = "TRAINING-NOTE" ascii fullword
    condition:
        any of them
}

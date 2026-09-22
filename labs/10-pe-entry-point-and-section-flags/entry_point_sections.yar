import "pe"

rule PE_Entry_Point_Executable_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE entry points and executable section flags"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.section_index(pe.entry_point) >= 0 and
        pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE
}

rule PE_Entry_Point_In_Text_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning pe.section_index with a section name"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.section_index(pe.entry_point) >= 0 and
        pe.section_index(".text") >= 0 and
        pe.section_index(pe.entry_point) == pe.section_index(".text")
}

# Lab 17 Runbook

## Files

- main_rules.yar
- helpers.yar
- samples/match.txt
- samples/no-header.txt
- samples/no-markers.txt

## Command

Run from the Lab 17 directory:

```bash
yara main_rules.yar samples/match.txt
yara main_rules.yar samples/no-header.txt
yara main_rules.yar samples/no-markers.txt
```

## Expected results

- match.txt -> Lab17_Composed_From_Include
- no-header.txt -> no match
- no-markers.txt -> no match

## Important

The include path is resolved relative to how YARA is invoked/environment configuration. Run from the lab directory for this exercise.

Record your local YARA version:

```bash
yara --version
```

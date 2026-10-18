from pathlib import Path
p=Path('samples'); p.mkdir(exist_ok=True)
(p/'positive.txt').write_text('TRAINING_LAB24 document_record\n',encoding='utf-8')
(p/'negative.txt').write_text('ordinary document\n',encoding='utf-8')
print('Prepared harmless fixtures')

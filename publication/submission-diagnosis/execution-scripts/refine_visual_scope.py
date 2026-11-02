from pathlib import Path
import re,subprocess
P=Path('examples/libcamera/config/visuals.yaml');current=P.read_text(encoding='utf-8');base=subprocess.check_output(['git','show','origin/main:examples/libcamera/config/visuals.yaml']).decode()
pattern=r'(?ms)^  request-diagnosis:\n.*?(?=^  [a-z][a-z0-9_-]*:\n|\Z)'
block=re.search(pattern,current).group()
block=block.replace('label: Fatal 로그 → activeStreams_ 비움 → -EINVAL',"label: '코드 위치: Fatal 및 후속 clear·-EINVAL (실행 완료 단정 안 함)'").replace('label_en: Fatal log → clear activeStreams_ → -EINVAL',"label_en: 'Code locations: Fatal and subsequent clear/-EINVAL (execution not asserted)'")
P.write_text(re.sub(pattern,lambda _:block,base),encoding='utf-8')
print('Only request-diagnosis visual block differs from main.')

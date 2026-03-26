import os
import codecs

search_terms = ['오프라인', '발급', '라이선스', '라이센스', '인증']

for filename in os.listdir('CMS-webpage/wireframe_site'):
    if filename.endswith('.html'):
        path = os.path.join('CMS-webpage/wireframe_site', filename)
        try:
            with codecs.open(path, 'r', 'utf-8') as f:
                content = f.read()
                for term in search_terms:
                    if term in content:
                        print(f"Found {term} in {filename}")
        except Exception as e:
            pass

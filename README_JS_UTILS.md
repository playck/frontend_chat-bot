# 프론트엔드 ERP-V@ 유틸 함수 RAG 챗봇 가이드

## 📋 개요

프론트엔드 ERP-v2 유틸 함수들을 RAG(Retrieval-Augmented Generation) 시스템으로 구현한 챗봇입니다.
사용자가 필요한 함수를 자연어로 질문하면, 적절한 유틸 함수를 추천해줍니다.

## 🚀 설정 방법

### 1. 환경 변수 설정

```bash
# .env 파일 생성
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 2. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 벡터 데이터베이스 초기 설정

```bash
# 임베딩 생성 및 Pinecone에 업로드
python embedding_utils.py
```

## 📁 파일 구조

### 핵심 파일들

- `frontend_utils.md`: 프론트엔드 erp-v2 유틸 함수 문서
- `embedding_utils.py`: 임베딩 생성 및 벡터 DB 관리 유틸리티
- `llm.py`: 자바스크립트 함수 특화 RAG 시스템
- `chat.py`: Streamlit 챗봇 UI

## 🔧 임베딩 최적화 전략

### 1. 문서 구조화

각 함수는 다음 구조로 작성되었습니다:

- **목적**: 함수의 역할을 명확히 설명
- **매개변수**: 입력값과 타입 정보
- **반환값**: 출력값 설명
- **사용 예시**: 실제 코드 예제
- **키워드**: 검색 최적화용 키워드

### 2. 마크다운 헤더 분할

```python
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),  # 각 함수별로 분할
    ("###", "Header 3"),
]
```

### 3. 메타데이터 추가

- `source`: 파일 경로
- `chunk_id`: 청크 순서
- `type`: 문서 타입
- `function_name`: 함수명 (자동 추출)

## 💡 사용 예시

### 사용자 질문 예시:

1. "날짜를 YYYY-MM-DD 형식으로 바꾸는 함수 있어?"
2. "배열에서 중복된 값들을 제거하고 싶어"
3. "이메일 주소가 올바른지 확인하는 방법"
4. "객체를 복사하는 함수"

### 예상 답변:

````
formatDate 함수를 추천드립니다! 이 함수는 Date 객체를 원하는 형식의 문자열로 변환해줍니다.

```javascript
function formatDate(date, format) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    return format
        .replace('YYYY', year)
        .replace('MM', month)
        .replace('DD', day);
}

// 사용법
formatDate(new Date(), 'YYYY-MM-DD'); // 2024-01-15
````

## 🔄 새로운 함수 추가 방법

### 1. 수동 추가

```python
# embedding_utils.py 실행
python embedding_utils.py
```

### 2. 자동화된 추가 (권장)

```python
from embedding_utils import update_embeddings

# 새로운 함수 추가 후
update_embeddings('javascript_utils.md')
```

### 3. 실시간 함수 추가 API

```python
from embedding_utils import create_vectorstore
from langchain_community.document_loaders import TextLoader

def add_new_function(function_doc):
    # 새로운 함수 문서를 벡터 DB에 추가
    vectorstore = create_vectorstore([function_doc])
    return "함수가 성공적으로 추가되었습니다!"
```

## 🎯 향후 개선 방안

### 1. 동적 업데이트 시스템

- GitHub Actions를 통한 자동 임베딩
- 파일 감시 시스템으로 실시간 업데이트
- 웹 인터페이스를 통한 함수 추가

### 2. 고급 검색 기능

- 함수 카테고리별 필터링
- 복잡도 레벨별 분류

## 🔍 검색 최적화 팁

### 효과적인 질문 방법:

1. **구체적인 동작 설명**: "날짜 포맷팅" vs "날짜를 YYYY-MM-DD로 바꾸기"
2. **용도 명시**: "배열 처리" vs "배열에서 중복 제거"
3. **키워드 활용**: "검증", "변환", "생성" 등

### 검색 성능 향상:

- 한국어와 영어 키워드 모두 포함
- 함수의 목적과 결과를 명확히 표현
- 예시와 함께 설명 제공

## 🐛 문제 해결

### 일반적인 문제들:

1. **API 키 오류**: 환경 변수 확인
2. **임베딩 실패**: Pinecone 연결 상태 확인
3. **검색 결과 없음**: 키워드 다양화 시도

### 디버깅 방법:

```python
# 검색 테스트
from embedding_utils import search_functions
results = search_functions("날짜 포맷팅", k=3)
for result in results:
    print(result.page_content)
```

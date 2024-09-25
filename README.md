# Ragas Synthetic Dataset Generator

이 프로젝트는 PDF 문서를 기반으로 질문-답변 데이터셋을 생성하는 Python 스크립트입니다. Amazon Bedrock과 Langchain을 사용하여 다양한 유형의 질문을 생성합니다.

## 주요 기능

- PDF 문서 로딩
- Amazon Bedrock을 사용한 텍스트 생성 및 임베딩
- Ragas를 이용한 다양한 유형의 질문 생성
- 생성된 데이터셋을 CSV 파일로 저장

## 필요 조건

- Python 3.7+
- 필요한 라이브러리: nest_asyncio, boto3, langchain, ragas, pandas
- Amazon Bedrock 계정 및 적절한 권한

## 설치

1. 저장소를 클론합니다:
   ```
   git clone https://github.com/NB3025/ragas-bedrock-qagen.git
   ```

2. 필요한 라이브러리를 설치합니다:
   ```
   pip install -r requirements.txt
   ```

3. `config.py` 파일을 생성하고 필요한 설정을 추가합니다:
   ```python
   config = {
       "profile": "your_aws_profile",
       "region": "your_aws_region",
       "bedrock_model_id": "your_bedrock_model_id",
       "bedrock_embedding_model_id": "your_bedrock_embedding_model_id"
   }

   config = {
        "profile": "myprofile",
        "region": "us-east-1",
        "bedrock_model_id": "anthropic.claude-3-haiku-20240307-v1:0",
        "bedrock_embedding_model_id":"amazon.titan-embed-text-v2:0",
    }

   ```

## 사용 방법

1. PDF 파일을 프로젝트 디렉토리에 넣고 `FILE_PATH` 변수를 업데이트합니다.

2. 스크립트를 실행합니다:
   ```
   python generate_dataset.py
   ```

3. 생성된 데이터셋은 `ragas_synthetic_dataset.csv` 파일로 저장됩니다.

## 주의사항

- Amazon Bedrock 사용에 따른 비용이 발생할 수 있습니다.
- 생성된 질문과 답변의 품질은 사용된 모델과 입력 문서의 품질에 따라 달라질 수 있습니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
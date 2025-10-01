# Software Engineering Hands-On Lecture 04 정리

## 개요
이 문서는 "Software Engineering in the era of AI" Week 4 실습 강의 내용을 정리한 노트입니다.

---

## 강의 정보
- **강의명**: CSE4201 – Software Engineering
- **강의 유형**: Hands-On Lecture 04
- **주제**: Software Engineering in the era of AI
- **총 페이지 수**: 17페이지

---

## 실습 목표
### 최종 목표
- **Base64 File Converter** 개발
- PyQt6 GUI 기반 애플리케이션 구현
- GitHub Repository 연결 및 버전 관리
- 소프트웨어 공학 원칙 적용한 개발 프로세스 실습

---

## 페이지별 실습 내용

### Page 1-3: 강의 소개 및 목표 설정
**주요 내용:**
- 강의명: Software Engineering in the era of AI
- **핵심 목표**: Base64 File Converter 개발
- **사용 기술 스택**:
  - PyQt6 GUI Toolkit
  - GitHub Repository 연결
  - File to Base64 구현 및 테스팅
  - 배치 파일 생성
  - 기능 확장

**키워드:**
- Base64 Converter
- PyQt6
- GitHub Integration

---

### Page 4-6: GitHub 환경 설정
**주요 내용:**
- **GitHub Desktop 설치**
  - Download GitHub Desktop | GitHub Desktop
- **새 Repository 생성**
  - Create a new repo 과정
- **버전 관리 시스템 설정**

**실습 단계:**
1. GitHub Desktop 다운로드 및 설치
2. 새로운 Repository 생성
3. 로컬 환경과 연결

**키워드:**
- GitHub Desktop
- Repository Creation
- Version Control

---

### Page 7: 개발 환경 설정 (실습 1)
**제목:** 가상환경 생성 및 PyQt6 설치

**주요 내용:**
- **가상환경 생성**:
  ```bash
  # Windows
  python -m venv venv
  venv\scripts\activate
  
  # Mac/Linux
  python3 -m venv venv
  source venv/bin/activate
  ```

- **라이브러리 설치**:
  ```bash
  pip install PyQt6
  ```

- **개발 도구 실행**:
  ```bash
  code  # VS Code 실행
  ```

**실습 체크리스트:**
- [ ] 프로젝트 폴더 생성
- [ ] 터미널에서 가상환경 생성
- [ ] 가상환경 활성화
- [ ] PyQt6 설치
- [ ] VS Code 실행

**키워드:**
- Virtual Environment
- PyQt6 Installation
- Development Setup

---

### Page 8: 프로젝트 계획 수립 (실습 2)
**제목:** 목표 분석 및 PRD 설계

**주요 내용:**
- **문서 작성 도구**: 메모장/텍스트 편집기 활용
- **포함해야 할 내용**:

**[1] 최종 목표 정의**
- PyQt6 기반의 File to Base64 Converter 개발

**[2] 구현 계획**
- **1단계**: CLI에서 실행 가능한 File to Base64 변환 코드 개발
  - 입력: 파일 경로
  - 출력: .txt 파일
- **2단계**: PyQt6 기반 GUI로 확장

**[3] 문서 작성**
- SRS(Software Requirements Specification) 문서 작성
- 체크리스트 마크다운 문서 작성

**실습 체크리스트:**
- [ ] PRD(Product Requirements Document) 작성
- [ ] 구현 계획 수립
- [ ] SRS 문서 초안 작성
- [ ] 개발 체크리스트 작성

**키워드:**
- PRD (Product Requirements Document)
- SRS (Software Requirements Specification)
- Implementation Planning
- CLI to GUI Migration

---

### Page 9: 개발 도구 설정
**제목:** Codex CLI Windows 승인 이슈 해결

**주요 내용:**
- **Windows 전용 설정**:
  ```toml
  approval_mode = "full-auto"
  ```
  - config.toml 파일 수정 필요 (직접 작성, 복붙 금지)
  - Mac/Linux(WSL)에서는 문제 없음

**기술적 참고사항:**
- Windows 환경에서 Codex CLI 사용 시 승인 모드 설정 필요
- 보안 및 자동화 관련 설정

**키워드:**
- Codex CLI
- Windows Configuration
- Approval Mode

---

### Page 10-12: AI 도구 활용
**제목:** Claude Code 샘플

**주요 내용:**
- AI 코드 생성 도구 활용 예시
- Claude를 통한 코드 샘플 생성
- 실제 개발에서 AI 도구 활용법

**실무 적용:**
- AI 도구를 활용한 코드 스켈레톤 생성
- 개발 효율성 향상
- AI 생성 코드의 검토 및 수정

**키워드:**
- AI Code Generation
- Claude AI
- Code Samples

---

### Page 13-14: UI 디자인
**제목:** UI 스켈레톤 제작

**주요 내용:**
- **디자인 도구**:
  - 그림판
  - PowerPoint
  - **Figma**: https://www.figma.com (추천)

- **UI 설계 과정**:
  1. UI 스켈레톤 디자인
  2. 사용자 인터페이스 레이아웃 계획
  3. 사용성 고려한 설계

**실습 체크리스트:**
- [ ] UI 스켈레톤 스케치 작성
- [ ] Figma를 통한 디지털 디자인
- [ ] 사용자 경험(UX) 고려사항 정리

**키워드:**
- UI Skeleton
- Figma Design
- User Interface Planning

---

### Page 15-16: 버전 관리
**제목:** Git Push (Publish) 및 지속적 개발

**주요 내용:**
- **Git 작업 플로우**:
  - Git Push를 통한 코드 게시
  - GitHub Repository 업데이트
  - 지속적인 개발(Continuous Development)

- **협업 및 배포**:
  - 코드 공유 및 협업
  - 버전 관리를 통한 안정성 확보

**키워드:**
- Git Push
- Continuous Development
- Code Publishing

---

### Page 17: 과제 및 평가
**제목:** TODO 및 확장 계획

**주요 내용:**
**과제 1**: 내 File to Base64 Convert Tool 리뷰 + 간단 평가 (문제점) – 1페이지 고정

**과제 2**: Base64 to File을 함께 지원하는 도구로의 확장 방안을 담은 SRS 문서 작성

**확장 계획:**
- 양방향 변환 지원 (File ↔ Base64)
- 기능 확장 및 개선
- 사용자 피드백 반영

**키워드:**
- Tool Evaluation
- SRS Extension
- Bidirectional Conversion

---

## 전체 실습 플로우 요약

### 1단계: 환경 설정
1. GitHub Desktop 설치 및 Repository 생성
2. 가상환경 생성 및 PyQt6 설치
3. 개발 도구(VS Code) 설정

### 2단계: 프로젝트 계획
1. PRD 작성 및 목표 정의
2. SRS 문서 초안 작성
3. 구현 계획 수립

### 3단계: 설계 및 개발
1. UI 스켈레톤 디자인 (Figma 활용)
2. CLI 버전 File to Base64 Converter 구현
3. AI 도구(Claude) 활용한 코드 생성

### 4단계: 확장 및 배포
1. GUI 버전으로 확장 (PyQt6)
2. Git을 통한 버전 관리
3. 기능 확장 계획 수립

---

## 학습 목표 달성 체크리스트

### 기술적 목표
- [ ] Python 가상환경 구성 및 관리
- [ ] PyQt6 GUI 애플리케이션 개발
- [ ] Base64 인코딩/디코딩 구현
- [ ] Git/GitHub를 통한 버전 관리
- [ ] AI 도구를 활용한 개발 효율성 향상

### 소프트웨어 공학적 목표
- [ ] 요구사항 분석 및 문서화 (PRD, SRS)
- [ ] 단계적 개발 접근법 (CLI → GUI)
- [ ] UI/UX 설계 원칙 적용
- [ ] 테스팅 및 품질 보증
- [ ] 지속적 통합 및 배포

### 실무 역량
- [ ] 프로젝트 계획 및 관리
- [ ] 문서화 및 커뮤니케이션
- [ ] 도구 활용 능력 (GitHub, Figma, AI)
- [ ] 문제 해결 및 디버깅
- [ ] 확장성 고려한 설계

---

## 사용된 도구 및 기술

### 개발 도구
- **Python**: 메인 개발 언어
- **PyQt6**: GUI 프레임워크
- **VS Code**: 통합 개발 환경
- **Git/GitHub**: 버전 관리 및 협업

### 설계 도구
- **Figma**: UI/UX 디자인
- **PowerPoint/그림판**: 스케치 도구
- **메모장**: 문서 작성

### AI 도구
- **Claude**: 코드 생성 및 문서 작성
- **Codex CLI**: 개발 자동화

---

## 실무 적용 포인트

### 소프트웨어 공학 원칙 적용
1. **요구사항 엔지니어링**: 명확한 목표 설정 및 문서화
2. **반복적 개발**: CLI → GUI 단계적 접근
3. **품질 관리**: 테스팅 및 평가 과정 포함
4. **버전 관리**: Git을 통한 체계적 코드 관리

### AI 시대 개발 패러다임
1. **AI 도구 활용**: 개발 효율성 극대화
2. **인간-AI 협업**: AI 생성 코드 검토 및 개선
3. **지속적 학습**: 새로운 도구 및 기술 적응

---

## 참고사항
- 원본 파일: Software Engineering - week4.pdf
- 작성일: 2025년 10월 1일
- 강의 유형: 실습 중심 핸즈온 강의
- 총 페이지 수: 17페이지
- 추출 방법: pdfplumber 라이브러리 사용

## 완료 체크리스트
- [x] PDF 내용 실제 추출 및 확인
- [x] 실습 단계별 내용 체계적 정리
- [x] 기술 스택 및 도구 정리
- [x] 학습 목표 및 체크리스트 작성
- [x] 소프트웨어 공학 원칙과의 연계성 분석
- [x] 실무 적용 가이드라인 제공
- [ ] 실제 실습 과제 수행 (필요 시)
- [ ] 다른 Week와의 연계성 분석 (추후 수행)
import pdfplumber
import os
import sys

def extract_pdf_text(pdf_path):
    """PDF 파일에서 텍스트를 추출하는 함수"""
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"총 페이지 수: {len(pdf.pages)}")
            
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"페이지 {page_num} 처리 중...")
                
                # 페이지에서 텍스트 추출
                text = page.extract_text()
                
                if text:
                    text_content.append({
                        'page': page_num,
                        'content': text.strip()
                    })
                else:
                    print(f"페이지 {page_num}에서 텍스트를 찾을 수 없습니다.")
                    
    except Exception as e:
        print(f"PDF 처리 중 오류 발생: {e}")
        return None
    
    return text_content

def save_extracted_text(text_content, output_path):
    """추출된 텍스트를 파일로 저장"""
    # extracted_texts 디렉토리가 존재하지 않으면 생성
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# PDF 내용 추출 결과\n\n")
        
        for page_data in text_content:
            f.write(f"## 페이지 {page_data['page']}\n\n")
            f.write(f"{page_data['content']}\n\n")
            f.write("---\n\n")

def process_pdf_file(pdf_relative_path, output_filename):
    """PDF 파일을 처리하여 텍스트를 추출하고 extracted_texts 폴더에 저장"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, pdf_relative_path)
    output_path = os.path.join(current_dir, "extracted_texts", output_filename)
    
    print(f"PDF 텍스트 추출을 시작합니다: {pdf_relative_path}")
    
    if not os.path.exists(pdf_path):
        print(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
        return False
    
    text_content = extract_pdf_text(pdf_path)
    
    if text_content:
        save_extracted_text(text_content, output_path)
        print(f"텍스트 추출 완료! 결과가 {output_path}에 저장되었습니다.")
        
        # 각 페이지 내용 미리보기
        for page_data in text_content[:2]:  # 처음 2페이지만 미리보기
            print(f"\n=== 페이지 {page_data['page']} 미리보기 ===")
            preview = page_data['content'][:300]  # 처음 300자만
            print(preview)
            if len(page_data['content']) > 300:
                print("... (내용이 더 있습니다)")
        return True
    else:
        print("텍스트 추출에 실패했습니다.")
        return False

if __name__ == "__main__":
    # 사용 예시들
    pdf_files = [
        # 이론 과제
        ("이론/과제/이론 과제 #1.pdf", "extracted_text_assignment1.txt"),
        ("이론/과제/이론 과제 #2.pdf", "extracted_text_assignment2.txt"),
        # 이론 수업
        ("이론/수업/Chapter1.pdf", "extracted_text_ch1.txt"),
        ("이론/수업/Chapter2.pdf", "extracted_text_ch2.txt"),
        # 실습 수업
        ("실습/수업/Software Engineering - week1.pdf", "extracted_text_week1.txt"),
        ("실습/수업/Software Engineering - week2.pdf", "extracted_text_week2.txt"),
        ("실습/수업/Software Engineering - week3.pdf", "extracted_text_week3.txt"),
        ("실습/수업/Software Engineering - week4.pdf", "extracted_text_week4.txt"),
    ]
    
    # 명령행 인수가 있으면 특정 파일만 처리
    if len(sys.argv) > 1:
        file_index = int(sys.argv[1]) - 1
        if 0 <= file_index < len(pdf_files):
            pdf_path, output_file = pdf_files[file_index]
            process_pdf_file(pdf_path, output_file)
        else:
            print(f"인덱스는 1부터 {len(pdf_files)} 사이여야 합니다.")
            print("\n사용 가능한 파일들:")
            for i, (pdf_path, output_file) in enumerate(pdf_files, 1):
                print(f"{i}. {pdf_path} -> {output_file}")
    else:
        # 기본적으로 이론 과제 #2 처리
        process_pdf_file("이론/과제/이론 과제 #2.pdf", "extracted_text_assignment2.txt")
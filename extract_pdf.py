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
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Chapter 1 PDF 내용 추출 결과\n\n")
        
        for page_data in text_content:
            f.write(f"## 페이지 {page_data['page']}\n\n")
            f.write(f"{page_data['content']}\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    pdf_path = r"c:\Users\qqpmzz\Desktop\GitHub\SWE\이론\과제\이론 과제 #2.pdf"
    output_path = r"c:\Users\qqpmzz\Desktop\GitHub\SWE\extracted_text_assignment2.txt"
    
    print("PDF 텍스트 추출을 시작합니다...")
    
    if not os.path.exists(pdf_path):
        print(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
        sys.exit(1)
    
    text_content = extract_pdf_text(pdf_path)
    
    if text_content:
        save_extracted_text(text_content, output_path)
        print(f"텍스트 추출 완료! 결과가 {output_path}에 저장되었습니다.")
        
        # 각 페이지 내용 미리보기
        for page_data in text_content[:3]:  # 처음 3페이지만 미리보기
            print(f"\n=== 페이지 {page_data['page']} 미리보기 ===")
            preview = page_data['content'][:500]  # 처음 500자만
            print(preview)
            if len(page_data['content']) > 500:
                print("... (내용이 더 있습니다)")
    else:
        print("텍스트 추출에 실패했습니다.")
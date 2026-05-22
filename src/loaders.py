import uuid
import os
from pypdf import PdfReader

def file_loader(file_path:str)->dict:
    
    if not os.path.exists(file_path):
        return None
    
    doc_content=[]

    if file_path.lower().endswith('.pdf'):
        doc=PdfReader(file_path)

        for page in doc.pages:
            text=page.extract_text()
            if text:
                doc_content.append(text)
            
        extracted_content='\n'.join(doc_content)

    elif file_path.lower().endswith(('.txt', '.md','.csv','.py')):
        with open(file_path,"r",encoding='utf-8') as fp:
            extracted_content=fp.read()
    else:
        return None
    
    
    return {
            'id':str(uuid.uuid4()),
            'source_path':file_path,
            'text':extracted_content
        }

# PDF → Load → Chunk → Embed → Store → Retrieve → LLM → Answer

#Imports

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI



def buildprompt(task,context,job_description):
    if task == "Match Score":

        prompt= f'''

        - You are expert recuirter who analyze the resume very precisely.
        - You can extract the meaningfull information from the resume very efficiently.
        - You match the resume with the job description with 100 percent accuracy.
        - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
        - You provide the insight to the candidate after matching the resume and job description as per industry standards.
        - You do not answer or give insight to make the person happy or please.
        - You are brutally honest and logical with your analysis.
        
        Resume:
        {context}
        
        Job description:
        {job_description}

        Return only:

        # Match Score:  <percentage>

        ## Reason for Score

        - Why Score is high?
        - Why Score is reduced?

        Rules:

        - Do not include the candidate details and job description in output response.
        - Score must be percentage only
        - No extra sections

        '''
    elif task == "Matching Skills":
        prompt= f'''

        - You are expert recuirter who analyze the resume very precisely.
        - You can extract the meaningfull information from the resume very efficiently.
        - You match the resume with the job description with 100 percent accuracy.
        - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
        - You provide the insight to the candidate after matching the resume and job description as per industry standards.
        - You do not answer or give insight to make the person happy or please.
        - You are brutally honest and logical with your analysis.
        
        Resume:
        {context}
        
        Job description:
        {job_description}

        Return only:

        # Matching skills
        - Skill 1
        - Skill 2
        - Skill 3
        - Skill 4
        - Skill 5
        - Skill 6
        - Skill 7
        - Skill 8
        - Skill 9
        - Skill 10
        
        
        Rules:

        - Do not include the candidate details and job description in output response.
        - No Explanation
        - No extra sections

        '''



    elif task == "Missing Skills":
        prompt= f'''

        - You are expert recuirter who analyze the resume very precisely.
        - You can extract the meaningfull information from the resume very efficiently.
        - You match the resume with the job description with 100 percent accuracy.
        - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
        - You provide the insight to the candidate after matching the resume and job description as per industry standards.
        - You do not answer or give insight to make the person happy or please.
        - You are brutally honest and logical with your analysis.
        
        Resume:
        {context}
        
        Job description:
        {job_description}

        Return only:

        # Missing skills
        - Skill 1
        - Skill 2
        - Skill 3
        - Skill 4
        - Skill 5
        - Skill 6
        - Skill 7
        - Skill 8
        - Skill 9
        - Skill 10

        Rules:

        - Do not include the candidate details and job description in output response.
        - No Explanation
        - No extra sections

        '''

    elif task == "Sugeestions":
        prompt= f'''

        - You are expert recuirter who analyze the resume very precisely.
        - You can extract the meaningfull information from the resume very efficiently.
        - You match the resume with the job description with 100 percent accuracy.
        - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
        - You provide the insight to the candidate after matching the resume and job description as per industry standards.
        - You do not answer or give insight to make the person happy or please.
        - You are brutally honest and logical with your analysis.
        
        Resume:
        {context}
        
        Job description:
        {job_description}

        Return only:

        # Suggestions
        - Suggestion 1
        - Suggestion 2
        - Suggestion 3
        - Suggestion 4
        - Suggestion 5
        - Suggestion 6
        - Suggestion 7
        - Suggestion 8
        - Suggestion 9
        - Suggestion 10


        Rules:

        - Do not include the candidate details and job description in output response.
        - No extra sections

        '''

    else:
        prompt= f'''

        - You are expert recuirter who analyze the resume very precisely.
        - You can extract the meaningfull information from the resume very efficiently.
        - You match the resume with the job description with 100 percent accuracy.
        - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
        - You provide the insight to the candidate after matching the resume and job description as per industry standards.
        - You do not answer or give insight to make the person happy or please.
        - You are brutally honest and logical with your analysis.
        
        Resume:
        {context}
        
        Job description:
        {job_description}

        Return the response only in the follwing format:

        # Match Score:  <percentage>

        ## Reason for Score

        - Why Score is high?
        - Why Score is reduced?

        # Matching skills
        - Skill 1
        - Skill 2
        - Skill 3
        - Skill 4
        - Skill 5
        - Skill 6
        - Skill 7
        - Skill 8
        - Skill 9
        - Skill 10

        # Missing skills
        - Skill 1
        - Skill 2
        - Skill 3
        - Skill 4
        - Skill 5
        - Skill 6
        - Skill 7
        - Skill 8
        - Skill 9
        - Skill 10

        # Suggestions
        - Suggestion 1
        - Suggestion 2
        - Suggestion 3
        - Suggestion 4
        - Suggestion 5
        - Suggestion 6
        - Suggestion 7
        - Suggestion 8
        - Suggestion 9
        - Suggestion 10


        Rules:

        - Match Score must be in percentage only.
        - Keep output in detail.
        - No extra Section.
        - No candidate summary.
        - No education summary unless relevent.
        - No certification details unless relvent.
        - Do not include the candidate details and job description in output response.

        '''
    return prompt

def analyze_resume(resume_file,job_description,task,custom_query):

    try:

        file_path = resume_file


        loader=PyPDFLoader(file_path)
        docs = loader.load()

        #Chunk
        splitter= RecursiveCharacterTextSplitter(
                chunk_size=700,
                chunk_overlap=100
            )

        chunks=splitter.split_documents(docs)
        
        #embedding
        embedding=OpenAIEmbeddings()
        
        #vector database
        vectorstore= FAISS.from_documents(chunks,embedding)


        #query
        if custom_query.strip():
            query = custom_query
        else:
            query = f"Perform {task} analysis"

        #Retrieval
        results=vectorstore.similarity_search(query,k=3)


        context = " ".join([r.page_content for r in results])

        
        ## Promting routing

        if custom_query.strip():
             prompt= f'''

                - You are expert recuirter who analyze the resume very precisely.
                - You can extract the meaningfull information from the resume very efficiently.
                - You match the resume with the job description with 100 percent accuracy.
                - You are the best in matching and extracting the meaningfull information from the resume for both candidate as well as organization.
                - You provide the insight to the candidate after matching the resume and job description as per industry standards.
                - You do not answer or give insight to make the person happy or please.
                - You are brutally honest and logical with your analysis.
                
                Resume:
                {context}
                
                Job description:
                {job_description}

                User Query:
                {custom_query}

                Rules:

                - Match Score must be in percentage only.
                - Keep output in detail.
                - No extra Section.
                - No candidate summary.
                - No education summary unless relevent.
                - No certification details unless relvent.
                - Do not include the candidate details and job description in output response.

                '''
        else:
            prompt= buildprompt(task,context,job_description)


        # LLM
        
        client = OpenAI()
        response = client.chat.completions.create(
                model="gpt-4o-mini",

                temperature=0,

                max_tokens=500,

                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", str(e))
        return f"Error: {str(e)}"